import re
from urllib.parse import urlsplit

RISK_PHRASES = {
    "credential_request": ("verify your password", "send your password", "share your otp", "enter your one time password"),
    "pressure": ("act immediately", "account will be suspended", "urgent action required"),
    "payment": ("pay a verification fee", "send gift cards"),
}

def scan_text(message: str) -> dict:
    if not isinstance(message, str):
        raise TypeError("message must be a string")
    normalized = " ".join(message.casefold().split())
    findings = [name for name, phrases in RISK_PHRASES.items() if any(phrase in normalized for phrase in phrases)]
    return {"risk": "high" if len(findings) >= 2 else "caution" if findings else "unknown", "signals": findings, "note": "Heuristic signals only; not proof of a scam."}

def assess_url(url: str) -> dict:
    if not isinstance(url, str):
        raise TypeError("url must be a string")
    try:
        parts = urlsplit(url.strip())
        host = parts.hostname or ""
        if parts.scheme not in ("http", "https") or not host:
            return {"risk": "invalid", "signals": ["invalid_url"]}
        signals = []
        if parts.scheme == "http":
            signals.append("unencrypted_http")
        if "@" in parts.netloc:
            signals.append("userinfo_in_url")
        if host.startswith("xn--") or ".xn--" in host:
            signals.append("internationalized_domain")
        if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", host):
            signals.append("ip_address_host")
        return {"risk": "caution" if signals else "unknown", "signals": signals, "host": host, "note": "No network requests are made. Unknown does not mean safe."}
    except ValueError:
        return {"risk": "invalid", "signals": ["invalid_url"]}
