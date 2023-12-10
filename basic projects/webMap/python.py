import folium
import pandas 

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_procedure(elev):
	if elev < 1000:
		return 'green'
	elif 1000<= elev < 3000:
		return 'orange'
	else:
		return 'red'
#print(data)
#print(data.columns)

map = folium.Map(location=[38.58, -99.99], zoom_start=5, titles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

#print(map)

fgp=folium.FeatureGroup(name="Population")

for lt, ln, el in zip(lat, lon, elev):
	fgv.add_child(folium.Marker(location=[lt, ln], radius = 5, popup=str(el)+" m", icon=folium.Icon(color=color_procedure(el))))

#for coordinates in [[11.26, 75.78],[11.29, 75.77]]:
#	fg.add_child(folium.Marker(location=coordinates, popup="Hi Marker", icon=folium.Icon(color="red")))
fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()), 
style_function=lambda X: {'fillColor':'green' if X['properties']['POP2005'] < 100000000 else 'orange' if 100000000 <= X['properties']['POP2005'] < 200000000 else 'red'}))


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("Map.html")
