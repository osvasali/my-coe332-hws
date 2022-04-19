from flask import Flask, jsonify, request
from typing import List
import json, redis, logging, socket

format_str = f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format_str)
app = Flask(__name__)
ML_data = {}

@app.route('/data', methods=['POST','GET'])
def data() -> str:
    '''
    POST: Loads data into Redis container. Returns: string with confirmation message
    GET: Prints either complete or indexed meteorite landings data. Returns: string with data from json file
    '''
    rd = redis.Redis(host='10.110.198.217', port=6379, db=0)
    if request.method == 'POST':
        logging.info("\U0001F4BE LOADING DATA...")
        global ML_data
        with open('ML_Data_Sample.json' , 'r') as f:
            ML_data =  json.load(f)
        for d in ML_data['meteorite_landings']:
            rd.set(d['id'],json.dumps(d))
        return ' \U00002705 Loading Complete \U00002705\n'
    elif request.method == 'GET':
        logging.info("\U0001F50E GETTING DATA...")
        indexed = []
        start = request.args.get('start')
        try:
            if start is None:
                for i in range (10001, 10301, 1):
                    indexed.append(json.loads(rd.get(i)))
                return json.dumps(indexed, indent=2) + '\n'
            elif type(start) == str:
                index = int(start) + 10000
                for i in range(index, 10301, 1):
                    indexed.append(json.loads(rd.get(i)))
                return json.dumps(indexed, indent=1) + f'\n\n\U0001F913 DATA AT START INDEX {start}\n'
        except (TypeError, ValueError, NameError):
            logging.error('START INDEX IS NOT AN INTEGER \U0001F621')
            return '\U0000274C Could not convert data to an integer. \U0000274C\n\a'
        return "ROUTE NOT FOUND\n\a"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
