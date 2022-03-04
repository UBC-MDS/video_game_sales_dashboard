from dash import Dash, html, dcc, Input, Output
import numpy as np
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import os
import altair as alt

# Load data
ps4 = pd.read_csv("../data/processed/ps4.csv").dropna()
xbox = pd.read_csv("../data/processed/xbox.csv").dropna()

def NA_sales_chart(company, years):
    ps4_NA = ps4[["Year", "North America"]].groupby(['Year']).sum().head(6).rename(columns={"North America": "ps4"})
    xbox_NA = xbox[["Year", "North America"]].groupby(['Year']).sum().reset_index().head(6).rename(columns={"North America": "xbox"})
    sales_NA = ps4_NA.join(xbox_NA.set_index('Year'), on = "Year").reset_index()
    sales_NA_year = sales_NA.set_index(["Year"])
    sales_NA_new = sales_NA_year.loc[2013:years].reset_index()
    fig = px.line(sales_NA_new, x="Year", y=company, title='Sales Trend')
    return fig

# Containers 
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server
app.layout = dbc.Container([
    html.H3('Video Game Sales Analysis'),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
              id = "company",
              options=[
                {'label': 'Xbox', 'value': 'xbox'},
                {'label': 'PlayStation4', 'value': 'ps4'}],
                value='ps4', multi=True)]),
        dbc.Col([
            dcc.Graph(id='NA_sales_chart'),
            dcc.Slider(
              id="tab1-year-slider",
              min=2013,
              max=2018,
              step=1,
              value=2017,
              marks={i: str(i) for i in range(2013, 2019, 1)},
              tooltip={"placement": "top", "always_visible": True},
              updatemode="drag")])])])


# Set up callbacks/backend
@app.callback(
    Output('NA_sales_chart', 'figure'),
    Input('company', 'value'),
    Input('tab1-year-slider', 'value'))
def chart_output(company, years):
    return NA_sales_chart(company, years)


if __name__ == '__main__':
    app.run_server(debug=True)
