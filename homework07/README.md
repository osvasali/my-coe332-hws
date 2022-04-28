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

### <span id="instructions"></span>Output Instructions - ```Orange Circle```

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

The possible requests are shown in this [output](#instructions).

### Epoch Data? - ```Yellow Diamond```

The user may make a request to either output the position and velocity data of the ISS (epochs) or output the places the ISS was sighted (countries).

If the user requested epoch data go [here](#epochs).
If the user requested country data go [here](#countries).

### <span id="epochs"></span>All Epochs? - ```Yellow Diamond```

The user may output data for every epoch or data for a specific epoch. Below are example outputs for both:

#### Output Every Epoch's Data - ```Orange Circle```

```
...
2022-057T10:12:56.869Z
2022-057T10:16:56.869Z
2022-057T10:20:56.869Z
2022-057T10:24:56.869Z
2022-057T10:28:56.869Z
2022-057T10:32:56.869Z
2022-057T10:36:56.869Z
2022-057T10:40:56.869Z
2022-057T10:44:56.869Z
2022-057T10:48:56.869Z
2022-057T10:52:56.869Z
2022-057T10:56:56.869Z
2022-057T11:00:56.869Z
2022-057T11:04:56.869Z
2022-057T11:08:56.869Z
2022-057T11:12:56.869Z
2022-057T11:16:56.869Z
2022-057T11:20:56.869Z
2022-057T11:24:56.869Z
2022-057T11:28:56.869Z
2022-057T11:32:56.869Z
2022-057T11:36:56.869Z
2022-057T11:40:56.869Z
2022-057T11:44:56.869Z
2022-057T11:48:56.869Z
2022-057T11:52:56.869Z
2022-057T11:56:56.869Z
2022-057T12:00:00.000Z
...
```

#### Output Data for an Epoch - ```Orange Circle```

```
{
  "X": {
    "#text": "-4945.2048874258298",
    "@units": "km"
  },
  "X_DOT": {
    "#text": "1.19203952554952",
    "@units": "km/s"
  },
  "Y": {
    "#text": "-3625.9704508659102",
    "@units": "km"
  },
  "Y_DOT": {
    "#text": "-5.67286420497775",
    "@units": "km/s"
  },
  "Z": {
    "#text": "-2944.7433487186099",
    "@units": "km"
  },
  "Z_DOT": {
    "#text": "4.99593211898374",
    "@units": "km/s"
  }
}
```

### <span id="countries"></span>All Countries? - ```Yellow Diamond```

The user may output data for every country or data for an area with a smaller scope. The output below is shown to the user if the answer to the condition is a yes:

#### Output Every Country's Data - ```Orange Circle```

### <span id="country"></span>Specific Country? - ```Yellow Diamond```

The user may output data for a specific country or data for an area with a smaller scope. The output below is shown to the user if the answer to the condition is a yes:

#### Output Data for a Country - ```Orange Circle```

### <span id="regions"></span>All Regions? - ```Yellow Diamond```

The user may output data for every region or data for an area with a smaller scope. The output below is shown to the user if the answer to the condition is a yes:

#### Output Every Region's Data - ```Orange Circle```

### <span id="region"></span>Specific Region? - ```Yellow Diamond```

The user may output data for a specific region or data for an area with a smaller scope. The output below is shown to the user if the answer to the condition is a yes:

#### Output Data for a Region - ```Orange Circle```

### <span id="cities"></span>All Cities? - ```Yellow Diamond```

The user may output data for every region or data for a speccific city. Below are example outputs for both:


#### Output Every City's Data - ```Orange Circle```
#### Output Data for a City - ```Orange Circle```
