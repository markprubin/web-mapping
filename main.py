import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

map = folium.Map(location=[40.758701, -111.876183], zoom_start=6, tiles="CartoDB Voyager")


fg = folium.FeatureGroup(name='My Map')


for lat, lon, elev in zip(lat, lon, elev):
    fg.add_child(folium.Marker(
        location=[lat, lon],
        popup=f"{elev} meters",
        icon=folium.Icon(color='red')))

map.add_child(fg)


map.save("Map1.html")
