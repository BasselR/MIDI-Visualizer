import json
import sys
import globalVars

def jsonInit():
    #fileName = sys.argv[1]
    fileName = 'Resources/bassTest.json'

    #Loads entire MIDI file as one big JSON Object into a python dictionary 
    with open(fileName) as json_file:
        song = json.load(json_file)

    #noteList = []

    #Locates the "track" which contains the song's notes and makes a noteList from that array of notes
    for track in song["tracks"]:
        if track["notes"]:
            globalVars.noteList = track["notes"]   #Assign the first non-empty "note" list as the noteList

def jsonPrint():
    print("Parsing {} with {} notes\n".format(fileName, len(globalVars.noteList)))

    for i in globalVars.noteList: 
        print(i)
