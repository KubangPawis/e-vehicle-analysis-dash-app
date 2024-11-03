from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/electric_vehicle_pop_clean.csv')

'''
STACKED BAR PLOT
-> 1. Leading Top 10 Producers of Electric Vehicles based on Number of E-Vehicles Produced; Afterwards, group based on E-Vehicle type (Stacked Bar Plot)
'''
top_producers_ordering = df.groupby(['Make'])['Model'].count().reset_index()
top_producers_ordering = top_producers_ordering.rename(columns={'Model': 'Count'})
top_producers_ordering = top_producers_ordering.sort_values(by='Count', ascending=False)['Make'].tolist()
top_producers = df.groupby(['Make', 'Electric Vehicle Type'])['Model'].count().reset_index()
top_producers.columns = ['Make', 'Electric Vehicle Type', 'Count']


vis1 = px.bar(top_producers, x='Make', y='Count', color='Electric Vehicle Type', category_orders={'Make': top_producers_ordering}, color_discrete_sequence=['#00bcd4', '#ff4081', '#8bc34a', '#ffeb3b', '#ff5722'])

vis1.update_layout(
    font=dict(
        color='white'
    ),
    width=1700,
    height=1000,
    barmode='stack', 
    title=None, 
    xaxis_title='Manufacturer', 
    yaxis_title='Number of E-Vehicles Produced',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    title_font_size=20
    )

story1_2_layout = html.Div([
        html.Div([
            html.Div([
                html.H1('Top 10 Manufacturers of Electric Vehicles', className='title-div'),
                dcc.Graph(figure=vis1)
            ]),
            html.Div([
                html.Div([
                    html.H1('BEVs are the most commonly produced and demanded type of E-Vehicles in the US.')
                ], className='insight-container')
            ], className='story-desc-wrapper animate__animated animate__rotateIn')  
        ], className='story-wrapper'),
        html.Div([
            dcc.Link('>>', href='/story2', className='story-next-btn change-color-hover')
        ], className='next-btn-container')
    ])