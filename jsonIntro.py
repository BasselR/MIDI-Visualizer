import json

with open('maybeShorter.json') as json_file:
    song = json.load(json_file)

myTracks = []

for track in song["tracks"]:
    if track["notes"]:
        myTracks = track["notes"]

for i in myTracks:
    print(i)