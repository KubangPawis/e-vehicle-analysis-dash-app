from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/electric_vehicle_pop_clean.csv')

'''
BUBBLE CHART
-> 5. MSRP vs Electric Range based on the Corresponding Number of Manufactured E-Vehicles
'''
erange_production_count = df.groupby('Electric Range')['Model'].count().reset_index()
erange_production_count.columns = ['Electric Range', 'Count']
erange_df = pd.merge(df, erange_production_count, on='Electric Range')
erange_df = erange_df[(erange_df['Electric Range'] != 0) & (erange_df['Base MSRP'] != 0)]
erange_df

vis5 = px.scatter(erange_df, y='Electric Range', x='Base MSRP', color='Electric Vehicle Type', size='Count', range_y=[0, 300], log_x=True, size_max=60)
vis5.update_layout(
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
vis5.update_xaxes(minor=dict(ticks='inside', showgrid=True))

story5_1_layout = html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H1('Unlike PHEVs, BEV performance (electric range) increases along with the price.')
                    ], className='insight-container animate__animated animate__jackInTheBox')
                ], className='story-desc-wrapper scale_animation')
            ], className='insight-group'),
            html.Div([
                html.Div([
                    html.H1('MSRP vs Electric Range based on the Corresponding Number of Manufactured E-Vehicles', className='title-div')
                ], className='title-div--story'),
                html.Div([
                    dcc.Graph(figure=vis5)
                ], className='graph-wrapper')
            ]),
        ], className='story-wrapper-row'),
        html.Div([
            dcc.Link('<<', href='/story4_2', className='story-next-btn change-color-hover'),
            dcc.Link('>>', href='/story5_2', className='story-next-btn change-color-hover')
        ], className='next-btn-container')
    ])