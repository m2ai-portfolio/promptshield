#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 -m pip install --quiet click pytest
pip install --quiet -e . 2>/dev/null || true
echo "PromptShield development environment ready."
