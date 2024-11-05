#!/usr/bin/env bash

## Following: https://github.com/testdrivenio/flask-vue-kubernetes/tree/master
#-------------------------------------------------#
echo "Launching minikube ..."
#-------------------------------------------------#
minikube start && eval $(minikube docker-env)
cd kubernetes

#-------------------------------------------------#
echo "Deploying Postgres into minikube  ..."
#-------------------------------------------------#
kubectl apply -f postgres-secrets.yaml
kubectl apply -f postgres-volume.yaml,postgres-volume-claim.yaml
kubectl apply -f postgres-deployment.yaml,postgres-service.yaml

#-------------------------------------------------#
echo "Building Python image ..."
#-------------------------------------------------#
docker compose build 

#-------------------------------------------------#
echo "Deploying Python into minikube ..."
#-------------------------------------------------#
kubectl apply -f python-deployment.yaml,python-service.yaml

#-------------------------------------------------#
echo "Setting minikube host and ports ..."
#-------------------------------------------------#
# kubectl apply -f minikube-ingress.yaml
minikube service python-pyramid --url
