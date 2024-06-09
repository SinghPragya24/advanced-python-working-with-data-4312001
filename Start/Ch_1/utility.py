# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates the use of the any, all, and sum functions
import json
import os

# these utility functions don't have callbacks like min or max,
# but we can use a generator for more fine control

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print("Are there any quake reports that were felt by more than 25,000 people?",any(quake["properties"]["felt"] is not None and quake["properties"]["felt"] > 25000
          for quake in data["features"]))

print("How many quakes were felt by more than 500 people?",sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 500
         for quake in data["features"]))

print("How many quakes had a magnitude of 6 or larger?",sum(quake["properties"]["mag"] is not None and quake["properties"]["mag"] >= 6
          for quake in data["features"]))
