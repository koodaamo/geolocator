"""

 To use the data providers, thus getting access to the location and/or geoip
 data, data providers have to be selected.

 In the long run, we want to make provider selection at least semi-automatic.
 For now, however, the providers have to be manually configured here.

 Since we don't yet have a windows binary to distribute with the library,
 we default to DummyProvider.

 If you're on unix, use the MaxMindCountryIpProvider.
 If you've purchased the MaxMind GeoIP City database,
 use MaxMindCityIpProvider.

"""

from providers import DummyProvider
from providers import MaxMindCountryDataProvider
from providers import MaxMindCityDataProvider

MAXMINDLOCATIONS = (
   "./data",
   "/usr/share/GeoIP",
   "/usr/local/share/GeoIP"
)

# default provider
DEFAULTPROVIDER = DummyProvider