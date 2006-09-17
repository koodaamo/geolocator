import os

class CountryLocationProvider:
   ""

   FILENAME = "countrylocations.csv"

   def __init__(self):
      self.countrylocations = {}
      file = open(os.path.abspath(os.curdir) + os.sep + FILENAME)

      for l in file:
         countrycode, latitude, longitude = l.split(',')
         self.countrylocations[countrycode] = (latitude, longitude)

   def getLocationByCountry(self,countrycode):
      "get (latitude, longitude) tuple"
      return self.countrylocations[countrycode]

   def locateCountry(self, countrycode):
      "get (latitude, longitude) tuple"
      return self.getLocationByCountry(countrycode)