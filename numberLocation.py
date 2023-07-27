import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder
Key='91963ed5e711443ea51a45186cf9a247'
samNumber = phonenumbers.parse(number)
yourLocation =geocoder.description_for_number(samNumber,"en")
print(yourLocation)
##get service provider
from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en "))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query =str(yourLocation)
results =geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)
myMap = folium.Map(loction=[lat,lng],zoom_start = 9)
 
# Adding a Marker on the map to show the location name
folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)
 
# save map to html file to open it and see the actual location in map format
myMap.save("Location.html")