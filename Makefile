# Makefile — contributors run the SAME checks locally that CI runs (the
# awesome-selfhosted pattern: "CI is just `make` in Actions"). See README's
# Contributing pointer + .github/workflows/validate.yml.
#
# Targets:
#   make install        create .venv + install Python deps; print Node tool note
#   make schema_check   validate data/skills/*.yml against the JSON Schema + rules
#   make awesome_lint   run awesome-lint on README.md (Gate A)
#   make link_check     run lychee on the READMEs (link health) with allowlist
#   make generate       regenerate README.md + README.zh-CN.md from data
#   make gen_data       regenerate web/src/data.json from data (the site's data source)
#   make build_site     build the React companion site (web/ -> docs/) via npm
#   make check_drift    fail if the committed READMEs or web/src/data.json differ from a fresh render
#   make security_scan  Tier-1 static scan (self-test by default; PR_REPO=<url>)
#   make update_metadata refresh CI-maintained fields from the GitHub API
#   make check_unmaintained flag entries with no activity in 6-12 months
#   make all            schema_check + awesome_lint + generate + check_drift
#   make clean          remove .venv and caches

SHELL := /bin/bash

# Use the venv's python if it exists, else fall back to system python3.
VENV    := .venv
PY      := $(shell [ -x "$(VENV)/bin/python" ] && echo "$(VENV)/bin/python" || echo "python3")
PIP     := $(VENV)/bin/pip

# Pin awesome-lint so local == CI (RF §4 pinning ethos, applied to npm too).
AWESOME_LINT_VERSION := 2.3.0
LYCHEE_ARGS := --no-progress --config lychee.toml

.PHONY: install schema_check check_public awesome_lint link_check generate gen_data build_site check_drift security_scan update_metadata check_unmaintained all clean help

help:
	@grep -E '^#   make ' Makefile | sed 's/^#   //'

install:
	@echo ">> Creating venv + installing Python deps (jinja2, pyyaml, jsonschema)…"
	python3 -m venv $(VENV)
	$(PIP) install --quiet --upgrade pip
	$(PIP) install --quiet jinja2 pyyaml jsonschema requests
	@echo ">> Python deps ready in $(VENV)."
	@echo ">> Node tools (run via npx, no install needed): awesome-lint@$(AWESOME_LINT_VERSION), lychee (link_check uses the lycheeverse action in CI; locally install lychee or use npx)."

schema_check:
	$(PY) scripts/schema_check.py

# Hard gate: every listed repo must be PUBLICLY reachable (unauthenticated). Catches a
# private repo that slipped in via an authenticated discovery token. Needs network.
check_public:
	$(PY) scripts/check_public.py

awesome_lint:
	npx --yes awesome-lint@$(AWESOME_LINT_VERSION)

# Local link check. CI uses lycheeverse/lychee-action (pinned SHA); locally we
# call the lychee binary if installed, else hint how to get it.
link_check:
	@if command -v lychee >/dev/null 2>&1; then \
		lychee $(LYCHEE_ARGS) README.md README.zh-CN.md ; \
	else \
		echo "lychee not installed locally. Install: 'brew install lychee' or 'cargo install lychee'." ; \
		echo "(CI runs the pinned lycheeverse/lychee-action with lychee.toml — see validate.yml.)" ; \
	fi

generate:
	$(PY) scripts/generate_readme.py

# Regenerate the site's data source (web/src/data.json) from the SAME data layer
# as the README (data/skills + framework/analysis.yml + config.yaml). Deterministic.
gen_data:
	$(PY) web/scripts/gen_data.py

# Build the React companion site (web/ -> docs/) via npm. Runs gen_data first
# (npm "build" script also runs it). Requires Node 20 + a one-time `npm --prefix web ci`.
build_site:
	npm --prefix web run build

# Drift gate: the committed READMEs AND the site's data source must match a fresh
# render. We drift-check web/src/data.json (deterministic Python output), NOT the
# Vite bundle in docs/ (its asset hashes are a build artifact, intentionally not
# diffed). Rebuild docs/ via `make build_site` when data changes.
check_drift: generate gen_data
	@git diff --exit-code README.md README.zh-CN.md web/src/data.json \
		&& echo ">> READMEs + site data match the generator (no drift)." \
		|| (echo ">> DRIFT: a generated file is out of date — run 'make generate gen_data' and commit." ; exit 1)

security_scan:
	@if [ -n "$(PR_REPO)" ]; then \
		$(PY) framework/scanner/security_scan.py --repo "$(PR_REPO)" ; \
	else \
		$(PY) framework/scanner/security_scan.py --self-test ; \
	fi

update_metadata:
	$(PY) scripts/update_metadata.py

check_unmaintained:
	$(PY) scripts/check_unmaintained.py

all: schema_check awesome_lint generate check_drift
	@echo ">> all checks passed."

clean:
	rm -rf $(VENV) .mypy_cache .pytest_cache **/__pycache__ scripts/__pycache__ scripts/lib/__pycache__ .lychee.cache
