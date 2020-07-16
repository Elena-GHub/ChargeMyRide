import os
import ssl
import folium
import pandas as pd
import json
from flask import Flask, render_template

if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
    ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__, template_folder='templates')

app.debug = True

# live data source
url = "https://analisi.transparenciacatalunya.cat/api/views/tb2m-m33b/rows.csv"
df_stations = pd.read_csv(url)


# live data source json
# url = "https://datos.gob.es/apidata/catalog/dataset/a09002970-estacions-de-recarrega-per-a-vehicle-electric-a-catalunya.json"
# df_stations = pd.read_json(url)


# offline last data collected source
def returned_data_type_is_dictionary():
    with open('data/charging_stations.json') as data:
        json_return = json.load(data)
    return json_return


# render map with charging stations
stations = folium.map.FeatureGroup()
latitude = 41.837937  # Catalonia's geographical center - latitude value
longitude = 1.539776  # Catalonia's geographical center - longitude value
catalonia_map = folium.Map(location=[latitude, longitude], zoom_start=8.2)
tooltip = 'Más información'
latitudes = list(df_stations.LATITUD)
longitudes = list(df_stations.LONGITUD)
labels = list(df_stations['DESIGNACIÓ-DESCRIPTIVA'])
for lat, long, label in zip(latitudes, longitudes, labels):
    stations.add_child(
        folium.Marker([lat, long], popup = label,
                      tooltip = tooltip,
                      icon = folium.Icon(icon = 'flash')
                      )).add_to(catalonia_map)
catalonia_map.add_child(stations)
catalonia_map.save('index.html')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
