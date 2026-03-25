"""PromptShield - CLI tool to detect LLM prompt injection attacks."""

from promptshield.validator import (
    ValidationResult,
    PROMPT_INJECTION_PATTERNS,
    RESPONSE_COMPROMISE_INDICATORS,
    validate_prompt,
    validate_response,
)

__version__ = "0.1.0"

__all__ = [
    "ValidationResult",
    "PROMPT_INJECTION_PATTERNS",
    "RESPONSE_COMPROMISE_INDICATORS",
    "validate_prompt",
    "validate_response",
]
