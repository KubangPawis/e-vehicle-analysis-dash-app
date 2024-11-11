from dash import Dash, html, dcc
import pandas as pd

df = pd.read_csv('./data/electric_vehicle_pop_clean.csv')

end_layout = [
        html.Div([
            html.Div([
                html.Div('Thank You!', className='title-div home-title-div animate__animated animate__bounceIn'),
                html.Div('I hope that you gained some new insights', className='title-div home-subtitle-div animate__animated animate__bounceIn'),
                dcc.Link('Back to Home',href='/', className='story-next-btn change-color-hover')
            ], className='home-wrapper')
        ])
]
