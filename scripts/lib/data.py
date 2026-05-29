"""Data + config loading helpers, shared by the generator and the schema check.

Pure stdlib + PyYAML. No third-party deps so contributors can run it anywhere.
"""

from __future__ import annotations

import os
import sys
from typing import Any

import yaml

# --- Repo layout -----------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
# DATA_DIR may be overridden via $AAS_DATA_DIR (used for isolated smoke-tests against
# a sanitized copy without mutating the canonical data/skills/*.yml).
DATA_DIR = os.environ.get("AAS_DATA_DIR") or os.path.join(REPO_ROOT, "data", "skills")
SCHEMA_PATH = os.path.join(REPO_ROOT, "schema", "skill.schema.json")
CONFIG_PATH = os.path.join(REPO_ROOT, "config.yaml")
TEMPLATES_DIR = os.path.join(REPO_ROOT, "templates")
README_EN = os.path.join(REPO_ROOT, "README.md")
README_ZH = os.path.join(REPO_ROOT, "README.zh-CN.md")


def load_yaml(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_config() -> dict:
    cfg = load_yaml(CONFIG_PATH)
    if not isinstance(cfg, dict):
        raise ValueError(f"config.yaml did not parse to a mapping: {CONFIG_PATH}")
    return cfg


def entry_files() -> list[str]:
    """All data/skills/*.yml paths, sorted by filename for determinism."""
    if not os.path.isdir(DATA_DIR):
        return []
    names = [
        n
        for n in os.listdir(DATA_DIR)
        if n.endswith(".yml") and not n.startswith(".")
    ]
    return [os.path.join(DATA_DIR, n) for n in sorted(names)]


def load_entries() -> list[dict]:
    """Load every entry YAML into a list of dicts (sorted by filename)."""
    out: list[dict] = []
    for path in entry_files():
        data = load_yaml(path)
        if not isinstance(data, dict):
            raise ValueError(f"{path}: top-level YAML is not a mapping")
        data["_path"] = path
        data["_filename"] = os.path.basename(path)
        out.append(data)
    return out


def eprint(*args: Any) -> None:
    print(*args, file=sys.stderr)
