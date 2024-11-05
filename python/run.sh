#!/usr/bin/env bash

sleep 5 && uvicorn main:app --workers 2 --host 0.0.0.0 & #--ssl-keyfile=./auth/key.pem --ssl-certfile=./auth/certificate.pem &

wait