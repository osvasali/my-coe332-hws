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
