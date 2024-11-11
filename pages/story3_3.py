from dash import html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/electric_vehicle_pop_clean.csv')

'''
LINE PLOT
-> 3.2. Trends in Electric Vehicle Type Demand Trends per Year
'''

type_production_year = df.groupby(['Electric Vehicle Type', 'Model Year'])['Model'].count().reset_index()
type_production_year.columns = ['Electric Vehicle Type', 'Model Year', 'Count']

vis3_2 = px.line(type_production_year, x='Model Year', y='Count', color='Electric Vehicle Type')
vis3_2.update_layout(
    font=dict(
        color='white'
    ),
    width=1500,
    height=900,
    title=None, 
    paper_bgcolor='rgba(0, 0, 0, 0)',
    plot_bgcolor='white',
    xaxis_gridcolor='LightGray', 
    yaxis_gridcolor='LightGray'
    )
vis3_2.update_xaxes(minor=dict(ticks='inside', showgrid=False), rangeslider_visible=False)

story3_3_layout = html.Div([
        html.Div([
            html.Div([
                html.H1('Trends in Electric Vehicle Type Demand Trends per Year', className='title-div'),
                dcc.Graph(figure=vis3_2)
            ]),
            html.Div([
                html.Div([
                    html.Div([
                        html.H1('Starting 2018, BEVs have become more in demand than PHEVs.')
                    ], className='insight-container animate__animated animate__jackInTheBox')
                ], className='story-desc-wrapper scale_animation')
            ], className='insight-group')
        ], className='story-wrapper-row'),
        html.Div([
            dcc.Link('<<', href='/story3_2', className='story-next-btn change-color-hover'),
            dcc.Link('>>', href='/story4_1', className='story-next-btn change-color-hover')
        ], className='next-btn-container')
    ])