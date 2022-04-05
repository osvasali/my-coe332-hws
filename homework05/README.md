# International Space Station Tracker - Positions and Sightings

This application outputs data for the position and velocity of the International Space Station (ISS), as well as the places around the world where the ISS was sighted.
The application does this by collecting data from XML files and making them easier for a person to read the country, region, city, time, 
position in cartesian coordinates, units of velocity, magnitude of velocity, and other details associated with the ISS for a particular sighting or epoch.   

## Files
- ```app.py```: this is the python application that uses GET and POST fucntions that output information about the ISS 
- ```Dockerfile```: creates a an a docker image needed to containerize the application
- ```requirements.txt```: captures the required libraries and packages for the application in Dockerfile
##### data sample:
-```ML_Data_Sample.json```: contains meteorite landings data (mass,location,classification, id number). it is sample data and only includes ids from 10001-10300 


### Source
The XML files above come from NASA's official website found [here](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq).

### Get files

##### Clone the contents of this repository by entering what follows the $ into a terminal or SCP client:

```
$ git clone https://github.com/osvasali/ISS-Tracker
```

(other methods for cloning a repository are described here [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))

#### XML file download
- Required data files: `ISS.OEM_J2K_EPH.xml` and `XMLsightingData_citiesUSA06.xml`
- Download the data [here](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq)
    - ```ISS.OEM_J2K_EPH.xml```: Titled "Public Distribution"
    - ```XMLsightingData_citiesUSA06.xml```: Titled "XMLsightingData_citiesUSA06"

##### Download the files by entering what follows the $ into a terminal or SCP client:

```
$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml
$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA06.xml
```

## Build Containerized App

The image may built by using either the Dockerfile or Makefile in this repository.
Replace `<username>` and `<tag>` with your own username and tag.
You may replace `<your port number>` with 5027 or another port not in use

### Using Makefile
#### Enter the following to pull and run a pre-containerized copy of the app

```
$ make pull
$ make run
```
####  Enter the following to build and run new image
```
$ NAME="<username>" make build
$ NAME="<username>" make run
```

### Using Dockerfile

#### Make requirements.txt - enter the following

```
$ emacs requirements.txt
```
Next type `Flask==2.0.3` then enter the following commands to save and exit the file.

1. `ctrl X` or `cmd X`
2. `ctrl S` or `cmd S`
3. `ctrl Z` or `cmd Z`

#### Enter the following to pull and run a pre-containerized copy of the app

```
$ docker pull osvasali/iss-tracker:midterm1
$ docker run --name "iss-tracker" -d -p <your port number>:5000 osvasali/iss-tracker:midterm1
```
####  Enter the following to build and run new image
```
$ docker build -t <username>/iss-tracker:<tag> .
$ docker run --name "iss-tracker" -d -p <your port number>:5000 osvasali/iss-tracker:midterm1
```
