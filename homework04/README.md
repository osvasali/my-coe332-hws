# Creating a Summary of Meteorite Data:

The python script `ml_data_analysis.py` uses the data from `Meteorite_Landings.json` to summarize the Mars meteorite data collected from an autonomous rover mission. The file `test_ml_data_analysis.py` tests the `ml_data_analysis.py` program to make sure that the program is working as expected. These files are containerized so it is reproducable in different computing environments.   

## Files

Clone the contents of this repository by entering what follows the $ into a terminal or SCP client:

```
$ git clone https://github.com/osvasali/my-coe332-hws/homework04
```

(other methods for cloning a repository are described here [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))

### Dictionaries with Meteorite Data

`Meteorite_Landings.json` contains a dictionary of dictionaries that each contain multiple key values. Here is and example of a dictionary in the within `Meteorite_Landings.json` file:

```
{
          "meteorite_landings": [
              {
                "name": "Belin",
                "id": "10029",
                "recclass": "H5",
                "mass (g)": "32000",
                "reclat": "42.53333",
                "reclong": "-85.88333",
                "GeoLocation": "(42.53333, -85.88333)"
              },
               ...    
```

The name of the main dictionary is `"meteorite_landings"`. The keys `recclass` , `mass (g)`, `reclat`, and `reclong` contain values that will be summarised by the script `ml_data_analysis.py`. These keys characterize the class the meteorite belongs to, its mass in grams, and its latitude and longitude coordinates.

### Reading Dictionaries to Summarize Meteorite Data

The python script `ml_data_analysis.py` has functions named `compute_average_mass`, `check_hemisphere`, and `count_classes` that use the data in `Meteorite_Landings.json` to output legible decriptions of the contents withing the dictionary. 

 1) `compute_average_mass` 
    - adds all the masses in the dictionaries and then divides the total by the amount of masses found. 
 2) `check_hemisphere` 
    - outputs a string that says `'Northern'` if the latitude is positive and a string that says `'Eastern'` if the longitude is positive; it also outputs `'Southern'` or             `'Western'` if the respective values are negative. These strings are combined to report what quadrant of Mars the meteorites were found on.
 3) `count_classes` 
    - iterates through a list of dictionaries, and pulls out the value associated with a given key. Counts the number of times each value occurs in the list of dictionaries           and returns the result.



### Testing the Python Script for Efficacy

`test_ml_data_analysis.py` contains a series of unit tests that take account of possible issues that may arise when running the python script `ml_data_analysis.py`. Each function in the python script has at least five tests in `test_ml_data_analysis.py`. The tests account for incompatibilities between the JSON file and the python script like inconsistent naming convetions or unnexpected values.

## Pull and use Existing Image from Dockerhub

Using a terminal (or SCP client), do the following:
1. Pull the image from Docker Hub
      - `docker pull osvasali/ml_data_analysis:hw04`
2. Run the image using the sample data provided
      - `docker run --rm -it -v $PWD:/code osvasali/ml_data_analysis:hw04 /bin/bash`
      - this will place you "inside" the container. Run using `ml_data_analysis.py /code/Meteorite_Landings.json` 
      - the terminal should look something like this:
      ```
          [username@isp02 homework04]$ docker run --rm -it -v $PWD:/code osvasali/ml_data_analysis:hw04 /bin/bash
          [root@7f7180bc742b /]# ml_data_analysis.py /code/Meteorite_Landings.json
          Summary data following meteorite analysis:

          The average mass of 30 meteors:
           83857.3

           Hemisphere summary data:
          There were  21  meteors found in the  Northern & Eastern quadrant
          There were  6  meteors found in the  Northern & Western quadrant
          There were  0  meteors found in the  Southern & Eastern quadrant
          There were  3  meteors found in the  Southern & Western quadrant

           Class summary data:
          The class L5 was found 1 times
          The class H6 was found 1 times
          The class EH4 was found 2 times
          The class Acapulcoite was found 1 times
          The class L6 was found 6 times
          ...
      ```
      
## Build an Image

