import json
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"

def _load_json(path: Path) -> dict | list:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def load_knowledge() -> dict:
    """
    Returns a dict keyed by relative path, e.g.:
      {
        "entities/demons": [...72 demon dicts...],
        "core/hierarchy": {...},
        "agent/question_patterns": {...},
        ...
      }
    """
    kb = {}
    for path in KNOWLEDGE_DIR.rglob("*.json"):
        rel = path.relative_to(KNOWLEDGE_DIR).with_suffix("").as_posix()
        kb[rel] = _load_json(path)
    return kb

# Load once at import — Streamlit reruns the script, so this avoids re-reading disk
KNOWLEDGE = load_knowledge()

def get_demons() -> list[dict]:
    return KNOWLEDGE["entities/demons"]["demons"]

def get_safety_rules() -> list[dict]:
    return KNOWLEDGE["agent/safety_rules"]["safety_rules"]

def get_question_patterns() -> list[dict]:
    return KNOWLEDGE["agent/question_patterns"]["question_patterns"]

def get_source(source_id: str) -> dict | None:
    for s in KNOWLEDGE["research/sources"]["sources"]:
        if s["id"] == source_id:
            return s
    return None