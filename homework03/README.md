# Mars Water Quality Assesment

## Overview:
After collecting meteorite samples, the next phase of the Mars Rover Mission is to asses the quality of water used to analize the samples. The turbidity of the water will be assesed in the following program to determine if the water is safe and usable or if the Mars Laboratory should go on boil water notice.

## Directions to Download Water Quality Data Set:
1) Click the link: https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
2) Log into TACC Computer
3) Move to the COE 332 Directory
4) Create a homework03 folder by using the mkdir command.
5) Use this command: `wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json` in order to download the file into the homework directory.

## Python Script Descriptions:
This project contains three files: `analyze_water.py` , `test_analyze_water.py` , `turbidity_data.json`.
- analyze_water.py contains three functions. The first function calculates the turbidity. The second function calculates the minimum decay time and determines whether the turbidity is below the threshold for safe use or not. Lastly, the main function provides structure and the ability to pull contents and dictionaries directly from the JSON file.
- test_analyze_water.py contains unit tests which ensure that the code and functions are working as expected. If minor changes are made to the code, these tests can be ran from this file in order to make sure that nothing is broken. Lastly, these unit tests test for edge cases.
- turbidity_data.json contains the water quality data that will be used for analysis and Python operations in this project.

## Instructions to Run Code:
1. Run analyze_water.py in the command line. You can do this by typing `python3 analyze_water.py` 
2. Run test_analyze_water.py in the command line. You can do this by typing `python3 analyze_water.py`

## Results:
The code outputs three key pieces of information:
- Average Turbidity
- Whether the Turbidity is above or below the safety threshold
- Minimum Decay Time required to return below safety threshold
