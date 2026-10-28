"""EDEN deterministic safety policy prototype. No device access or enforcement."""

from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ALLOW = "allow"
    REVIEW = "review"
    BLOCK = "block"


@dataclass(frozen=True)
class SecurityEvent:
    category: str
    authorized: bool
    verified: bool
    severity: int = 0


def evaluate(event: SecurityEvent) -> Decision:
    """Keep unknown or untrusted activity restricted until reviewed."""
    if not 0 <= event.severity <= 10:
        raise ValueError("severity must be between 0 and 10")
    if event.category not in {"usb", "network", "application", "archive", "red_team"}:
        return Decision.REVIEW
    if event.category == "red_team" and not event.authorized:
        return Decision.BLOCK
    if not event.authorized:
        return Decision.BLOCK
    if not event.verified or event.severity >= 7:
        return Decision.REVIEW
    return Decision.ALLOW
