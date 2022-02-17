import json
import math
from typing import List
import logging
import socket
format_str=f'%(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format_str)

def calculate_turbidity(listdicts: List[dict], calib: str, detect: str, i: int) -> float:

     a0 = float(listdicts[i][calib])
     I90 = float(listdicts[i][detect])

     T = a0 * I90
     return(T)

def calculate_time(T: float) -> bool:
     b = 0
     Ts = 1.0
     d = 0.02

     T0 = T
     b = math.log((1/T0),0.98)

     if (Ts > T0*((1-d)**b)):
         logging.info('Turbidity is below threshold for safe use')
         print(f'Minimum time required to return below a safe threshold = {b} hours')
     else:
         logging.warning('Turbidity is above threshold for safe use')
         print(f'Minimum time required to return below a safe threshold = 0 hours')

     return(0)

def main():
     with open('turbidity_data.json', 'r') as f:
         turb_data = json.load(f)
     T_list = 0
     x = 0
     for i in range(1,6):
         x = len(turb_data['turbidity_data'])- i

         T = calculate_turbidity(turb_data['turbidity_data'], 'calibration_constant', 'detector_current', x)
         T_list += T

     print(f'Average turbidity based on most recent five measurements = {T_list/5} NTU')
     Time = calculate_time(T)

if __name__ == '__main__':
     main()
