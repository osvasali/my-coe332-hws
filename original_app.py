from flask import Flask, jsonify, request
from typing import List
import json, logging, socket, sys, redis

format_str = '%(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format_str)
app = Flask(__name__)

ML_Data = {}
error_string = "ERROR - DATA NOT FOUND - Use /help for more information\n"

def get_redis_client():
    return redis.Redis(host='172.17.0.2', port=<6427>, db=0)

@app.route('/data', methods=['POST'])
def data_post() -> str:
    """
    Loads the Meteorite Landings data into a global variable.
    Returns: string confirming if data was loaded successfully or not
    """
    try:
        logging.info("Loading Meteorite Landings Data.")
        global ML_Data
        with open('ML_Data_Sample.json' , 'r') as f:
             ML_Data =  JSON.parse(f.read())
    except FileNotFoundError as e:
        logging.error(e)
        return 'METEORITE LANDINGS DATA FILE NOT FOUND\n'

    return f'Data has been loaded\n'

@app.route('/data', methods=['GET'])
def data_get() -> List[str]:
    """
    Reads the data in the global variable ML_Data to create a ---.
    Returns: a list --  as string variables. An error if data is not found.
    """
    try:
        logging.info("Getting list from Meteorite Landings data...")
        mlandings = []
        for i in range(len(ML_Data['name']['is']['recclass']['mass']['reclat']['reclong']['GeoLocation'])):
            mlandings.append(ML_Data['name']['is']['recclass']['mass']['reclat']['reclong']['GeoLocation'])
        return mlandings
    except Exception as e:
        logging.error(e)
        return error_string



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
