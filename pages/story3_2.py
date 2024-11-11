from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/electric_vehicle_pop_clean.csv')

'''
LINE PLOT
-> 3.1. Trends in Number of Electric Vehicles Produced by Top 5 Manufacturers (1997-2024)
'''

line_top_producers = df[df['Make'] != 'Others']['Make'].value_counts().nlargest(5).index.tolist()
make_year_df = df[(df['Make'].isin(line_top_producers)) & (df['Model Year'].isin(range(1997, 2024)))].groupby(['Make', 'Model Year'])['Model'].count().reset_index()
make_year_df.columns = ['Make', 'Model Year', 'Count']

vis3_1 = px.line(make_year_df, x='Model Year', y='Count', color='Make')
vis3_1.update_layout(
    font=dict(
        color='white'
    ),
    width=1500,
    height=900,
    title=None,
    paper_bgcolor='rgba(0, 0, 0, 0)',
    plot_bgcolor='white',
    title_font_size=20, 
    xaxis_gridcolor='LightGray', 
    yaxis_gridcolor='LightGray'
    )
vis3_1.update_xaxes(minor=dict(ticks='inside', showgrid=False), rangeslider_visible=False)
vis3_1.add_vline(x=2017, line_width=2, line_dash='dash', line_color='red')

story3_2_layout = html.Div([
        html.Div([
            html.Div([
                html.H1('Trends in Number of Electric Vehicles Produced by Top 5 Manufacturers (1997-2024)', className='title-div'),
                dcc.Graph(figure=vis3_1)
            ]),
            html.Div([
                html.Div([
                    html.Div([
                        html.H1('E-Vehicle Production did not go lower upon the upset of COVID-19.')
                    ], className='insight-container animate__animated animate__jackInTheBox')
                ], className='story-desc-wrapper scale_animation')
            ], className='insight-group')
        ], className='story-wrapper-row'),
        html.Div([
            dcc.Link('<<', href='/story3_1', className='story-next-btn change-color-hover'),
            dcc.Link('>>', href='/story3_3', className='story-next-btn change-color-hover')
        ], className='next-btn-container')
    ])