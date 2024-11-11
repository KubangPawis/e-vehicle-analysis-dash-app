from dash import Dash, html, dcc, Input, Output
from pages.home import home_layout
from pages.story1_1 import story1_1_layout
from pages.story1_2 import story1_2_layout
from pages.story2_1 import story2_1_layout, app_2_1_callback
from pages.story3_1 import story3_1_layout
from pages.story3_2 import story3_2_layout
from pages.story4_1 import story4_1_layout
import plotly.express as px
import pandas as pd
import json

df = pd.read_csv('./data/electric_vehicle_pop_clean.csv')
app = Dash(external_stylesheets=['https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'], suppress_callback_exceptions=True)

with open('./assets/us_county_geo.json') as f:
    geojson = json.load(f)

app_2_1_callback(app)

'''
STACKED BAR PLOT
-> 1. Leading Top 10 Producers of Electric Vehicles based on Number of E-Vehicles Produced; Afterwards, group based on E-Vehicle type (Stacked Bar Plot)
'''
top_producers_ordering = df.groupby(['Make'])['Model'].count().reset_index()
top_producers_ordering = top_producers_ordering.rename(columns={'Model': 'Count'})
top_producers_ordering = top_producers_ordering.sort_values(by='Count', ascending=False)['Make'].tolist()
top_producers = df.groupby(['Make', 'Electric Vehicle Type'])['Model'].count().reset_index()
top_producers.columns = ['Make', 'Electric Vehicle Type', 'Count']

vis1 = px.bar(top_producers, x='Make', y='Count', color='Electric Vehicle Type', category_orders={'Make': top_producers_ordering})
vis1.update_layout(
    width=1000,
    height=600,
    barmode='stack', 
    title='Top 10 Manufacturers of Electric Vehicles', 
    xaxis_title='Manufacturer', 
    yaxis_title='Number of E-Vehicles Produced',
    paper_bgcolor='lightgray',
    plot_bgcolor='white',
    title_font_size=20
    )

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

'''
SCATTER MAP
-> 2.2. Geographical Distribution of Registered Electric Vehicles
'''

vis2_2 = px.scatter_map(df, lat='Vehicle_Latitude_Loc', lon='Vehicle_Longitude_Loc', color='Make', zoom=3, center={'lat': 39.139918, 'lon': -95.383279})
vis2_2.update_layout(
    width=1000,
    height=600,
    title='E-Vehicle Geographical Distribution based on Manufacturer', 
    paper_bgcolor='lightgray',
    plot_bgcolor='white',
    title_font_size=20
    )

'''
LINE PLOT
-> 3.1. Trends in Number of Electric Vehicles Produced by Top 5 Manufacturers (1997-2024)
'''

line_top_producers = df[df['Make'] != 'Others']['Make'].value_counts().nlargest(5).index.tolist()
make_year_df = df[(df['Make'].isin(line_top_producers)) & (df['Model Year'].isin(range(1997, 2024)))].groupby(['Make', 'Model Year'])['Model'].count().reset_index()
make_year_df.columns = ['Make', 'Model Year', 'Count']

vis3_1 = px.line(make_year_df, x='Model Year', y='Count', color='Make')
vis3_1.update_layout(
    width=1000,
    height=600,
    title='Number of Produced E-Vehicles of Top 5 Manufacturer per Year (1997-2024)', 
    paper_bgcolor='lightgray',
    plot_bgcolor='white',
    title_font_size=20, 
    xaxis_gridcolor='LightGray', 
    yaxis_gridcolor='LightGray'
    )
vis3_1.update_xaxes(minor=dict(ticks='inside', showgrid=True), rangeslider_visible=True)
vis3_1.add_vline(x=2017, line_width=2, line_dash='dash', line_color='red')
'''
vis3_1.add_annotation(x=3, y=18,
                   text='Peak Value',
                   showarrow=True,
                   arrowhead=1)
'''

'''
LINE PLOT
-> 3.2. Trends in Electric Vehicle Type Demand Trends per Year
'''

type_production_year = df.groupby(['Electric Vehicle Type', 'Model Year'])['Model'].count().reset_index()
type_production_year.columns = ['Electric Vehicle Type', 'Model Year', 'Count']

vis3_2 = px.line(type_production_year, x='Model Year', y='Count', color='Electric Vehicle Type')
vis3_2.update_layout(
    width=1000,
    height=600,
    title='E-Vehicle Type Production per Year (2014-2024)', 
    paper_bgcolor='lightgray',
    plot_bgcolor='white',
    title_font_size=20,
    xaxis_gridcolor='LightGray', 
    yaxis_gridcolor='LightGray'
    )
vis3_2.update_xaxes(minor=dict(ticks='inside', showgrid=True), rangeslider_visible=True)

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
    width=1000,
    height=600,
    title='Difference between Tesla E-Vehicle Model Demand Distributions of 2017 and 2018', 
    paper_bgcolor='lightgray',
    plot_bgcolor='white',
    title_font_size=20,
    xaxis_gridcolor='LightGray', 
    yaxis_gridcolor='LightGray'
    )

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
    width=1000,
    height=600,
    title='Price vs Performance of E-Vehicles', 
    paper_bgcolor='lightgray',
    plot_bgcolor='white',
    title_font_size=20,
    xaxis_gridcolor='LightGray', 
    yaxis_gridcolor='LightGray'
    )
vis5.update_xaxes(minor=dict(ticks='inside', showgrid=True))


app.layout = html.Div([
        dcc.Store(id='geojson_us', data=geojson),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home_layout
    if pathname == '/story1_1':
        return story1_1_layout
    if pathname == '/story1_2':
        return story1_2_layout
    if pathname == '/story2_1':
        return story2_1_layout
    if pathname == '/story3_1':
        return story3_1_layout
    if pathname == '/story3_2':
        return story3_2_layout
    if pathname == '/story4_1':
        return story4_1_layout
    else:
        return html.Div('404: Page Not Found')

if __name__ == '__main__':
    app.run_server(debug=True)