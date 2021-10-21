import requests
import pathlib
import time
def main(inp,start,end,filename):
    APIStations = set()
    j = -180
    
    while j < 180: # each step takes about 0.4 seconds
        print("pinging API")
        curr = time.perf_counter()
        try:
            url = "https://www.ncei.noaa.gov/access/services/search/v1/data?dataset=global-hourly&bbox=90,"+str(j)+",-90,"+str(j+1) 
            r = requests.get(url)
            data = r.json()
        except:
            print(url)
        nextCurr = time.perf_counter()
        print(nextCurr - curr)
        print("processing API")
        curr = time.perf_counter()
        if data["count"] != 0: #check to see if count is = 1000
            for station in data["stations"]["buckets"]:
                APIStations.add(station["key"])
        if len(data["stations"]["buckets"]) == 1000:
            print("stations => 1000, stations might be missed")
        j+=1
        nextCurr = time.perf_counter()
        print(nextCurr - curr)
    print(len(APIStations))
    print("API Done")
    file = open(str(pathlib.Path(__file__).parent.resolve()) + "/api-isd-stations.txt","w")
    count = 0
    for station in APIStations:
        print("api request")
        curr = time.perf_counter()
        try:
            url = "https://www.ncei.noaa.gov/access/services/search/v1/data?dataset=global-hourly&stations="+station+"&includeStationName=1"
            r = requests.get(url)
            data = r.json()
        except:
            pass
        nextCurr = time.perf_counter()
        print(nextCurr - curr)
        print("processing api request")
        curr = time.perf_counter()
        code = station
        name = ""
        lat = ""
        lon = ""
        start = ""
        end = ""
        try:
            name = data["results"][0]["stations"][0]["name"]
        except:
            pass
        try:
            lat = data["bounds"]["bottomRight"]["lat"]
            lon = data["bounds"]["bottomRight"]["lon"]
        except:
            pass
        try:
            start = data["startDate"]
            end = data["endDate"]
        except:
            pass
        count += 1
        if count % 1000 == 0:
            print(count)
        file.write(str(code) + "\t" + str(name) + "\t" + str(lat) + "\t" + str(lon) + "\t" + str(start) + "\t" + str(end) + "\n")
        nextCurr = time.perf_counter()
        print(nextCurr - curr)
    file.close()
main(0,0,0,0)
