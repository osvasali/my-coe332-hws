# Using Kubernetes to Read Meteorite Landings Data
Kubernetes (k8s) are used to deploy a Flask API that uses Redis to create a test environment for the application. The application reads meteorite landing data from a json file and oututs the result to the user.
- ```Dockerfile```: creates a an a docker image needed to containerize the application.
- ```app.py```: this is the python application that uses GET and POST fucntions that output information about the sample data
 yaml files used to make pods with Redis and Flask:
- ```osvasali-test-redis-deployment.yml```: Creates a deployment for the Redis database
- ```osvasali-test-redis-volume.yml```: Stores the data written to it from the deployment file independently from the pods
- ```osvasali-test-redis-service.yml```: Provides a persistent IP address to use that is able to interact with Redis
- ```osvasali-test-flask-deployment.yml```: Creates a deployment (with two replicas) for the Flask API
- ```osvasali-test-flask-service.yml```: Provides a persistent IP address to use that is able to interact with the API


## Clone the contents of this repository by entering what follows the $ into a terminal or SCP client:

```
$ git clone https://github.com/osvasali/homework05
```

(other methods for cloning a repository are described here [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))

## Running in Kubernetes
Once you've logged onto your Kubernetes cluster, ensure you have a Python debug pod to use for running the API. To apply a configuration of all ```yml``` files use the following command for each of the 5 ```yml``` files:
``` bash
[user@f5p ~]$ kubectl apply -f <file name>
```
This creates various Kubernetes resources for each file of types ```pvc```, ```pods```, ```deployments```, and ```services```. To check the IDs of your resources execute:
``` bash
[user@f5p ~]$ kubectl get all -o wide
```
Find the IP address of your Flask service with:
``` bash
[user@f5p ~]$ kubectl get services
NAME                   TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
s-shah-flask-service   ClusterIP   10.97.210.193    <none>        5000/TCP   3h6m
```
Now execute a command in your Python debug pod with:
``` bash
[user@f5p ~]$ kubectl exec -it <python-debug-ID> /bin/bash
root@py-debug-deployment-5dfcf7bdd9-pfrdv:/#
```
You're now in the pod. You can access the Flask API with the service's unique IP address and the port ```5000``` by ```curl```ing the route ```/data```. First load the data with the ```-X POST``` verb, then you can retrieve it without explicitly writing the ```GET``` verb.
``` bash
root@py-debug-deployment-5dfcf7bdd9-pfrdv:/# curl -X POST 10.97.210.193:5000/data
Data has been loaded!
root@py-debug-deployment-5dfcf7bdd9-pfrdv:/# curl 10.97.210.193:5000/data
[
 {
  "name": "Gerald",
  "id": "10001",
  "recclass": "H4",
  "mass (g)": "5754",
  "reclat": "-75.6691",
  "reclong": "60.6936",
  "GeoLocation": "(-75.6691, 60.6936)"
 },
 {
  "name": "Dominique",
  "id": "10002",
  "recclass": "L6",
  "mass (g)": "1701",
  "reclat": "-9.4378",
  "reclong": "49.5751",
  "GeoLocation": "(-9.4378, 49.5751)"
 },
 {
  "name": "Malinda",
  "id": "10003",
  "recclass": "CI1",
  "mass (g)": "3482",
  "reclat": "35.3692",
  "reclong": "61.4206",
  "GeoLocation": "(35.3692, 61.4206)"
 },
```
You are now free to load retrieve your data!
