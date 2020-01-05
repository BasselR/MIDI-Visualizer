import json
import sys

fileName = sys.argv[1]

#Loads entire MIDI file as one big JSON Object into a python dictionary 
with open(fileName) as json_file:
    song = json.load(json_file)

noteList = []

#Locates the "track" which contains the song's notes and makes a noteList from that array of notes
for track in song["tracks"]:
    if track["notes"]:
        noteList = track["notes"]   #Assign the first non-empty "note" list as the noteList

print("Parsing {} with {} notes\n".format(fileName, len(noteList)))

for i in noteList: 
    print(i)
