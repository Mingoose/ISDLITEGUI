from ftplib import FTP
import pathlib
def main(USAFWBAN,start,end,filename):
    out = open(str(pathlib.Path(__file__).parent.resolve()) + "/" + filename,"w")
    stationCode = USAFWBAN
    try:
        ftp = FTP("ftp.ncei.noaa.gov")
        ftp.login()
        ftp.cwd("pub/data/noaa/isd-lite/")
        ftp.voidcmd('TYPE I')
    except:
        return "ftp failed"
    yearsAvailable = []
    yearsNotAvailable = []
    startYear = 0
    endYear = 0
    if start == "" and end == "":
        listOfStations = open(str(pathlib.Path(__file__).parent.resolve()) + "/api-isd-stations.txt","r")
        stations = listOfStations.readlines()
        if len(stations) == 0:
            return "station list empty"
        for i in range(len(stations)):
            data = stations[i].split("\t")
            if stationCode == data[0]:
                print("found")
                startYear = int(data[4][:4])
                endYear = int(data[5][:4])
                break;
    else:
        try:
            startYear = int(start)
            endyear = int(end)
        except:
            return "invalid start and end"
    print("starting ftp")
    while startYear <= endYear:
        try:
            ftp.cwd(str(startYear))
            ftp.size(stationCode[:6]+"-"+stationCode[6:]+"-"+str(startYear)+".gz")
            yearsAvailable.append(startYear)
        except:
            yearsNotAvailable.append(startYear)
        finally:
            ftp.cwd("../")
            startYear += 1
    ftp.quit()
    out.write("available:")
    out.write("\n")
    out.write(",".join(str(e) for e in yearsAvailable))
    out.write("\n")
    out.write("not available: ")
    out.write("\n")
    out.write(",".join(str(e) for e in yearsNotAvailable))
    out.close()
