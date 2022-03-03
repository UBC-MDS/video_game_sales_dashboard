from dash import Dash, html , dcc, Input, Output
import altair as alt
from vega_datasets import data
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/UofTCoders/workshops-dc-py/master/data/processed/world-data-gapminder.csv"
df = pd.read_csv(url, parse_dates = ['year'])

def plot_chart(year= "1962", df=df.copy()):
    # Filter data for a year
    df = df.query(f'year == {year}')

    chart = alt.Chart(df).mark_circle().encode(
    alt.X('children_per_woman', scale=alt.Scale(zero=False)),
    alt.Y('life_expectancy',
          scale=alt.Scale(zero=False)),
    alt.Color('region'),
    alt.Size('population', scale=alt.Scale(range=(100, 1000))),
    tooltip='region').interactive().configure_axis(
    labelFontSize=14,
    titleFontSize=20
).configure_legend(
    titleFontSize=14
).configure_title(
    fontSize=30
)
    return chart.to_html()

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div(
    [
    html.H1('LifeExpectancy Plot of Gapminder', style={'color': 'blue', 'fontSize': 30}),
    html.Div(
            [
                "Year",
                dcc.Dropdown(
                    id="year",
                    options=[
                    {'label': year, 'value': year} for year in df['year'].dt.year
                    ],
                    value=["1962"],
                    placeholder='Select year between 1800-2018..')
            ]
        ),
    html.Iframe(
            id="iframe",
            srcDoc=plot_chart(year=["1962"]),
            style={"border-width": "0", "width": "100%", "height": "1500px"},
        ),
    ]
)

@app.callback(
    Output("iframe", "srcDoc"),
    Input("year", "value")
)

def update_output(year):
    return plot_chart(year)

if __name__ == '__main__':
    app.run_server(debug=True)
