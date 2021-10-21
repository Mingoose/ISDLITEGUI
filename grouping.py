import math
import pathlib
maxDist = 0.007

def main(inp,start,end,filename):
    filepath = str(pathlib.Path(__file__).parent.resolve()) + "/api-isd-stations.txt"
    listOfStations = open(filepath,"r")
    stationsList = listOfStations.readlines()
    coords = []
    stations = {}
    for station in stationsList:
        data = station.split("\t")
        if (float(data[2]) != 0 or float(data[3]) != 0):
            coords.append((data[0],float(data[2]),float(data[3])))
    for coord in coords:
        stations[coord[0]] = set()
        for coord2 in coords:
            if distance(coord[1],coord[2],coord2[1],coord2[2]):
                stations[coord[0]].add(coord2[0])
    print("done with init")
    cont = True
    count = 0
    while(cont):
        cont = False
        for station in stations.keys():
            start = len(stations[station])
            for s in stations[station]:
                stations[station].union(stations[s])
            if len(stations[station]) > start:
                cont = True
        count += 1
        print(count)
    groups = []
    longest = set()
    for station in stations.values():
        if len(station) > len(longest):
            longest = station
        groups.append(len(station))
    print(longest)
    
    return "done"
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2) < maxDist
main(0,0,0,0)
