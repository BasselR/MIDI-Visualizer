import json

with open('c_scale.json') as json_file:
    song = json.load(json_file)

myTracks = []

for track in song["tracks"]:
    if track["notes"]:
        myTracks = track["notes"]

print(len(myTracks))

for i in myTracks:
    print(i)