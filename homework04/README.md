# Creating a Summary of Meteorite Data Analysis:

The python script `ml_data_analysis.py` uses the data from `Meteorite_Landings.json` to summarize the Mars meteorite data collected from an autonomous rover mission. The file `test_ml_data_analysis.py` tests the `ml_data_analysis.py` program to make sure that the program is working as expected. These files are containerized so it is reproducable in different computing environments.   

## Files

### Dictionaries with Meteorite Data

`Meteorite_Landings.json` contains a dictionary of dictionaries that each contain multiple key values. Here is and example of a dictionary in the within `Meteorite_Landings.json` file:

```

  {
      "name": "Belin",
      "id": "10029",
      "recclass": "H5",
      "mass (g)": "32000",
      "reclat": "42.53333",
      "reclong": "-85.88333",
      "GeoLocation": "(42.53333, -85.88333)"
    }
      
```

The keys `recclass` , `mass (g)`, `reclat`, and `reclong` contain values that will be summarised by the script `ml_data_analysis.py`. These keys characterize the class the meteorite belongs to, its mass in grams, and its latitude and longitude coordinates.

### Reading Dictionaries to Summarize Meteorite Data

The python script `ml_data_analysis.py` has functions named `compute_average_mass`, `check_hemisphere`, and `count_classes` that use the data in `Meteorite_Landings.json` to output legible decriptions of the contents withing the dictionary. 
#### 1) `compute_average_mass` adds all the masses in the dictionaries and then divides the total by the amount of masses found. 
#### 2) `check_hemisphere` outputs a string that says `'Northern'` if the latitude is positive and a string that says `'Eastern'` if the longitude is positive; it also outputs `'Southern'` or `'Western'` if the respective values are negative. These strings are combined to report what quadrant of Mars the meteorites were found on.
#### 3) `count_classes` iterates through a list of dictionaries, and pulls out the value associated with a given key. Counts the number of times each value occurs in the list of dictionaries and returns the result.


## Instructions
#### 1)
Pulling information from another person docker profile is essential to sharing information, in this situation we will be pulling my Docker
conatiner. This will allow access the scripts and data I have and it will allow for the input of your own data as well, computing the script and
testing itself.
```BASH
$ docker pull osvasali/ml_data_analysis:hw04
```

#### 2)
In order to build an image we must first have a Dockerfile containing `FROM`, `RUN`,`COPY`, and `ENV PATH` commands appropriate to the
files you want to upload. In order to build the image we must do the following,
```BASH
$ docker build -t osvasali/ml_data_analysis:hw04 .
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
 
 
 
 # The Joys of Containerization with Docker 

## Description
This project asked us to update the ml_data_analysis.py file, then to make a test file and put both of them into a conatiner on Docker. (As well as Meteorite_Landings.json)
The test and changes to ml_data_analysis are then run in Docker so that anyone may pull them and be able to run them from the container.

## Files
`ml_data_analysis.py` has been modified to be able to run without using the python3 command, and it also dislplays meteorite data such as average mass, location, and class in a much more simple and concise manner.
`test_ml_data_analysis.py` has been written to do unit testing for the functions in the previous file, all tests should pass if the code is working properly.
`Meteorite_Landings.json` contains all the the data pertaining to the meteorites that will be read and outputted when `ml_data_analysis.py` runs.

## How to Run the Code Using Docker
1)To get access to the files, use `docker pull ecolley3/ml_data_analysis:hw04`\
2)Next, run `docker build -t ecolley3/ml_data_analysis:hw04 .` to build your container. It should give an output of: 
```bash 
docker build -t ecolley3/ml_data_analysis:hw04 .
Sending build context to Docker daemon  36.86kB
Step 1/10 : FROM centos:7.9.2009
 ---> eeb6ee3f44bd
Step 2/10 : RUN yum update -y
 ---> Using cache
 ---> f412cd73b2c4
Step 3/10 : RUN yum install -y python3
 ---> Using cache
 ---> 9754c2b75a6c
Step 4/10 : RUN pip3 install pytest==7.0.0
 ---> Using cache
 ---> f78a483af15c
Step 5/10 : COPY ml_data_analysis.py /code/ml_data_analysis.py
 ---> Using cache
 ---> ac66c467f9f1
Step 6/10 : COPY test_ml_data_analysis.py /code/test_ml_data_analysis.py
 ---> Using cache
 ---> a6800a61d195
Step 7/10 : COPY Meteorite_Landings.json /code/Meteorite_Landings.json
 ---> Using cache
 ---> 30458c5b65b0
Step 8/10 : RUN chmod +rx /code/ml_data_analysis.py
 ---> Using cache
 ---> e9a7871711b5
Step 9/10 : RUN chmod +rx /code/test_ml_data_analysis.py
 ---> Using cache
 ---> 1511bcfe07c4
Step 10/10 : ENV PATH "/code:$PATH"
 ---> Using cache
 ---> 3385eeceaae1
Successfully built 3385eeceaae1
``` 
\
3) After this, use the `docker run --rm -it -v $PWD:/data ecolley3/ml_data_analysis:hw04 /bin/bash` To open the container, and then `cd /code` to open the directory with your files. Type `ml_data_analysis.py /data/Meteorite_Landings.json` to run the code using the data in the container, and the output should look like this:
``` bash 
Average mass of the meteors are:
 83857.3 grams


Summary of Hemisphere data:
There were  21  meteors found in the Northern and Eastern quadrant
There were  6  meteors found in the Northern and Western quadrant
There were  0  meteors found in the Southern and Eastern quadrant
There were  3  meteors found in the Southern and Western quadrant
Class summary data:
The L5 class was found 1 times
The H6 class was found 1 times
The EH4 class was found 2 times
The Acapulcoite class was found 1 times
The L6 class was found 6 times
The LL3-6 class was found 1 times
The H5 class was found 3 times
The L class was found 2 times
The Diogenite-pm class was found 1 times
The Stone-uncl class was found 1 times
The H4 class was found 2 times
The H class was found 1 times
The Iron-IVA class was found 1 times
The CR2-an class was found 1 times
The LL5 class was found 2 times
The CI1 class was found 1 times
The L/LL4 class was found 1 times
The Eucrite-mmict class was found 1 times
The CV3 class was found 1 times
```
\
4)To use your own data, use the `wget` command followed by whatever the link to the data is, and then use the command `ml_data_analysis.py /data/yourlink` to get an output similar to the last.\
5) After you have run the code, you may run the unit test by using the `pytest` command. While still in the `/code` directory, just type in `pytest` and the unit tests should run correctly.

## Input Data
If you plan to use wget to use your own input data, keep in my that it should be formatted in a certain way. The format gives the specific keys needed so that the code may analyze the data, and it looks as follows:
``` bash 
"meteorite_landings": [
    {
      "name": "Gerald",
      "id": "10001",
      "recclass": "H4",
      "mass (g)": "5754",
      "reclat": "-75.6691",
      "reclong": "60.6936",
      "GeoLocation": "(-75.6691, 60.6936)"
    },
```
The code uses these keywords to find the specific values it needs for each data point.
