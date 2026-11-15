from rapidfuzz import process, fuzz
from utils.loader import get_demons

# Build flattened index once
_demons = get_demons()

# For each demon, build searchable keys: name, all aliases, rank words, power words
_index = []
for d in _demons:
    keys = [d["name"]] + d.get("aliases", []) + [d["rank"]]
    keys += d.get("powers", [])
    _index.append({
        "number": d["number"],
        "name": d["name"],
        "keys": [k.lower() for k in keys],
        "entry": d,
    })

def _score_entry(entry: dict, query_lower: str) -> float:
    best = 0.0
    for key in entry["keys"]:
        s = fuzz.partial_ratio(query_lower, key)
        if s > best:
            best = s
    return best

def search_demons(query: str, limit: int = 3, threshold: float = 70.0) -> list[dict]:
    """
    Returns up to `limit` demon entries whose fuzzy score ≥ threshold,
    sorted best-first. Empty list if nothing matches.
    """
    q = query.lower().strip()
    if not q:
        return []
    scored = [(e["entry"], _score_entry(e, q)) for e in _index]
    scored = [x for x in scored if x[1] >= threshold]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in scored[:limit]]

def search_any(query: str, limit: int = 3) -> list[dict]:
    """
    Simple alias — you may want to add rank/power-specific retrievers later.
    """
    return search_demons(query, limit=limit)