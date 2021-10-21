from os import path
import pathlib
#done
def main(latlong,start,end,filename):
   file = open(str(pathlib.Path(__file__).parent.resolve()) + "/api-isd-stations.txt","r")
   out = open(str(pathlib.Path(__file__).parent.resolve()) + "/" + filename,"w")
   stations = file.readlines()
   if len(stations) == 0:
      return "station list empty"
   latlong = latlong.split(",")
   if len(latlong) != 4:
      return "incorrect amount of inputs"
   minLat = float(latlong[0])
   minLong = float(latlong[1])
   maxLat = float(latlong[2])
   maxLong = float(latlong[3])
   #print(minLat,minLong,maxLat,maxLong)
   for line in stations:
      tabbedLine = line.split("\t")
      lat = 0
      long = 0
      try:
         lat = float(tabbedLine[2])
         long = float(tabbedLine[3])
      except:
         pass
      #print(lat,long)
      if lat>=minLat and lat <= maxLat and long >= minLong and long <= maxLong:
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
        
