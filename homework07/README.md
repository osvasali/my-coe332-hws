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

**How to Interact with the Application**

The user interacts with the application by replacing  `<your port number>` with their port number and
`<route>` with the one of the routes shown in the help output. These will be the inputs shown as a teal rhombus in the behavioral diagram.

```
$ curl localhost:<your port number>/<route>
```

### Input Help Route

The user of the application begins by making an HTTP request that explains how to load the data and output it.



#### `/help` - shows list of routes

```
$ curl localhost:<your port number>/help
```
 
Output below explains how to download the data and lists of the routes:

```
 
FIRST LOAD DATA USING THE FOLLOWING PATH: /load -X POST

    IF THERE ARE ERRORS LOAD THE DATA ONCE MORE


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
