# PromptShield

A CLI tool that validates LLM prompts and responses to detect injection attacks. Runs entirely offline, inspecting text input against patterns of known injection techniques.

## Tech Stack
- Python 3.11+
- Click (CLI interface)
- Pytest (testing)

## Usage
```bash
# Install
pip install -e .

# Validate a prompt
promptshield validate --type prompt "your text here"

# Validate a response
promptshield validate --type response "LLM output here"
```

## Development
```bash
./init.sh    # Install dependencies
pytest        # Run tests
```
