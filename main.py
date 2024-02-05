import folium

map = folium.Map(location=[33.657029634028994, -112.08982501349456], zoom_start=16, tiles="CartoDB Voyager")

map.add_child(folium.Marker(
    location=[33.657029634028994, -112.08982501349456],
    popup="Yo",
    icon=folium.Icon(color='red')))


map.save("Map1.html")
