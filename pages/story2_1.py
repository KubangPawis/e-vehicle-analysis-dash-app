from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/electric_vehicle_pop_clean.csv')

'''
CHLOROPLETH
-> 2.1. Geographical Distribution of Registered Electric Vehicles
'''

county_popular_make = df.groupby('County')['Make'].agg(lambda x: x.mode()[0]).reset_index()

story2_1_layout = html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H1('Tesla E-Vehicles are most prevalent in the Washington and Californian regions, but are generally found in many other parts of the US')
                    ], className='insight-container animate__animated animate__rotateIn')
                ], className='story-desc-wrapper scale_animation'),
                html.Div([
                    html.Div([
                        html.H1('Tesla owners in Floridian counties constitute about 90% of the E-Vehicle population in the said state')
                    ], className='insight-container animate__animated animate__rotateIn')
                ], className='story-desc-wrapper scale_animation'),
                html.Div([
                    html.Div([
                        html.H1('Chevrolet E-Vehicle owners come second to Tesla in terms of pre    valence, but are more dispersed than densely grouped throughout the US.')
                    ], className='insight-container animate__animated animate__rotateIn')
                ], className='story-desc-wrapper scale_animation'),
            ], className='insight-group'),
            html.Div([
                html.Div([
                    html.H1('E-Vehicle Prevalence over US Counties based on Manufacturer', className='title-div')
                ], className='title-div'),
                html.Div([
                    dcc.Loading(children=[dcc.Graph(id='story2_1')])
                ], className='graph-wrapper')
            ]),
        ], className='story-wrapper-row'),
        html.Div([
            dcc.Link('<<', href='/story1_2', className='story-next-btn change-color-hover'),
            dcc.Link('>>', href='/story3_1', className='story-next-btn change-color-hover')
        ], className='next-btn-container')
    ])

'''
'''

def app_2_1_callback(app):
    @app.callback(
        Output('story2_1', 'figure'),
        [Input('geojson_us', 'data')]
    )
    def update_graph(geojson_us):
        vis2_1 = px.choropleth_mapbox(
                county_popular_make,
                geojson=geojson_us,
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
            width=1500,
            height=900,
            title=None, 
            paper_bgcolor='rgba(0, 0, 0, 0)',
            plot_bgcolor='white',
            title_font_size=20
            )
        return vis2_1