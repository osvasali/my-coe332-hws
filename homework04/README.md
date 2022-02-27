# Mars Rover Mission Report

The python programs generateSites.py and readSites.py are used in tandem to to model a rover mission on Mars where the objective is to collect meteorite samples on Syrtis Major. This model may be used to assess the missionviability of a rover that moves at 10 kilometers per hour.

## Generating Meteorite Sites on Syrtis Major

The python program generateSites.py creates a dictionary with one key then appends five sub-dictonaries in that key. Each sub-dictionary contains four keys: the site identification number, the site latitude, the site longitude, and the type of meteorite on site. The values of these four keys are randomly generated and then daved into a json file named meteorite_data.json.

## Reading meteorite_data.json to Make a Mission Report

The python program readSites.py uses the data from meteorite_data.json to calculate the distance (kilometers) the rover traveled by using the great-circle distance algorithm. The total mission duration is calculated by measuring the time it took for the rover to take a sample, the distance the rover traveled for each leg of the mission, dividing each distance by the rover speed of 10 kilometers per hour, then adding the time elasped for each leg. All of this data is outputed to the console.

## File Usage

Using a terminal (or SCP client), first run generateSites.py by entering the following in the command line (do not type the dollar sign).

```bash
$ python3 generateSites.py
```
Nothing will appear in the command line, but doing this will create a new file named meteorite_data.json that contains randomized values for the meteorite composition and location.

Now run readSites.py by entering the following in the command line (do not type the dollar sign).

```bash
$ python3 readSites.py
```
This will output a summary of what the rover was doing at each leg of the mission. The time it took to travel to the meteorite and the time it took to take a sample will be displayed for each leg; the total time for the mission and number of legs will be displayed below that. 

# Mars Water Quality Assesment
After collecting meteorite samples, the next phase of the Mars Rover Mission is to asses the quality of water used to analize the samples. The turbidity of the water will be assesed in the following program to determine if the water is safe and usable or if the Mars Laboratory should go on boil water notice.



## Python Script Descriptions:
This project contains three files: `spaceTurbidity.py` , `testSpaceTurbidity.py` , `turbidity_data.json`.
- `spaceTurbidity.py` contains three functions. The first function calculates the turbidity. The second function calculates the minimum decay time and determines whether the turbidity is below the threshold for safe use or not. Lastly, the main function provides structure and the ability to pull contents and dictionaries directly from the JSON file.
- `testSpaceTurbidity.py` contains unit tests which ensure that the code and functions are working as expected. If minor changes are made to the code, these tests can be ran from this file in order to make sure that nothing is broken. Lastly, these unit tests test for edge cases.
- `turbidity_data.json` contains the water quality data that will be used for analysis and Python operations in this project.

## Downloading Turbidity Data Set:
1) Using a terminal (or SCP client), enter the following in the command line (do not type the dollar sign) to download `turbidity_data.json` in the same directory as `spaceTurbidity.py` and `testSpaceTurbidity.py` :

```bash
$ wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
```

## Instructions to Run Code:
1. Run `spaceTurbidity.py` by typing the following in the terminal:
```bash
$ `python3 spaceTurbidity.py`
```  
2. Run `testSpaceTurbidity.py` by typing the following in the terminal: 
```bash
$ `python3 testSpaceTurbidity.py`
``` 

## Results:
Example output from `spaceTurbidity.py`:

```bash

Average turbidity based on most recent five measurements = 0.6849400000000001 NTU
WARNING: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 0 hours

``` 

The code outputs three key pieces of information:
- Average Turbidity
- Whether the Turbidity is above or below the safety threshold
- Minimum Decay Time required to return below safety threshold

Example output from `testSpaceTurbidity.py`:

```bash
================================================= test session starts ==================================================
platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
rootdir: /home/osvasali/coe332/HW/03
collected 4 items

testSpaceTurbidity.py ....                                                                                     [100%]

================================================== 4 passed in 0.01s ===================================================
``` 

The code outputs the results from the unit tests. It demonstartes the tests that have either passed or failed and the time it took to compute these tests.


