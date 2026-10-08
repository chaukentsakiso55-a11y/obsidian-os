from .guardian import assess_url, scan_text

WEIGHTS = {
    "credential_request": 45,
    "pressure": 30,
    "payment": 40,
    "unencrypted_http": 25,
    "userinfo_in_url": 45,
    "internationalized_domain": 15,
    "ip_address_host": 20,
}

def score_signals(signals):
    unique = sorted(set(signals))
    score = min(100, sum(WEIGHTS.get(signal, 0) for signal in unique))
    level = "high" if score >= 60 else "caution" if score > 0 else "unknown"
    return {"score": score, "risk": level, "signals": unique, "note": "Heuristic score; zero is not a safety guarantee."}

def analyze(kind, value):
    if kind not in ("text", "url"):
        raise ValueError("kind must be text or url")
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    if len(value) > 10000:
        raise ValueError("input exceeds 10000 characters")
    result = scan_text(value) if kind == "text" else assess_url(value)
    if result["risk"] == "invalid":
        return {"score": None, "risk": "invalid", "signals": result["signals"]}
    return score_signals(result["signals"])
