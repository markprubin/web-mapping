import folium

map = folium.Map(location=[33.657029634028994, -112.08982501349456], zoom_start=16, tiles="CartoDB Voyager")


fg = folium.FeatureGroup(name='My Map')


for coordinates in [[33, -112],[34, -113]]:
    fg.add_child(folium.Marker(
        location=coordinates,
        popup="My house",
        icon=folium.Icon(color='red')))

map.add_child(fg)


map.save("Map1.html")
