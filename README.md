# Overview

Create simple kubernetes minikube service that says hello.

```
# start minikube environment
minikube start

kubectl create -f hello-pod.yml
kubectl create -f hello-svc.yml
kubectl create -f hello-rc.yml

# get minikube to tell us what url the service is running on and then curl it
curl $(minikube service web --url)
```

Minikube hosts the service on one of it's Node machines.  In this case, there
is only one and a random port (in a given range) is picked for the hello
service.
