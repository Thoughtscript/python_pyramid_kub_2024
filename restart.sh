#!/usr/bin/env bash

minikube stop && minikube delete && docker system prune -a --volumes -f