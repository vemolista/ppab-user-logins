#!/usr/bin/env bash

set -e

echo "Downloading SQLite"
sudo apt-get update
sudo apt-get install sqlite3

echo "Create DB"
sqlite3 db/db.db < db/schema.sql
sqlite3 db/db.db < db/seed.sql

echo "Installing uv"
curl -LsSf https://astral.sh/uv/install.sh | sh

echo "Creating a virtual environment"

uv venv
source .venv/bin/activate
uv sync

exit 0