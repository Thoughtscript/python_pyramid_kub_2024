#!/usr/bin/env bash

sleep 15 && uvicorn main:app --workers 2 --host 0.0.0.0 &

sleep 25 && cd tests && pytest functional_tests.py &

wait