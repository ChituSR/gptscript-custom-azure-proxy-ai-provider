#!/usr/bin/env bash

source ./.venv/Scripts/activate
uvicorn main_proxy:app --reload
