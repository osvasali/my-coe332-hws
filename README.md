# Homework Directory for COE 332 – Software Engineering & Design
Homework Assignments for COE 332 will be posted here. Each homework assignment has it's own directory with the naming convention `homework0X`. Inside each directory, there is a README.md, Python scripts, and the files needed for the Python script to function.

## Folders
- `homework01` Intro to Python: Testing Basic Scripts
  - contains two solutions for the two exercises from the python refresher guide.
- `homework02` Mars Rover Mission Report
  - The python programs generateSites.py and readSites.py are used in tandem to to model a rover mission on Mars where the objective is to collect meteorite samples on Syrtis Major. This model may be used to assess the missionviability of a rover that moves at 10 kilometers per hour. 
- `homework03` Mars Water Quality Assesment
  - After collecting meteorite samples, the next phase of the Mars Rover Mission is to asses the quality of water used to analize the samples. The turbidity of the water will be assesed in the following program to determine if the water is safe and usable or if the Mars Laboratory should go on boil water notice. 
- `homework04` Creating a Summary of Meteorite Data
  - The python script `ml_data_analysis.py` uses the data from `Meteorite_Landings.json` to summarize the Mars meteorite data collected from an autonomous rover mission. The file `test_ml_data_analysis.py` tests the `ml_data_analysis.py` program to make sure that the program is working as expected. These files are containerized so it is reproducable in different computing environments.   
- `homework05` Using a Redis Database to Read Meteorite Landings Data
  - A Flask container (using a python app) sends and reads data to and from a seperate Redis container.
- `homework06` Using Kubernetes to Read Meteorite Landings Data
  - Kubernetes (k8s) are used to deploy a Flask API that uses Redis to create a test environment for the application. The application reads meteorite landing data from a json file and oututs the result to the user.
- `homework07` International Space Station Tracker - Behavioral Diagram
  - the behavioral diagram is for a midterm found [here](https://github.com/osvasali/ISS-Tracking-Application-Using-Flask).
