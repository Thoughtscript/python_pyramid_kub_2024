#!/usr/bin/env bash

minikube start && eval $(minikube docker-env) && 
cd kubernetes && docker-compose up -d &&
kubectl apply -f kub-deployment.yaml,kub-service.yaml && 
sleep 15 && minikube service python-pyramid-postgres --url