Using a terminal (or SCP client), do the following:
  1. Build the image using the pulled Dockerfile
      - make sure you are in the directory pulled from this github repository
      - `docker build -t <username>/ml_data_analysis:<tag> .` (remember to replace with your own username and tag. the <> are not necessary)
  2. Use provided data or download new input data
      - The main program in the `ml_data_analysis.py` script runs functions assuming the dictionary is named `"meteorite_landings"` and the keys `recclass` , `mass (g)`, `reclat`, and `reclong` are inside the sub-dictionaries in the JSON file. 
      - If you would like to use your own input data, it should be in a JSON file in the format shown below:
        ```
        {
          "meteorite_landings": [
            {
              "recclass": "EH4",
              "mass (g)": "321",
              "reclat": "58.775",
              "reclong": "12.08333",
            },
            {
              "recclass": "Acapulcoite",
              "mass (g)": "450",
              "reclat": "56.18333",
              "reclong": "-10.23333",
            },
            ...
        ```
       - The Docker file must be altered so that the containter copies a new JSON file and contains the following line (remember to replace with a filename of your choosing. the <> are not essential). 
       ```
        COPY Meteorite_Landings.json /code/<filename>.json
       ```
       - The main function inputs must be altered to read from JSON files that contain similar data but use different naming conventions.
        
## Run the Containerized Code Against Data 
### Running against the sample data inside the container
   1. Using a terminal (or SCP client), do the following:
      - `docker run --rm -v $PWD:/data osvasali/ml_data_analysis:hw04 ml_data_analysis.py /data/Meteorite_Landings.json`
      - the the following will be the output:
      ```
      Summary data following meteorite analysis:

      The average mass of 30 meteors:
       83857.3

       Hemisphere summary data:
      There were  21  meteors found in the  Northern & Eastern quadrant
      There were  6  meteors found in the  Northern & Western quadrant
      There were  0  meteors found in the  Southern & Eastern quadrant
      There were  3  meteors found in the  Southern & Western quadrant

       Class summary data:
      The class L5 was found 1 times
      The class H6 was found 1 times
      The class EH4 was found 2 times
      The class Acapulcoite was found 1 times
      The class L6 was found 6 times
      ...
      ```
      
### Run against user-provided data found on the internet
2. Using a terminal (or SCP client), do the following:
      - Dowload data using this command `curl https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json --output <filename>.json` (remember to replace with a filename of your choosing. the <> are not essential)
      - Note: the above link may be replaced with one of your choosing as long as it meets the conditions described in the "Build an Image" section of this `README.md` document.
      - `docker run --rm -v $PWD:/data osvasali/ml_data_analysis:hw04 ml_data_analysis.py /data/<filename>.json` (remember to replace with the filename chosen in previous step)
      -  The output should look like the the output in section 1, but may have different values.

## Run The Containerized Test Suite With pytest
  - Using a terminal (or SCP client), enter the following:
      - `docker run --rm -it osvasali/ml_data_analysis:hw04 /bin/bash` to start an interactive shell inside the container
      - Enter `pytest /code/` in the terminal. This will be the output if the tests ran successfully:
        ```
          ================================================================= test session starts ==================================================================
          platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
          rootdir: /code
          collected 6 items

          code/test_ml_data_analysis.py ......                                                                                                             [100%]

          ================================================================== 6 passed in 0.04s ===================================================================
        ```

## Interpreting the Output

- Here is an example output that summarizes the Meteorite data collected from a Mars rover mission:

```
Summary data following meteorite analysis:

The average mass of 30 meteors:
 83857.3

 Hemisphere summary data:
There were  21  meteors found in the  Northern & Eastern quadrant
There were  6  meteors found in the  Northern & Western quadrant
There were  0  meteors found in the  Southern & Eastern quadrant
There were  3  meteors found in the  Southern & Western quadrant

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

 - The average mass of the meteors is shown in grams.
 - In the subsequent section, the amount of meteors found in each quadrant is displayed.
 - The last section lists all the classes found and the amount of meteors in each class. 
