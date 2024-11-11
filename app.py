from dash import Dash, html, dcc, Input, Output
from pages.home import home_layout
from pages.end import end_layout
from pages.story1_1 import story1_1_layout
from pages.story1_2 import story1_2_layout
from pages.story2_1 import story2_1_layout, app_2_1_callback
from pages.story3_1 import story3_1_layout
from pages.story3_2 import story3_2_layout
from pages.story3_3 import story3_3_layout
from pages.story4_1 import story4_1_layout
from pages.story4_2 import story4_2_layout
from pages.story5_1 import story5_1_layout
from pages.story5_2 import story5_2_layout
import pandas as pd
import json

df = pd.read_csv('./data/electric_vehicle_pop_clean.csv')
app = Dash(external_stylesheets=['https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'], suppress_callback_exceptions=True)

with open('./assets/us_county_geo.json') as f:
    geojson = json.load(f)

app_2_1_callback(app)

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
    if pathname == '/story3_3':
        return story3_3_layout
    if pathname == '/story4_1':
        return story4_1_layout
    if pathname == '/story4_2':
        return story4_2_layout
    if pathname == '/story5_1':
        return story5_1_layout
    if pathname == '/story5_2':
        return story5_2_layout
    if pathname == '/end':
        return end_layout
    else:
        return html.Div('404: Page Not Found')

if __name__ == '__main__':
    app.run_server(debug=True)