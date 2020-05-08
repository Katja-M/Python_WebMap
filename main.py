# 1. Install folium and jinja2
import folium
import pandas

volcano_data = pandas.read_csv('C://Users//Katja//PythonCodingTraining//Webmaps//Volcanoes.txt')

def colour(elevation):
    min_elevation = min(volcano_data['ELEV'])
    max_elevation = max(volcano_data['ELEV'])
    step_value = (max(volcano_data['ELEV']) - min(volcano_data['ELEV']))/3
    if elevation in range(int(min_elevation), int(min_elevation + step_value)):
        color = 'green'
    elif elevation in range(int(min_elevation + step_value), int(min_elevation + step_value * 2)):
        color = 'orange'
    else:
        color = 'red'
    return color

# The main object of folium is the map object
# Two inputs are required, the location consisting of longitude and latitude
# and the zoom_start which defines zoom level when opening map
map = folium.Map(location=[volcano_data['LAT'].mean(),volcano_data['LON'].mean()], zoom_start = 6)
# map object ONLY INSIDE PYTHON

for lat, lon, name, elevation in zip(volcano_data['LAT'], volcano_data['LON'], volcano_data['NAME'], volcano_data['ELEV']):
    # 1. Option: Separate function for different colouring
    #folium.Marker(location=[lat,lon], popup= name, tooltip= 'Find out what place this is', icon=folium.Icon(color= colour(elevation),icon='info-sign')).add_to(map)
    # 2. Option: If statement inside the function
    #folium.Marker(location=[lat,lon], popup= name, tooltip= 'Find out what place this is', icon=folium.Icon(color='green'if elevation in range(0,1000)\
        # else 'orange' if elevation in range(1000, 3000) else 'red' ,icon='info-sign')).add_to(map)

    # Alternativ to add markers
    map.add_child(folium.Marker(location=[lat,lon], popup= name, tooltip= 'Find out what place this is', icon = folium.Icon(color= colour(elevation), icon_color = 'green')))



#print(dir(folium))
#print(dir(folium.Map))
#print(dir(folium.Marker))
#print(help(folium.Marker))


# After necessary objects have been added to the map, the map is 'published'
# Using save() method in order to build an HTML file
map.save(outfile = 'myfirstmap.html')
# File created which contains the HTML code