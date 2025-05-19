#!/usr/bin/env bash

echo "Installing uv"
curl -LsSf https://astral.sh/uv/install.sh | sh

echo "Creating a virtual environment"

uv venv
source .venv/bin/activate
uv sync

exit 0