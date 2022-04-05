# Using a Redis Database to Read Meteorite Landings Data

A Flask container (using a python app) sends and reads data to and from a seperate Redis container.  

## Files
- ```app.py```: this is the python application that uses GET and POST fucntions that output information about the sample data 
- ```Dockerfile```: creates a an a docker image needed to containerize the application
- ```requirements.txt```: captures the required libraries and packages for the application in Dockerfile
#### sample data:
- ```ML_Data_Sample.json```: contains meteorite landings data (mass,location,classification, id number). it is sample data and only includes ids from 10001-10300 

### Get files

#### Clone the contents of this repository by entering what follows the $ into a terminal or SCP client:

```
$ git clone https://github.com/osvasali/homework05
```

(other methods for cloning a repository are described here [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))

#### Download the sample data by entering what follows the $ into a terminal or SCP client:

```
$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
```

## Building and Using Containers

The image may built by using the Dockerfile in this repository.
Replace `<username>` and `<tag>` with your own username and tag.
You may replace `<port number>` with 5027 Flask and 6427 for Redis or any other port not in use

#### Enter the following to pull and run a pre-containerized copy of the app from the docker file:

```
$ docker pull osvasali/ml_data_sample:hw5
```
####  Enter the following to build and run new image:

```
$ docker build -t <username>/<name it here>:<tag> .
```

####  run Redis container - Enter the following:

```
$ docker run -d -p <port number>:6379 -v $(pwd)/data:/data:rw --name=<container name>-redis redis:6 --save 1 1
```

- The output will be the container name

####  run Flask container - Enter the following:

```
$ docker run --name " ml_data_sample" -d -p <port number>:5000 osvasali/ml-data-sample:hw5
```

- The output will be the container name

#### edit the IP Address in app.py - Enter the following:

1) get the container ID
```
$ docker ps -a | grep <redis container name>
```

2) enter the container ID here to get IP Address
```
$ docker inspect <redis container id> | grep IPAddress
```

3) use a text editor like emacs or vim to edit app.py
   - for emacs enter the following:
    ```
    $ emacs app.py
    ```
    Next in line that says `return redis.Redis(host='172.17.0.16', port=6379, db=0)` chnage `172.17.0.16` to the IP address found in step 2.
    
    Close and save:
    1. `ctrl X` or `cmd X`
    2. `ctrl S` or `cmd S`
    3. `ctrl Z` or `cmd Z`


