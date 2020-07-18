# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

# Creating the class called City
class City():
  def __init__(self, name, lat, lon):
    self.name = name 
    self.lat = lat
    self.lon = lon

  # making a __str method to be able to 
  # print out object
  def __str__(self):
    return f"{self.name}, {self.lat}, {self.lon}"

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

# going to get the path to the cities file
import os
import csv


def cityreader(cities=[]):

  # put the path in the method so that it wouldn't 
  # mess up the test file hopefully
  csv_path = os.path.join(os.path.dirname(__file__), "cities.csv")

  theLat = None
  theLon = None
  # reading in the file
  with open(csv_path) as csv_file:
    my_reader = csv.DictReader(csv_file)
    for i, row in enumerate(my_reader):
      if i == 0:
        pass
        #print((f'Column names are {", ".join(row)}'))
      # building the city then appending to the cities list

      # ensuring the the types of values are floats
      theLat = row["lat"]
      theLon = row["lng"]
      if not isinstance(theLat, float):
         theLat = float(theLat)
      if not isinstance(theLon, float):
        theLon = float(theLon)
      cities.append(City(name=row["city"], lat=theLat, lon=theLon))


  # TODO Implement the functionality to read from the 'cities.csv' file
  # Ensure that the lat and lon valuse are all floats
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    
  return cities

cityreader(cities)


    
# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

# Getting the values from the user
fList = None
sList = None
while True:
  first = input("Enter lat1,lon1: ")
  # spliting
  fList = first.split()
  try :
    fList[0] = float(flist[0])
    flist[1] = float(fList[1])
    break
  except:
    print("Make sure that you enter numbers!\n")
  
  while True:
    second = input("Enter lat2,lon2: ")
    # splitting
    sList = second.split()
    try:
      sList[0] = float(sList[0])
      sList[1] = float(sList[1])
      break
    except:
      print("Make sure that you enter numbers!\n")
  

# Will be using the lon as the x val and lat as the y val

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []
  # finding the lowest longitude min = a if a < b else b 
  leftSide  = lon1 if lon1 < lon2 else lon2
  rigtSide = lon1 if lon1 > lon2 else lon2
  top = lat1 if lat1 > lat2 else lat2
  bottom = lat1 if lat1 < lat2 else lat2

  for city in cities:
    if city.lon > leftSide and city.lon < rigtSide and city.lat < top and city.lat > bottom:
      within.append(city)

  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within
