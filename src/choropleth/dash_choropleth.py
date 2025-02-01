import json
from pathlib import Path

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html


def london_age_chart(age_data):
    # open the geojson
    file_path = Path(__file__).parent.joinpath('data','london_boroughs.geojson')
    with open(file_path) as json_file:
        la_geojson = json.load(json_file)

    # Create a choropleth mapbox using Plotly express
    # The geojson and the data can therefore be linked where
    # GEO_LABEL in the data matches properties.name in the geojson
    fig = px.choropleth_mapbox(age_data,
                               geojson=la_geojson,
                               locations="GEO_LABEL",
                               featureidkey="properties.name",
                               color="F105",
                               color_continuous_scale='Viridis',
                               range_color=(0, 200),
                               mapbox_style="carto-positron",
                               zoom=8,
                               center={"lat": 51.5074, "lon": 0.0000},
                               opacity=0.5,
                               hover_name="GEO_LABEL",
                               labels={'GEO_LABEL': 'Local authority'},
                               title="London residents over 100 in the 2011 Census"
                               )
    return fig

# Read the data for the over 100's (F105) into a data frame skipping the second heading row
age_data_path = Path(__file__).parent.joinpath('data','london_age_data.csv')
age_data = pd.read_csv(age_data_path, usecols=["GEO_LABEL", "F105"], skiprows=[1])
map_fig = london_age_chart(age_data)

meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1"}, ]
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

app.layout = dbc.Container([
    html.H1("Choropleth map demo using UK local authority geojson"),
    dcc.Graph(figure=map_fig)
])

if __name__ == '__main__':
    app.run(debug=True)
