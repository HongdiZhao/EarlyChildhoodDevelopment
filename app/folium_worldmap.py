import folium
import pandas as pd
import os

data = pd.read_csv('data/MICS_country_info.csv',encoding='cp1252')
world_geocode = os.path.join('data', 'world-countries.json')

lat = list(data['lat'])
lng = list(data['lng'])
name = list(data['name'])
total = list(data['Total'])
outcome_identifyletter_r = list(data['outcome_identifyletter_r'])
earlyc_edu_r = list(data['earlyc_edu_r'])
has_hometoy_r = list(data['has_hometoy_r'])
data_to_plot = data[['name_id','outcome_identifyletter_r']]
data_to_plot_edu = data[['name_id','earlyc_edu_r']]

m = folium.Map(location = [0,0],zoom_start = 1.5)

for lt, ln, nm, tot, oc in zip(lat, lng, name, total, outcome_identifyletter_r):
    m.add_child(folium.Marker(location=[lt,ln], popup="Country: "+nm+ "; Total Obs: "+str(tot)+ "; Child Indentify 10 letters "+str(oc)))

folium.Choropleth(geo_data=world_geocode, 
             data=data_to_plot,
             columns=['name_id', 'outcome_identifyletter_r'],
             key_on='feature.id',
             fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
             name='ECD Overview: Identify Letters',
             legend_name="Child Development Overview: Identify Letters").add_to(m)

folium.GeoJson(world_geocode, name='World Map').add_to(m)
folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('Stamen Terrain').add_to(m)
folium.LayerControl().add_to(m)

m.save('templates/worldmap.html')


m2 = folium.Map(location = [0,0],zoom_start = 1.5)

for lt, ln, nm, oc in zip(lat, lng, name, earlyc_edu_r):
    m2.add_child(folium.Marker(location=[lt,ln], popup="Country: "+nm+ "; Attend Early Childhoold Education Program "+str(oc)))

folium.Choropleth(geo_data=world_geocode, 
             data=data_to_plot_edu,
             columns=['name_id', 'earlyc_edu_r'],
             key_on='feature.id',
             fill_color='BuPu', fill_opacity=0.7, line_opacity=0.2,
             name='ECD Overview: Education',
             legend_name="Child Development Overview: Education").add_to(m2)

folium.GeoJson(world_geocode, name='World Map').add_to(m2)
folium.TileLayer('openstreetmap').add_to(m2)
folium.TileLayer('Stamen Terrain').add_to(m2)
folium.LayerControl().add_to(m2)

m2.save('templates/worldmap_edu.html')