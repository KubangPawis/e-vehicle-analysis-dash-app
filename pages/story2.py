from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import json

df = pd.read_csv('./data/electric_vehicle_pop_clean.csv')

'''
CHLOROPLETH
-> 2.1. Geographical Distribution of Registered Electric Vehicles
'''

with open('./assets/us_county_geo.json') as f:
    geojson = json.load(f)

county_popular_make = df.groupby('County')['Make'].agg(lambda x: x.mode()[0]).reset_index()

vis2_1 = px.choropleth_mapbox(
    county_popular_make,
    geojson=geojson,
    locations='County',
    color='Make',
    featureidkey='properties.NAME',
    mapbox_style='carto-positron',
    zoom=3,
    center={'lat': 39.139918, 'lon': -95.383279},
    opacity=0.5
)

vis2_1.update_layout(
    width=1000,
    height=600,
    title='E-Vehicle Prevalence over US Counties based on Manufacturer', 
    paper_bgcolor='lightgray',
    plot_bgcolor='white',
    title_font_size=20
    )

vis2_1.update_geos(fitbounds='locations', visible=False)

story1_layout = [
    dcc.Graph(figure=vis2_1)
]