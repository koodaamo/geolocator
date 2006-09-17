"""
 Unit tests. Add more!
"""

import unittest

from geolocator import GeoLocator
from geolocator.providers import DummyProvider
from geolocator.providers import MaxMindCityIpProvider
from geolocator.providers import MaxMindCountryIpProvider


__all__ = ("GeolocatorTestSuite",)

class DummyLocatorCase(unittest.TestCase):
   "test the default"

class DummyCityIpProviderCase(unittest.TestCase):
   ""

class DummyLocationProviderCase(unittest.TestCase):
   ""

class DummyProviderCase(unittest.TestCase):

   def setUp(self):
      self.locator = GeoLocator()
      self.provider = MaxMindCityDataProvider()
      self.city = "Munkkiniemi"
      self.country = "FI"
      self.domain = "www.helsinki.fi"
      self.ip ="128.214.205.16"

   def tearDown(self):
      del self.locator

   def testCityForIp(self):
      self.assertRaises(self.locator.getCityForIp(self.ip), NotImplementedError)

   def testCityForDomain(self):
      self.assertRaises(self.locator.getCityForDomain(self.domain), NotImplementedError)

   def testCountryForIp(self):
      self.assertRaises(self.locator.getCountryForIp(self.ip), NotImplementedError)

   def testCountryForDomain(self):
      self.assertRaises(self.locator.getCountryForDomain(self.domain), NotImplementedError)

   def testCoordinatesForIp(self):
      self.assertRaises(self.locator.getCityForIp(self.ip), NotImplementedError)

   def testCoordinatesForDomain(self):
      self.assertRaises(self.locator.getCityForDomain(self.domain), NotImplementedError)

   #def testCoordinatesForCity(self.city):
   #   self.locator.getCityForIp("")

   # TODO: See countrycoordinates.csv and the provider and then add test
   #def testCoordinatesForCountry(self):
   #   self.locator.getLocationByCountry(self.country)

   # geoip city
   def testCityForIp(self):
      ""
      self.assertRaises(NotImplementedError)

class MaxMindCountryProviderCase:

   def testCountryForIp(self):
      self.assertRaises(self.locator.getCountryForIp(self.ip), NotImplementedError)

   def testCountryForDomain(self):
      self.assertRaises(self.locator.getCountryForDomain(self.domain), NotImplementedError)

GeolocatorTestSuite = unittest.makeSuite(DummyProviderCase,'test')


if __name__ == "__main__":
   unittest.main()
   raw_input("press any key to quit...")
