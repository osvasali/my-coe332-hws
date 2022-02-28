# Creating a Summary of Meteorite Data:

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
The main program for this python script runs these functions assuming that the keys `recclass` , `mass (g)`, `reclat`, and `reclong` are inside the `.json` file and the main function must be altered to read from `.json` files that contain similar data but use different naming conventions.

### Testing the Python Script for Efficacy

`test_ml_data_analysis.py` contains a series of unit tests that tak account of possible issues that may arise when running the python script `ml_data_analysis.py`. Each function in the python script has at least five tests in `test_ml_data_analysis.py`. The tests account for incompatibilities between the `.json` file and the python script like inconsistent naming convetions or unnexpected values.

## How to Run From a Container

Using a terminal (or SCP client), do the following:

1. Pull the image from Docker Hub
      - `docker pull osvasali/ml_data_analysis:hw04`
  2. Run the image using the sample data provided
      - `docker run --rm osvasali/ml_data_analysis:hw04 ml_data_analysis.py /data/Meteorite_Landings.json`
      - Once you run the command above, you should see the following output: 

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
