#!/usr/bin/env bash

source ./.venv/Script/activate
uvicorn main_proxy:app --reload
