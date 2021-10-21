import PySimpleGUI as sg
import searchByUSAF as sbUSAF
import searchByUSAFWBAN as sbUSAFWBAN
import searchByStationName as sbsn
import searchByLatLong as sbll
import StationChecker as sc
import latlongchecker as llc
import usafChecker as uc
import downloader as d
import APIToList as APItl
from datetime import datetime

	

sg.theme("light green 6")
scale = 3
scriptsData = {"search by USAF":("USAF","Returns Separate info for all USAFWBAN combinations. Reports lat/lon, station name, begin, end",sbUSAF,"USAF") ,
           "search by USAFWBAN":("USAFWBAN", "Do Not include hyphen in input. Reports lat/lon, station name, begin, end",sbUSAFWBAN,"USAFWBAN") ,
           "search by station name":("Station Name", "Supports use of *. Returns all data of all stations found", sbsn,"Name"),
           "search by lat/long":("Lat/Long", "Seach for locations within a box. Format inputs as comma separated values: minlat,minlong,maxlat,maxlong. Reports lat/long, elev, ctry, st, station name, begin, end", sbll,"LatLon"),
           "check if file exists for given USAFWBAN":("USAFWBAN","Returns list of years that exist and list of years that don't exist", sc,"Exists"),
           "download by USAFWBAN":("USAFWBAN","Downloads all files that exist for given station",d, "ISDLiteData"),
           "find all stations that have a USAF number that matches another station":("No Input","Finds all stations that have another station with a matching USAF number.",uc,"matchingUSAF"),
           "find all stations that have a lat long that matches another station":("No Input","Finds all stations that have another station with the same lat long.",llc,"matchingLatLon"),
            "update station list":("No Input","Update the list of stations. Will take around 3 hours", APItl,"StationList")   }
currentScript = ""
scripts = ["search by USAF","search by USAFWBAN","search by station name",
           "search by lat/long","check if file exists for given USAFWBAN","download by USAFWBAN",
           "find all stations that have a USAF number that matches another station","find all stations that have a lat long that matches another station","update station list"]
# Define the window's contents
col1 = [[sg.Text("Scripts")],[sg.Listbox(values = scripts, size = (20*scale,12*scale), key = "LIST", enable_events = True)]]
col2 = [[sg.Text("input",size = (10*scale,1*scale), key = "inputText"),sg.Text("start year",size = (10*scale,1*scale),),sg.Text("end year",size = (10*scale,1*scale))],
        [sg.Input(size = (10*scale,1*scale), key = "input"),sg.Input(size = (10*scale,1*scale),key = "start year"),sg.Input(size = (10*scale,1*scale),key = "end year"),sg.Button("Clear")],
        [sg.Text("Instructions",size = (20*scale,5*scale),key = "INSTRUCTIONS")],
        [sg.Input(size = (20*scale,5*scale), key = "filename"),sg.Text("filename",size = (10*scale,1*scale))],
        [sg.Text("",(10*scale,1*scale),key = "status")],
        [sg.Button("Run"),sg.Button('Quit')]]
layout1 = [[sg.Column(col1),
          sg.Column(col2)]]

# Create the window
window = sg.Window("Windographer Data Downloader Helper", layout1)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == "Clear":
        window["input"].update("")
        window["start year"].update("")
        window["end year"].update("")
        continue
    print(values["LIST"])
    if values["LIST"][0] != None:
        currentScript = values["LIST"][0]
        window["status"].update("")
        window["INSTRUCTIONS"].update(scriptsData[currentScript][1])
        window["inputText"].update(scriptsData[currentScript][0])
        now = datetime.now()
        dateTime = now.strftime("%d-%m-%Y-%H:%M:%S:")
        window["filename"].update(dateTime+scriptsData[currentScript][3]+".txt")
        if currentScript == "update station list":
            window["filename"].update("No Input")
    if currentScript != "" and event == "Run":
        window["status"].update("running")
        message = scriptsData[currentScript][2].main(values["input"],values["start year"],values["end year"],values["filename"])
        window["status"].update(message)
        window["input"].update("")
        window["start year"].update("")
        window["end year"].update("")
        window["filename"].update(dateTime+scriptsData[currentScript][3]+".txt")

# Finish up by removing from the screen
window.close()
