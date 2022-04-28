# International Space Station Tracker - Behavioral Diagram

![](https://github.com/osvasali/my-coe332-hws/blob/main/homework07/trackingAppFlowchart.png)

## Application Description

This application outputs data for the position and velocity of the International Space Station (ISS), as well as the places around the world where the ISS was sighted. The application does this by collecting data from XML files and making them easier for a person to read the country, region, city, time, position in cartesian coordinates, units of velocity, magnitude of velocity, and other details associated with the ISS for a particular sighting or epoch.

The repository for the application may be found [here](https://github.com/osvasali/ISS-Tracking-Application-Using-Flask).

## Key

The following is a key for the behavioral diagram:

- ```Green Oval```: Marks the start or the end of the application
- ```Burnt Orange Rectangle```: Decribes what is outputted in a terminal to the user
- ```Orange Circle```: Marks the connection point between different behaviors
- ```Teal Rhombus```: Describes the type of HTTP request made by the user
- ```Yellow Diamond```: Contains a condition that asks what type of input was made

![](https://github.com/osvasali/my-coe332-hws/blob/main/homework07/Key.png)

## Behaviors

##### How to Interact with the Application

The user interacts with the application by replacing  `<port number>` with their port number and
`<route>` with the one of the routes shown in the help output. These will be the inputs (HTTP requests) shown as a teal rhombus in the behavioral diagram.

```
$ curl localhost:<port number>/<route>
```

### Input Help Route - ```Teal Rhombus```

The user of the application begins by making an HTTP request that explains how to load the data and output it.

#### `/help` - shows list of routes

```
$ curl localhost:<port number>/help
```

### Output Instructions - ```Orange Circle```

Output below explains how to download the data and lists of the routes:

```
 
FIRST LOAD DATA USING THE FOLLOWING PATH: /load -X POST

    
    IF THERE ARE ERRORS ENTER THE FOLLOWING COMMANDS THEN LOAD THE DATA ONCE MORE
    
    $ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml
    $ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA06.xml

    Navigation:

    Use the following routes to access the data:
      1.  /epochs
          #lists all epochs
      2.  /epochs/<epoch>
          #data for specific epoch
      3.  /countries
          #lists all countries
      4.  /countries/<country>
          #data for specific country
      5.  /countries/<country>/regions
          #lists all regions
      6.  /countries/<country>/regions/<region>
          #data for specific region
      7.  /countries/<country>/regions/<region>/cities
          #lists all cities
      8. /countries/<country>/regions/<region>/cities/<cities>
          #data for specific city

```

### Input Load Route - ```Teal Rhombus```

The user then inputs the HTTP request to load the data to the application.

#### `/load` - loads data from XML files

```
$ curl localhost:<port number>/load -X POST
```

### Did the Data Load? - ```Yellow Diamond```

If the data loaded without errors, then the user will make an HTTP request to output data. If there were errors in loading, then the user will input the help route again.

### Input Data Route - ```Teal Rhombus```

The user will make an HTTP request as shown in the [How to Interact with the Application](#how-to-interact-with-the-application) section.

The possible requests are shown in this [output](#output-instructions).

### Epoch Data? - ```Yellow Diamond```

If it is epoch data go [here](#epochs).

If it is country data go [here](#countries).


### <span id="epochs"></span>All Epochs? - ```Yellow Diamond```

### <span id="countries"></span>All Countries? - ```Yellow Diamond```

### Specific Country? - ```Yellow Diamond```

### All Regions? - ```Yellow Diamond```

### Specific Region? - ```Yellow Diamond```

### All Cities? - ```Yellow Diamond```

### Output Every Epoch's Data - ```Orange Circle```
### Output Data for an Epoch - ```Orange Circle```
### Output Every Country's Data - ```Orange Circle```
### Output Data for a Country - ```Orange Circle```
### Output Every Region's Data - ```Orange Circle```
### Output Data for a Region - ```Orange Circle```
### Output Every City's Data - ```Orange Circle```
### Output Data for a City - ```Orange Circle```

<span id="a"></span>
[here](#epochs)

*
*
*
*
*
*

*
*
*
*
*
*
*
*






