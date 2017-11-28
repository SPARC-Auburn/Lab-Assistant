import geocoder
from geopy.geocoders import Nominatim

g = geocoder.ip('me')
geolocator = Nominatim()
address = geocoder.reverse(g.latlng)
print(address.city + ", " + address.state + ", " + address.country)
