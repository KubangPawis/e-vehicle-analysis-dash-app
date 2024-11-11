from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/electric_vehicle_pop_clean.csv')

'''
PIE CHART (SUBPLOTS)
-> 4. Difference between Tesla E-Vehicle Model Demand Distributions of 2017 and 2018
'''

pie_model_distribution = df.groupby(['Model'])['VIN (1-10)'].count().reset_index()
pie_model_distribution.columns = ['Model', 'Count']
pie_model_distribution = pd.merge(df, pie_model_distribution, on='Model')[['Model', 'Make', 'Model Year', 'Count']]
pie_model_distribution = pie_model_distribution[(pie_model_distribution['Make'] == 'Tesla') & (pie_model_distribution['Model Year'].isin([2017, 2018]))]

vis4 = px.pie(pie_model_distribution, values='Count', names='Model', facet_col='Model Year', hole=.3, category_orders={'Model Year': [2017, 2018]})
vis4.update_layout(
    font=dict(
        color='white'
    ),
    width=1000,
    height=700,
    title=None, 
    paper_bgcolor='rgba(0, 0, 0, 0)',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    title_font_size=20,
    xaxis_gridcolor='LightGray', 
    yaxis_gridcolor='LightGray'
    )

story4_1_layout = html.Div([
        html.Div([
            html.Div([
                html.H1('Difference between Tesla E-Vehicle Model Demand Distributions of 2017 and 2018'),
            ], className='title-div--story'),
            html.Div([
                dcc.Graph(figure=vis4)
            ], className='graph-wrapper'),
            html.Div([
                html.Div([
                    html.Div([
                        html.H1('The production and demand of Tesla\'s MODEL 3 overtook the E-vehicle market in 2018.')
                    ], className='insight-container animate__animated animate__jackInTheBox')
                ], className='story-desc-wrapper scale_animation')
            ], className='insight-group')
        ], className='story-wrapper-col'),
        html.Div([
            dcc.Link('>>', href='/story5_1', className='story-next-btn change-color-hover')
        ], className='next-btn-container')
    ])