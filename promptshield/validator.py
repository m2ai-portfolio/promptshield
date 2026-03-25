"""Validation logic and pattern sets for prompt injection detection."""

from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of a validation check."""
    is_safe: bool
    reason: str | None = None


# Patterns that indicate prompt injection attempts
PROMPT_INJECTION_PATTERNS = {
    "ignore previous instructions",
    "act as",
    "dan",
    "jailbreak",
    "forget ethics",
    "you are now",
    "unfiltered",
    "bypass",
    "override",
    "system:",
}

# Indicators that a response has been compromised
RESPONSE_COMPROMISE_INDICATORS = {
    "i am dan",
    "system:",
    "my instructions are",
    "i ignore",
    "unlocked",
    "developer mode",
    "pretend",
    "as an ai",
}


def validate_prompt(text: str) -> ValidationResult:
    """
    Validate a prompt for injection patterns.

    Args:
        text: The prompt text to validate

    Returns:
        ValidationResult indicating if the prompt is safe and why
    """
    if not text:
        return ValidationResult(is_safe=True)

    text_lower = text.lower()

    for pattern in PROMPT_INJECTION_PATTERNS:
        if pattern in text_lower:
            return ValidationResult(is_safe=False, reason=pattern)

    return ValidationResult(is_safe=True)


def validate_response(text: str) -> ValidationResult:
    """
    Validate a response for compromise indicators.

    Args:
        text: The response text to validate

    Returns:
        ValidationResult indicating if the response is safe and why
    """
    if not text:
        return ValidationResult(is_safe=True)

    text_lower = text.lower()

    for indicator in RESPONSE_COMPROMISE_INDICATORS:
        if indicator in text_lower:
            return ValidationResult(is_safe=False, reason=indicator)

    return ValidationResult(is_safe=True)
