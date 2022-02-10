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
