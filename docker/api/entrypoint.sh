#!/bin/sh
# Script de inicialização para a API FastAPI

uvicorn main:app --host 0.0.0.0 --port 8000
