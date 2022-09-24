import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def getColor(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")

fgVol = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el in zip(lat, lon, elev):   # because multiple list so use zip
    fgVol.add_child(folium.CircleMarker(location=[lt, ln], popup = str(el) + " m",
    fill_color = getColor(el), color = 'grey', fill_capacity = 0.7))

fgPop = folium.FeatureGroup(name = "Population")

fgPop.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgVol)
map.add_child(fgPop)
map.add_child(folium.LayerControl())


map.save("Map1.html")
