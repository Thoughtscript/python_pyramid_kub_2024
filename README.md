# python_pyramid_kub_2024

[![](https://img.shields.io/badge/Python-3.13-yellow.svg)](https://www.python.org/downloads/) 
[![](https://img.shields.io/badge/Pyramid-2.0-red.svg)](https://trypyramid.com/) 
[![](https://img.shields.io/badge/Docker-blue.svg)](https://www.docker.com/) 
[![](https://img.shields.io/badge/Kubernetes-purple.svg)](https://kubernetes.io/) 
[![](https://img.shields.io/badge/Postgres-16.2-lightblue.svg)](https://hub.docker.com/_/postgres)

Very simple exploration of Python + Pyramid.

## TODO Check List

- [x] Basic Pyramid App
- [x] Basic Pyramid APIs
- [x] Pyramid + Postgres
- [x] Docker-Compose and equivalents in Kubernetes
  - [X] Kubernetes build pipeline suitable for local builds and `minikube`
  - [X] Address this ancient question: https://stackoverflow.com/questions/74598540/how-to-mount-a-sql-file-in-a-init-container-in-order-to-bootstrap-postgres-datab
- [x] Add Tests
- [x] Add Better Integration Tests (that fully inject a view)
- [x] Learn more about Kubernetes in 2024 (`deployments`, `services`, `configMaps`, `volumes`, `volume-claims`, etc.)
- [x] Learn how to initialize Postgres with a script correctly (presumably through `containerInit`)
  - [x] I created a `configMap`, mounted, and executed a command in `deployment < containers`.
  - [x] Tested dropping the SQL script into `docker-entrypoint-initdb.d`.
- [x] Learn about ways to generate fixed hostnames and/or URLs (for `minikube` since it has some issues with this)
   - [x] `NodePorts`
   - [x] [Ingress](https://minikube.sigs.k8s.io/docs/handbook/addons/ingress-dns/#Windows)
- [x] Basic SSL
  - [x] Looks like `uvicorn`, TLS/SSl, and `asgiref` are presently incompatible: https://github.com/encode/uvicorn/issues/1118
  - [x] In Production, one would presumably deploy a Proxy w/ SSL out in front (still bad practice to not SSL encrypt everything - internal network sniffing)
  - [x] So is Waitress: https://github.com/Pylons/waitress/issues/287

## Setup and Use

1. For **Docker Compose**: 
   * Execute `bash run-dc.sh`
2. For Kubernetes:
   * Execute `bash run-k.sh`
   * Will generate and display a dynamic **IP Address**.
     * You may need to update the **Postman Collection Variables** accordingly to test.
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

# Make SSl certs for local testing
# cd python && bash ssl.sh
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
minikube dashboard # Display minikube pods and namespaces
## can find the Pod and Exec into the Container easily throug the supplied interface
```

> Check out [run-k.sh](./run-k.sh) for other relevant Kubernetes commands!

`pytest`

```bash
# Within the Python container
cd tests && pytest functional_tests.py
cd tests && pytest *.py 
## Note that "Deprecated call to `pkg_resources.declare_namespace('zope')" is a known Python-wide issue
```

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