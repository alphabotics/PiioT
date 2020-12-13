#!/bin/bash
source venv-py3.7/bin/activate
uvicorn FastAdmin.main:app --reload --port 8009
