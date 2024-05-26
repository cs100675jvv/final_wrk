#!/bin/sh

git clone https://github.com/cs100675jvv/project-f16df35s.git
cd project-f16df35s/
python -m venv ./.venv
source ./.venv/bin/activate
pip install -e .
exec "$SHELL"
