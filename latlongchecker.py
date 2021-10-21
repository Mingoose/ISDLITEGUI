#this folder creates a txt file with a list of stations that have the same lat long
# script could be improved for better output readability:
#	list all stations with same lat long next to each other
#	exists and doesnt exist calculations arent great
import pathlib
def main(USAFWBAN,start,end,filename):
    listOfStations = open(str(pathlib.Path(__file__).parent.resolve()) + "/api-isd-stations.txt","r")
    stations = {}
    dups = {}
    file = open(str(pathlib.Path(__file__).parent.resolve()) + "/" + filename, "w")
    count = 0
    nullcount = 0
    lines = listOfStations.readlines()
    if len(lines) == 0:
        return "station list empty"
    for station in lines:
        data = station.split("\t")
        name = data[1]
        latlong = data[2]+data[3]
        if latlong in stations.keys():
            if latlong not in dups.keys():
                dups[latlong] = [latlong, name, stations[latlong]]
                count += 2
            else:
                dups[latlong].append(name)
                count += 1
            if (stations[latlong] == "XM20" or latlong == "0.00.0"):
                nullcount += 1
        else:
            stations[latlong] = name
    file.write("garbage duplicate lat longs: " + str(nullcount) + "\n")
    file.write("total stations with duplicate: " + str(count) + "\n")
    for key in dups.keys():
        file.write(",".join(dups[key])+"\n")
    file.close()
    return "done"
