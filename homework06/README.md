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


#### Clone the contents of this repository by entering what follows the $ into a terminal or SCP client:

```
$ git clone https://github.com/osvasali/homework05
```

(other methods for cloning a repository are described here [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))

## Kubernetes Deployment
login to kubernetes cluster:

```
$ ssh <tacc_username>@coe332-k8s.tacc.cloud
```

Once you've logged onto your Kubernetes cluster, use the following command to apply a configuration for each of the 5 ```yml``` files:
``` bash
[user@f5p ~]$ kubectl apply -f <file name>
```

example:

``` bash
[user@f5p ~]$ kubectl apply -f osvasali-test-redis-service.yml
```

To see all the ```pvc```, ```pods```, ```deployments```, and ```services``` that have been aplied and check their NAMEs and statuses enter this:

``` bash
[user@f5p ~]$ kubectl get all -o wide
```
Find the IP address of your Flask service with:
``` bash
[user@f5p ~]$ kubectl get services
NAME                             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE     SELECTOR
service/hw6-flask-test-service   ClusterIP   10.104.235.83    <none>        5000/TCP   47m     app=hw6-test-flask
```
Now execute a command in your Python debug pod with:
``` bash
[user@f5p ~]$ kubectl exec -it <python-debug-NAME> /bin/bash
root@py-debug-deployment-5dfcf7bdd9-pfrdv:/#
```
You're now in the pod. You can access the Flask API with the service's unique IP address and the port ```5000``` by curling the route ```/data```. First load the data with the ```-X POST``` verb, then you can retrieve it without explicitly writing the ```GET``` verb.
``` bash
root@py-debug-deployment-5dfcf7bdd9-pfrdv:/# curl 10.104.235.83:5000/data -X POST
✅ Loading Complete ✅
root@py-debug-deployment-5dfcf7bdd9-pfrdv:/# curl 10.104.235.83:5000/data?start=299 -X GET
      [
       {
        "name": "Jennifer",
        "id": "10299",
        "recclass": "L5",
        "mass (g)": "539",
        "reclat": "-84.0579",
        "reclong": "69.9994",
        "GeoLocation": "(-84.0579, 69.9994)"
       },
       {
        "name": "Christina",
        "id": "10300",
        "recclass": "H5",
        "mass (g)": "4291",
        "reclat": "-38.1533",
        "reclong": "-46.7127",
        "GeoLocation": "(-38.1533, -46.7127)"
       }
      ]

      🤓 DATA AT START INDEX 299
```
