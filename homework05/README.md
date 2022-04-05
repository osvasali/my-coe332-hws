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
    
    Next in line that says `return redis.Redis(host='172.17.0.16', port=6379, db=0)` change `172.17.0.16` to the IP address found in step 2.
    
    Close and save:
    1. `ctrl X` or `cmd X`
    2. `ctrl S` or `cmd S`
    3. `ctrl Z` or `cmd Z`

4) enter the following to make sure app.py is exported to Flask

```
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run -p <port number>
```
Then follow the instructions in the next section using a different tab. You may leave this tab open to see logging messages. Example:

```
[2022-04-05 09:31:31,573 isp02.tacc.utexas.edu] _internal.py:_log:225 - INFO: 127.0.0.1 - - [05/Apr/2022 09:31:31] "GET /data?start=299 HTTP/1.1" 200 -
[2022-04-05 09:35:14,210 isp02.tacc.utexas.edu] app.py:data:26 - INFO: 🔎 GETTING DATA...
[2022-04-05 09:35:14,210 isp02.tacc.utexas.edu] app.py:data:40 - ERROR: START INDEX IS NOT AN INTEGER 😡
127.0.0.1 - - [05/Apr/2022 09:35:14] "GET /data?start=jfkc HTTP/1.1" 200 -
[2022-04-05 09:35:14,210 isp02.tacc.utexas.edu] _internal.py:_log:225 - INFO: 127.0.0.1 - - [05/Apr/2022 09:35:14] "GET /data?start=jfkc HTTP/1.1" 200 -
 * Detected change in '/home/osvasali/my-coe332-hws/homework05/app.py', reloading
[2022-04-05 09:36:53,317 isp02.tacc.utexas.edu] _internal.py:_log:225 - INFO:  * Detected change in '/home/osvasali/my-coe332-hws/homework05/app.py', reloading
[2022-04-05 09:36:53,374 isp02.tacc.utexas.edu] _internal.py:_log:225 - INFO:  * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 768-430-896
[2022-04-05 09:37:01,714 isp02.tacc.utexas.edu] app.py:data:18 - INFO: 💾 LOADING DATA...
```

## Interpret the Results
Examples for POST, GET, and GET with start query:
  1. Load data into Redis container with `$ curl localhost:<flask port number>/data -X POST`:
      - The ouput will be a confirmation message or error saying the file is missing
      
      ```
      [username@isp02 homework05]$ curl localhost:5027/data -X POST
       ✅ Loading Complete ✅
      ```
      - possible error message when ```ML_Data_Sample.json``` is not in the directory:

      ```
      ...
          with open('_ML_Data_Sample.json' , 'r') as f:
      FileNotFoundError: [Errno 2] No such file or directory: 'ML_Data_Sample.json'

      -->
      ```


  2. Print ```ML_Data_Sample.json``` to terminal with `$ curl localhost:<port number>/data -X GET`
      - excerpt below marked with breaks using `...`.
      - the output will be the contents of the json file
      
      ```
      [username@isp02 homework05]$ curl localhost:5027/data -X GET
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
        ...
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
      ```

  3.  Implement an optional start query parameter that takes an integer and returns the Meteorite Landing data starting at that index using 
  
      `$ localhost:<your flask port number>/data?start=<starting index> -X GET`. Replace `<starting index>` with a number from 1 to 300
      
      - output a shortened version of data set
      - includes the start index at the end of output message
      
      ```
      [username@isp02 homework05]$ curl localhost:5027/data?start=299 -X GET
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
      
      - possible error message when user enters a number less than 1 or a string:

      ```
      [osvasali@isp02 homework05]$ curl localhost:5027/data?start=jfkc -X GET
      ❌ Could not convert data to an integer. ❌
      ```
