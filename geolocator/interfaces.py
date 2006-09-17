# WARNING! THESE ARE NOT UP TO DATE AND ARE NOT USED BY THE PACKAGE

"""
 Data provider interfaces.

  - IP should be given as a 'xxx.xxx.xxx.xxx' string

  - location is returned as a (lat,lon) tuple, where lat & lon are (degrees,minutes,seconds) tuples

  - city is identified by name, whereas a country is identified by country code

"""

class IGeoIPLocationProvider:
   "provides location by IP"

   def getLocationByIP(ip):
      "get location"


class ICityIPProvider:
   "provides city IP data"

   def getCityByIP(ip):
      ""

class ICountryIPProvider:
   "provides country IP data"

   def getCountryByIP(ip):
      ""

class IGeoLocationProvider:
   "provides city & country location data"

   def getLocationByCity(cityname):
      ""

   def getLocationByCountry(countrycode):
      ""


"""
 Interfaces for localized names providers

"""

class ICityNameProvider:
   "get city name"

   def getCityName(cityname, language):
      ""

class ICountryNameProvider:
   "get country name"

   def getCountryName(countrycode,language):
      ""