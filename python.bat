@echo off
REM
python gunicorn -b :8080 -c gunicorn.conf.py main:app