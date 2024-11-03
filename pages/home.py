from dash import Dash, html, dcc
import pandas as pd

df = pd.read_csv('./data/electric_vehicle_pop_clean.csv')

home_layout = [
        html.Div([
            html.Div([
                html.Div('Electric Vehicle Population Data Analysis', className='title-div home-title-div'),
                html.Div('A data storytelling app', className='title-div home-subtitle-div'),
                dcc.Link('Start Story',href='/story1_1', className='story-next-btn change-color-hover')
            ], className='home-wrapper')
        ])
]
