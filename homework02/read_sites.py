import json
import math

with open('meteorite_data.json', 'r') as f:
    data = json.load(f)

mars_radius = 3398.5 #km
#great-circle distance algorithm using the radius of Mars
def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def compute_lat_long(sites, latitude, longitude, composition):
    #Robot's initial latitude and longitude
    robot_lat = 16.0
    robot_long = 82.0
    #initial time
    time = 0

    for i in range(len(sites)): #iterates through dictionary of dictionaries
        distance_traveled = calc_gcd(robot_lat, robot_long, float(sites[i][latitude]), float(sites[i][longitude]))
        robot_lat = float(sites[i][latitude])
        robot_long = float(sites[i][longitude])
        travel_duration = round( distance_traveled/10 , 2) #divided by ten because robot moves 10km/hr

        #time it takes to sample different meteorites
        if(str(sites[i][composition]) == "stony"):
            sample_time = 1
        elif(str(sites[i][composition]) == "iron"):
            sample_time = 2
        else:
            sample_time = 3

        time = sample_time + travel_duration + time #current total time
        print("leg = ", i+1, ", time to travel = ",travel_duration, " hrs, time to sample = ", sample_time, " hrs")
    print("====================================")
    print("number of legs = 5, total elapsed time = ", time, " hrs")
    return(None)

print(compute_lat_long(data['sites'], 'latitude', 'longitude', 'composition'))
