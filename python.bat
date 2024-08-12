@echo off
REM
gunicorn -b :$PORT -c gunicorn.conf.py main:app
