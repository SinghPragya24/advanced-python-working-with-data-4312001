# Example file for Advanced Python: Working With Data by Joe Marini
# sorting data with the sorted() and sort() functions

import json


numbers = [42, 54, 19, 17, 23, 31, 16, 4]
names = ["Jeff", "Bill", "Addie", "Stephanie", "Zach", "Lukas", "Joe", "Stacy"]

# the sorted() function can be used to return a new list with sorted data
# result_sorted = sorted(numbers)
# print("Sorted ->", result_sorted)

# alternately, you can use the list object's sort() method, which sorts the list in-place
# numbers.sort(reverse=True)
# print(numbers)

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)

data["features"].sort(key=getmag, reverse=True)
for i in range(0,10):
    print(data["features"][i]["properties"]["place"])
    