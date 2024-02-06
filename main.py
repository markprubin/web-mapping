import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

map = folium.Map(location=[40.758701, -111.876183], zoom_start=6, tiles="CartoDB Voyager")

info = """<h5>Volcano Info:</h5>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

fg = folium.FeatureGroup(name='My Map')


for lat, lon, elev, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=info % (name, name, elev), width=200, height=100)
    fg.add_child(folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(iframe),
        icon=folium.Icon(color='red')))

map.add_child(fg)


map.save("Map1.html")
