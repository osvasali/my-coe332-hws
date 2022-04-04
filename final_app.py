from flask import Flask, jsonify, request
from typing import List
import json, redis, logging, socket

format_str = f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format_str)
app = Flask(__name__)
ML_data = {}

@app.route('/data', methods=['POST','GET'])
def data():
    '''

    '''
    rd = redis.Redis(host='172.17.0.2', port=6379, db=0)
    if request.method == 'POST':
        logging.info("LOADING DATA...")
        global ML_data
        with open('ML_Data_Sample.json' , 'r') as f:
            ML_data =  json.load(f)
        for d in ML_data['meteorite_landings']:
            rd.set(d['id'],json.dumps(d))
        return ' -- Loading Complete --\n'
    elif request.method == 'GET':
        logging.info("GETTING DATA...")
        indexed = []
        start = request.args.get('start')
        try:
            if start is None:
                for i in range (10001, 10301, 1):
                    indexed.append(json.loads(rd.get(i)))
                return json.dumps(indexed, indent=2) + '\n' ##error here
            elif type(start) == str:
                index = int(start) + 10000
                for i in range(index, 10301, 1):
                    indexed.append(json.loads(rd.get(i)))
                return json.dumps(indexed, indent=1) + '\n'
        except (TypeError, ValueError, NameError):
            logging.error('START INDEX IS NOT AN INTEGER')
            return 'Could not convert data to an integer.\n\a'
        return "ROUTE NOT FOUND\n\a"
