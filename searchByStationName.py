from os import path
import pathlib
#done
def main(stationName,start,end,filename):
    file = open(str(pathlib.Path(__file__).parent.resolve()) + "/api-isd-stations.txt","r")
    out = open(str(pathlib.Path(__file__).parent.resolve()) + "/" + filename,"w")
    stations = file.readlines()
    if len(stations) == 0:
        return "station list empty"
    if len(stationName) == 0:
        return "empty station name"
    for line in stations:
        tabbedLine = line.split("\t")
        found = False
        if stationName[0] == "*" and stationName[-1] == "*":
            found = stationName.upper()[1:-1] in tabbedLine[1]
        elif stationName[0] == "*":
            found = (tabbedLine[1][-(len(stationName)-1):] == stationName.upper()[1:])
        elif stationName[-1] == "*":
            found = (tabbedLine[1][:len(stationName)-1] == stationName.upper()[:-1])
        else:
            found = (tabbedLine[1] == stationName.upper())
        if found:
            stationStart = tabbedLine[4][:4]
            stationEnd = tabbedLine[5][:4]
            try:
                if start == "" and end == "":
                    out.write(line)
                elif (int(start) >= int(stationStart) and int(start) <= int(stationEnd)) or (int(end) >= int(stationStart) and int(end) <= int(stationEnd)):
                    out.write(line)
            except:
                return "invalid start end"
    file.close()
    out.close()
    return "done"

