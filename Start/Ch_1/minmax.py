# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# The min() function finds the minimum value
# print(f"Min value: {min(values)}")
# print(f"Min value: {min(strings)}")

# The max() function finds the maximum value
# print(f"Max value alphabetically: {max(values)}")
# print(f"Max value alphabetically: {max(strings)}")

# define a custom "key" function to extract a data field
# print(f"Min value per passed value: {min(strings, key=len)}")
# print(f"Max value per passed value: {max(strings, key=len)}")

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
print(data["metadata"]["title"])
print(len(data["features"]))

def magnitude(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if magnitude is None:
        magnitude = 0
    return float(magnitude)

# magnitude = magnitude(data)
# print(magnitude)

print(min(data["features"], key=magnitude))    
