import pathlib
#done
def main(usafwban,start,end,filename):
    file = open(str(pathlib.Path(__file__).parent.resolve()) + "/api-isd-stations.txt","r")
    out = open(str(pathlib.Path(__file__).parent.resolve()) + "/" + filename,"w")
    stations = file.readlines()
    if len(stations) == 0:
        return "station list empty"
    for line in stations:
        tabbedLine = line.split("\t")
        if tabbedLine[0] == usafwban:
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

