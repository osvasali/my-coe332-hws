# Summary of Meteorite Data Analysis:

The python program `ml_data_analysis.py` uses the data from `Meteorite_Landings.json` to summarize the Mars meteorite data collected from an autonomous rover mission. The file `test_ml_data_analysis.py` tests the `ml_data_analysis.py` program to make sure that the program is working as expected. These files are containerized so it is reproducable in different computing environments.   

## Scripts
The analysis script was improved in its output structure, were the information is described and explained. The unit test are simple 
sanity checks that make sure the code works correctly with different data samples. Lastly is the Docker file which contains the commands
normally inputted into the command line, but it executes them within this file as a shortcut.
## Instructions
#### 1)
Pulling information from another person docker profile is essential to sharing information, in this situation we will be pulling my Docker
conatiner. This will allow access the scripts and data I have and it will allow for the input of your own data as well, computing the script and
testing itself.
```BASH
$ docker pull jbolivar101/ml_data_analysis:hw04
```

#### 2)
In order to build an image we must first have a Dockerfile containing `FROM`, `RUN`,`COPY`, and `ENV PATH` commands appropriate to the
files you want to upload. In order to build the image we must do the following,
```BASH
$ docker build -t jbolivar101/ml_data_analysis:hw04 .
```
It should output:
```BASH
Sending build context to Docker daemon  28.16kB
Step 1/9 : FROM centos:7.9.2009
 ---> eeb6ee3f44bd
Step 2/9 : RUN yum update -y &&     yum install -y python3
 ---> Using cache
 ---> 33d6c421a020
Step 3/9 : RUN pip3 install pytest==7.0.0
 ---> Using cache
 ---> 7016c3ab98b6
Step 4/9 : COPY ml_data_analysis.py /code/ml_data_analysis.py
 ---> Using cache
 ---> a1e59cbde25c
Step 5/9 : COPY test_ml_data_analysis.py /code/test_ml_data_analysis.py
 ---> Using cache
 ---> fdfcb79687a9
Step 6/9 : COPY Meteorite_Landings.json /code/Metorite_Landings.json
 ---> Using cache
 ---> f54de5af9084
Step 7/9 : RUN chmod +rx /code/ml_data_analysis.py
 ---> Using cache
 ---> 837a8b0a8550
Step 8/9 : RUN chmod +rx /code/test_ml_data_analysis.py
 ---> Using cache
 ---> 75bb62e1ab9f
Step 9/9 : ENV PATH "/code:$PATH"
 ---> Using cache
 ---> a8b717bde52c
Successfully built a8b717bde52c
Successfully tagged jbolivar101/ml_data_analysis:hw04
``` 

#### 3)
Running a container requires access to the profile so one must be logged in, then input the run command below, and finally call upon
the script and data file within the container. It should look like:
```BASH
$ docker login

$ docker run --rm -it -v $PWD:/data jbolivar101/ml_data_analysis:hw04 /bin/bash

$ ml_data_analysis.py /code/Meteorite_Landings.json
```
It should output:
```BASH
The average mass of 30 meteors:
83857.3

Hemisphere summary data:
There were  21  meteors found in the Northern and Eastern quadrant
There were  6  meteors found in the Northern and Western quadrant
There were  0  meteors found in the Southern and Eastern quadrant
There were  3  meteors found in the Southern and Western quadrant

Class summary data:
The class L5 was found 1 times
The class H6 was found 1 times
The class EH4 was found 2 times
The class Acapulcoite was found 1 times
The class L6 was found 6 times
The class LL3-6 was found 1 times
The class H5 was found 3 times
The class L was found 2 times
The class Diogenite-pm was found 1 times
The class Stone-uncl was found 1 times
The class H4 was found 2 times
The class H was found 1 times
The class Iron-IVA was found 1 times
The class CR2-an was found 1 times
The class LL5 was found 2 times
The class CI1 was found 1 times
The class L/LL4 was found 1 times
The class Eucrite-mmict was found 1 times
The class CV3 was found 1 times
```

#### 4)
To use local data in this example we must first download it(it can be any link you want). This can also be run and use files locally,
while running scripts from the container. Similar to the last step we must be logged in, then execute the following command that is all in one:
```BASH
$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json

$ docker run --rm -v $PWD:/data jbolivar101/ml_data_analysis:hw04 ml_data_analysis.py /data/ML_Data_Sample.json
```
This example runs the container, then inputs the command and calls upon data that we just downloaded from the local folder it should output:
```BASH
The average mass of 30 meteors:
5081.37

Hemisphere summary data:
There were  71  meteors found in the Northern and Eastern quadrant
There were  86  meteors found in the Northern and Western quadrant
There were  74  meteors found in the Southern and Eastern quadrant
There were  69  meteors found in the Southern and Western quadrant

Class summary data:
The class H4 was found 22 times
The class L6 was found 18 times
The class CI1 was found 29 times
The class L5 was found 36 times
The class LL3-6 was found 27 times
The class LL5 was found 39 times
The class CV3 was found 24 times
The class CR2-an was found 26 times
The class H6 was found 31 times
The class EH4 was found 22 times
The class H5 was found 26 times
```

#### 5)
To run the unit test from the container we must run and call it from within the container, which is then accessed within the `code` folder:
```BASH
$ docker run --rm -it -v $PWD:/data jbolivar101/ml_data_analysis:hw04 /bin/bash

$ cd code/

$ pytest 
```
It should output:
```BASH
===================================================================================================== test session starts ======================================================================================================
platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
rootdir: /home/jbolivar/Spring2022coe/my_coe332_hws/homework04
collected 6 items

test_ml_data_analysis.py ......                                                                                                                                                                                          [100%]

====================================================================================================== 6 passed in 0.03s =======================================================================================================
```

## INPUTS
The scripts I have made work as long as the data provided fits within the structure of the following data set, this is because the names of the
key data points are specific to the analysis. 
```BASH
"meteorite_landings": [
    {
      "name": "Gerald",
      "id": "10001",
      "recclass": "H4",
      "mass (g)": "5754",
      "reclat": "-75.6691",
      "reclong": "60.6936",
      "GeoLocation": "(-75.6691, 60.6936)"
    }
]
```
As long as the data provided holds this information it will be capable of calculating the average mass, hemisphere, and class. In case you do not
have your own data to input, the container already has a sample and you can aquire one with
 ` wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json`
