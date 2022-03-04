import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import numpy as np
import pandas as pd
import plotly.express as px
import os
import altair as alt
import dash_bootstrap_components as dbc
from datetime import datetime

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
  
def global_sales_chart(company, years):
    ps4_global = ps4[["Year", "Global"]].groupby(['Year']).sum().head(6).rename(columns={"Global": "ps4"})
    xbox_global = xbox[["Year", "Global"]].groupby(['Year']).sum().reset_index().head(6).rename(columns={"Global": "xbox"})
    sales_global = ps4_global.join(xbox_global.set_index('Year'), on = "Year").reset_index()
    sales_global_year = sales_global.set_index(["Year"])
    sales_global_new = sales_global_year.loc[2013:years].reset_index()
    fig = px.line(sales_global_new, 
        x="Year", y=company, title='Sales Trend')
    return fig
  

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
  "position": "fixed",
  "top": 0,
  "left": 0,
  "bottom": 0,
  "width": "16rem",
  "padding": "2rem 1rem",
  "background-color": "#ADD8E6",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
  "margin-left": "18rem",
  "margin-right": "2rem",
  "padding": "2rem 1rem",
}

sidebar = html.Div(
  [
    html.H2("Video Game Sales Analytics App", className="display-4", style={'color': 'black', 'fontSize': 25, 'text-align':'center'}),
    html.Hr(),
    html.P(
      "A dashboard to analyze sales of major players in the video game industry", className="lead", 
      style={'color': 'black', 'fontSize': 18, 'text-align':'center'} 
    ),
    html.Hr(),
    html.P(
      "Sales Trend Companies", style={'color': 'black', 'fontSize': 15, 'text-align':'center'} 
    ),
    dcc.Dropdown(
      id = "company",
      options=[{'label': 'Xbox', 'value': 'xbox'},
      {'label': 'PlayStation4', 'value': 'ps4'}],
      value='ps4', multi=True),
    html.Hr(),
    html.P(
      "Market Share Year", style={'color': 'black', 'fontSize': 15, 'text-align':'center'} 
    ),
    html.Hr(),
    html.P(
      "Top Genres Year", style={'color': 'black', 'fontSize': 15, 'text-align':'center'} 
    ),
    html.Hr(),
    html.P(
      "Top Publisher Year", style={'color': 'black', 'fontSize': 15, 'text-align':'center'} 
    ),
    html.Hr(),
    html.P(
      "Critic Score Year", style={'color': 'black', 'fontSize': 15, 'text-align':'center'} 
    ),
    html.Hr(),
    html.P(f"""
        This dashboard was made by Amelia Tang, 
        Alex Yinan Guo, Yike Shi, and Mahmoodur Rahman.  
        Last updated 2022-03-05.
        License is in effect up to 
        {datetime.now().date()}.
        """, style={'color': 'black', 'fontSize': 12}  
        ),
    html.A("GitHub Repository",
    href="https://github.com/UBC-MDS/video_game_sales_dashboard", target="_blank",
    style={'color': 'black', 'fontSize': 12}
    ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div([
  dcc.Tabs([
    dcc.Tab(label='North America', children=[
      dbc.Row([
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
              updatemode="drag")]),
         dbc.Col([html.H3('PLACEHOLDER - ALEX - MARKET SHARE')])
      ]),
     dbc.Row([
        dbc.Col([html.H3('PLACEHOLDER - MAEVE - BAR CHART')]),
        dbc.Col([html.H3('PLACEHOLDER - MARVE - BAR CHART')]),
        dbc.Col([html.H3('PLACEHOLDER - ALEX - BAR CRITIC')]),
      ])]),
    dcc.Tab(label='Global', children=[
      dbc.Row([
        dbc.Col([
          dcc.Graph(id='global_sales_chart'),
          dcc.Slider(
            id="tab2-year-slider",
            min=2013,
            max=2018,
            step=1,
            value=2017,
            marks={i: str(i) for i in range(2013, 2019, 1)},
            tooltip={"placement": "top", "always_visible": True},
            updatemode="drag")]),
        dbc.Col([html.H3('PLACEHOLDER - ALEX - MARKET SHARE')])
         ]),
      dbc.Row([
          dbc.Col([html.H3('PLACEHOLDER - MAEVE - BAR CHART')]),
          dbc.Col([html.H3('PLACEHOLDER - MARVE - BAR CHART')]),
          dbc.Col([html.H3('PLACEHOLDER - ALEX - BAR CRITIC')])])])
          ])],id="page_content",style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# Set up callbacks/backend
@app.callback(
    Output('NA_sales_chart', 'figure'),
    Input('company', 'value'),
    Input('tab1-year-slider', 'value'))
def chart_output(company, years):
    return NA_sales_chart(company, years)
  
  
@app.callback(
    Output('global_sales_chart', 'figure'),
    Input('company', 'value'),
    Input('tab2-year-slider', 'value'))
def chart_output(company, years):
    return global_sales_chart(company, years)


if __name__ == "__main__":
  app.run_server(debug=True)
