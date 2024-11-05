# python_pyramid_kub_2024

[![](https://img.shields.io/badge/Python-3.13-yellow.svg)](https://www.python.org/downloads/) 
[![](https://img.shields.io/badge/Pyramid-2.0-red.svg)](https://trypyramid.com/) 
[![](https://img.shields.io/badge/Docker-blue.svg)](https://www.docker.com/) 
[![](https://img.shields.io/badge/Kubernetes-purple.svg)](https://kubernetes.io/) 
[![](https://img.shields.io/badge/Postgres-16.2-lightblue.svg)](https://hub.docker.com/_/postgres)

Very simple exploration of Python + Pyramid.

## Setup and Use

1. For **Docker Compose**: 
   * Execute `bash run-dc.sh`
2. For Kubernetes:
   * Execute `bash run-k.sh`
   * Will generate and display a dynamic **IP Address**.
     * You will need to update the **Postman Collection Variables** accordingly to test.
     * This is apparently required for `minikube` [local testing](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/).

Note that **Pyramid** API Requests may not appear in the browser as rendered text (w/out a satisfactory Renderer). 
    * Check the Developer Console for the correct Response.
    * Postman is supplied to simplify basic testing.

## Helpful Commands

`bash`:

```bash
# Remove every Docker image, dangling volume, minikube, etc. and startover
## use only if you know what you're doing!
bash restart.sh 
```

`docker`:

```bash
# Display running Docker Containers
docker stats ## verify that the Docker builds are contained within the Kubernetes environment
```

`kubectl`:

```bash
kubectl get services
kubectl get pods
kubectl describe services/python-pyramid-postgres
```

`minikube`:

```bash
minikube dashboard ## Display minikube pods and namespaces
```

> Check out [run-k.sh](./run-k.sh) for other relevant Kubernetes commands!

## Views

**Serving File Content Dynamically**

> Using the resolve DNS hostname from `docker-compose`:

1. Simple HTML View: http://localhost:8000/index.html
   * https://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/static_assets/serving-files.html
2. Direct Static File Serve: http://localhost:8000/static/test.html

## Resources and Links

1. https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/
2. https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/
3. https://kubernetes.io/docs/tutorials/services/connect-applications-service/
4. https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/
5. https://github.com/Pylons/pyramid/blob/main/docs/quick_tutorial/static_assets/tutorial/home.pt
6. https://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/static_assets/serving-files.html
7. https://github.com/testdrivenio/flask-vue-kubernetes/tree/master
8. https://www.digitalocean.com/community/tutorials/how-to-deploy-postgres-to-kubernetes-cluster