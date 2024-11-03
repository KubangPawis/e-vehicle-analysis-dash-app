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
    opacity=0.5,
    color_discrete_sequence=['#00bcd4', '#ff4081', '#8bc34a', '#ffeb3b', '#ff5722']
)

vis2_1.update_layout(
    font=dict(
        color='white'
    ),
    width=1100,
    height=800,
    title=None, 
    paper_bgcolor='rgba(0, 0, 0, 0)',
    plot_bgcolor='white',
    title_font_size=20
    )

story2_1_layout = html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H1('Tesla E-Vehicles are most prevalent in the Washington and Californian regions, but are generally found in many other parts of the US')
                    ], className='insight-container')
                ], className='story-desc-wrapper animate__animated animate__rotateIn'),
                html.Div([
                    html.Div([
                        html.H1('Tesla owners in Floridian counties constitute about 90% of the E-Vehicle population in the said state')
                    ], className='insight-container')
                ], className='story-desc-wrapper animate__animated animate__rotateIn'),
                html.Div([
                    html.Div([
                        html.H1('Chevrolet E-Vehicle owners come second to Tesla in terms of pre    valence, but are more dispersed than densely grouped throughout the US.')
                    ], className='insight-container')
                ], className='story-desc-wrapper animate__animated animate__rotateIn'),
            ], className='insight-group'),
            html.Div([
                html.H1('E-Vehicle Prevalence over US Counties based on Manufacturer', className='title-div'),
                dcc.Loading(
                children=[dcc.Graph(figure=vis2_1)])
            ]),
        ], className='story-wrapper'),
        html.Div([
            dcc.Link('>>', href='/story2', className='story-next-btn change-color-hover')
        ], className='next-btn-container')
    ])