# ==============================================================================
#                           Import Dependencies
# ==============================================================================

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import numpy as np
import pandas as pd
import plotly.express as px
import os
import altair as alt
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from datetime import datetime

# ==============================================================================
#                            Load the data and define constants
# ==============================================================================

#current path
current_dir = os.path.abspath(os.path.dirname(__file__))
summary = pd.read_csv(os.path.join(current_dir, '../data/processed/summary.csv'))
ps4 = pd.read_csv(os.path.join(current_dir, '../data/processed/ps4.csv'))
videoGame = pd.read_csv(os.path.join(current_dir, '../data/processed/videoGame.csv'))
xbox = pd.read_csv(os.path.join(current_dir, '../data/processed/xbox.csv'))

def NA_sales_chart(company, years):
    ps4_NA = ps4[["Year", "North America"]].groupby(['Year']).sum().head(6).rename(columns={"North America": "PS4"})
    xbox_NA = xbox[["Year", "North America"]].groupby(['Year']).sum().reset_index().head(6).rename(columns={"North America": "XBox"})
    sales_NA = ps4_NA.join(xbox_NA.set_index('Year'), on = "Year").reset_index()
    sales_NA_year = sales_NA.set_index(["Year"])
    sales_NA_new = sales_NA_year.loc[2013:years].reset_index()
    fig = px.line(sales_NA_new, x="Year", y=company, title='North America Sales Trend', labels=dict(value="Sales in million", variable="Company"))
    fig.update_layout(title_x=0.5)
    fig['layout']['title']['font'] = dict(size=20)


    return fig
  
def global_sales_chart(company, years):
    ps4_global = ps4[["Year", "Global"]].groupby(['Year']).sum().head(6).rename(columns={"Global": "PS4"})
    xbox_global = xbox[["Year", "Global"]].groupby(['Year']).sum().reset_index().head(6).rename(columns={"Global": "XBox"})
    sales_global = ps4_global.join(xbox_global.set_index('Year'), on = "Year").reset_index()
    sales_global_year = sales_global.set_index(["Year"])
    sales_global_new = sales_global_year.loc[2013:years].reset_index()
    fig = px.line(sales_global_new, 
        x="Year", y=company, title='Global Sales Trend', labels=dict(value="Sales in million", variable="Company"))
    fig.update_layout(title_x=0.5)
    fig['layout']['title']['font'] = dict(size=20)
    return fig

def global_genre_chart(year, rownum):
    genre = summary.groupby(['Genre', 'Year']).size().to_frame(name = 'Counts').reset_index()
    genre_year = genre[genre['Year'] == year]
    chart = alt.Chart(genre_year, title='Global Top Genres').transform_window(
            rank='rank(Counts)',
            sort=[alt.SortField('Counts', order='descending')]
        ).transform_filter(
            alt.datum.rank <= rownum
        ).mark_bar().encode(
            x='Counts',
            y=alt.Y('Genre', sort = '-x')
        ).configure_title(fontSize=20)
    return chart.to_html()


def global_publisher_chart(year, rownum):
    publisher = summary.groupby(['Publisher', 'Year']).size().to_frame(name = 'Counts').reset_index()
    publisher_year = publisher[publisher['Year'] == year]
    chart = alt.Chart(publisher_year, title='Global Top Publishers').transform_window(
            rank='rank(Counts)',
            sort=[alt.SortField('Counts', order='descending')]
        ).transform_filter(
            alt.datum.rank <= rownum
        ).mark_bar().encode(
            x='Counts',
            y=alt.Y('Publisher', sort = '-x')
        ).configure_title(fontSize=20)
    return chart.to_html()

def na_genre_chart(year, rownum):
    genre = summary[summary['North America'] !=0].groupby(['Genre', 'Year']).size().to_frame(name = 'Counts').reset_index()
    genre_year = genre[genre['Year'] == year]
    chart = alt.Chart(genre_year, title='North America Top Genres').transform_window(
            rank='rank(Counts)',
            sort=[alt.SortField('Counts', order='descending')]
        ).transform_filter(
            alt.datum.rank <= rownum
        ).mark_bar().encode(
            x='Counts',
            y=alt.Y('Genre', sort = '-x')
        ).configure_title(fontSize=20)
    return chart.to_html()

def na_publisher_chart(year, rownum):
    publisher = summary[summary['North America'] !=0].groupby(['Publisher', 'Year']).size().to_frame(name = 'Counts').reset_index()
    publisher_year = publisher[publisher['Year'] == year]
    chart = alt.Chart(publisher_year, title='North America Top Publishers').transform_window(
            rank='rank(Counts)',
            sort=[alt.SortField('Counts', order='descending')]
        ).transform_filter(
            alt.datum.rank <= rownum
        ).mark_bar().encode(
            x='Counts',
            y=alt.Y('Publisher', sort = '-x')
        ).configure_title(fontSize=20)
    return chart.to_html()

def global_market_share_plot(year):
    global_sales = summary.groupby(["tag", "Year"]).sum()[["Global"]].reset_index()
    global_sales_year = global_sales[global_sales["Year"] == year].replace(
        "Video Games", "Others"
    )
    global_sales_year["percent"] = (
        round(
            (global_sales_year["Global"] / global_sales_year["Global"].sum() * 100), 2
        ).astype(str)
        + "%"
    )
    plot = (
        alt.Chart(global_sales_year, title="Global Market Shares of Companies")
        .mark_arc(innerRadius=70)
        .encode(
            theta=alt.Theta(field="Global", type="quantitative"),
            color=alt.Color(
                field="tag", type="nominal", legend=alt.Legend(title="Company")
            ),
            tooltip=["percent"],
        ).configure_title(fontSize=20)
    )
    return plot.to_html()

def na_market_share_plot(year):
    global_sales = summary.groupby(["tag", "Year"]).sum()[["North America"]].reset_index()
    global_sales_year = global_sales[global_sales["Year"] == year].replace(
        "Video Games", "Others"
    )
    global_sales_year["percent"] = (
        round(
            (global_sales_year["North America"] / global_sales_year["North America"].sum() * 100), 2
        ).astype(str)
        + "%"
    )
    plot = (
        alt.Chart(global_sales_year, title="North America Market Shares of Companies")
        .mark_arc(innerRadius=70)
        .encode(
            theta=alt.Theta(field="North America", type="quantitative"),
            color=alt.Color(
                field="tag", type="nominal", legend=alt.Legend(title="Company")
            ),
            tooltip=["percent"],
        ).configure_title(fontSize=20)
    )
    return plot.to_html()



def global_critic_score_plot(year):
    score = (videoGame.groupby(["Platform", "Year"]).mean())[
        ["Critic_Score"]
    ].reset_index()
    score_year = score[score.iloc[:, 1] == year].rename(
        columns={"Critic_Score": "Critic score"}
    )
    plot = (
        alt.Chart(score_year, title="Global Critic Scores")
        .transform_window(
            rank="rank(Critic score)",
            sort=[alt.SortField("Critic score", order="descending")],
        )
        .mark_bar()
        .encode(
            x=alt.X("Platform", sort="-y"),
            y='Critic score',
            tooltip=["Critic score"]
        ).properties(width=200,
        height=480).configure_title(fontSize=20)
        .interactive()
    )
    return plot.to_html()


def global_user_score_plot(year):
    score = (videoGame.groupby(["Platform", "Year"]).mean())[
        ["User_Score"]
    ].reset_index()
    score_year = score[score.iloc[:, 1] == year].rename(
        columns={"User_Score": "User score"}
    )
    plot = (
        alt.Chart(score_year, title="Global User Scores")
        .transform_window(
            rank="rank(User score)",
            sort=[alt.SortField("User score", order="descending")],
        )
        .mark_bar()
        .encode(
            x=alt.X("Platform", sort="-y"),
            y='User score',
            tooltip=["User score"]
        ).properties(width=200,
        height=480).configure_title(fontSize=20)
        .interactive()
    )
    return plot.to_html()


def na_critic_score_plot(year):
    score = (videoGame.groupby(["Platform", "Year"]).mean())[
        ["Critic_Score"]
    ].reset_index()
    score_year = score[score.iloc[:, 1] == year].rename(
        columns={"Critic_Score": "Critic score"}
    )
    plot = (
        alt.Chart(score_year, title="North America Critic Scores")
        .transform_window(
            rank="rank(Critic score)",
            sort=[alt.SortField("Critic score", order="descending")],
        )
        .mark_bar()
        .encode(
            x=alt.X("Platform", sort="-y"),
            y='Critic score',
            tooltip=["Critic score"]
        ).properties(width=200,
        height=480).configure_title(fontSize=20)
        .interactive()
    )
    return plot.to_html()

def na_user_score_plot(year):
    score = (videoGame.groupby(["Platform", "Year"]).mean())[
        ["User_Score"]
    ].reset_index()
    score_year = score[score.iloc[:, 1] == year].rename(
        columns={"User_Score": "User score"}
    )
    plot = (
        alt.Chart(score_year, title="North America User Scores")
        .transform_window(
            rank="rank(User score)",
            sort=[alt.SortField("User score", order="descending")],
        )
        .mark_bar()
        .encode(
            x=alt.X("Platform", sort="-y"),
            y='User score',
            tooltip=["User score"]
        ).properties(width=200,
        height=480).configure_title(fontSize=20)
        .interactive()
    )
    return plot.to_html()

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

app.title = "Video Game Sales Analytics"

server=app.server
logo = "https://github.com/UBC-MDS/video_game_sales_dashboard/blob/main/src/assets/favicon.png"


# ==============================================================================
#                            Styles
# ==============================================================================
# the style arguments for the sidebar. 
SIDEBAR_STYLE = {
  "position": "fixed",
  "top": 0,
  "left": 0,
  "bottom": 0,
  "width": "14rem",
  "padding": "2rem 1rem",
  "background-color": "#ADD8E6",
  "overflow": "scroll",
  "text-align":"center"
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
  "margin-left": "18rem",
  "margin-right": "2rem",
  "padding": "2rem 1rem",
  "width": "1500px",
  "height": "1000px"
}


# ==============================================================================
#                            App Layout
# ==============================================================================
# The codes for side bar was adapted from https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/ 

sidebar = html.Div(
  [
    html.H2("Video Game Sales Analytics", className="display-4", style={'color': 'black', 'fontSize': 25, 'text-align':'center'}),
    html.Hr(),
    html.P(
      "A dashboard to analyze sales of major players in the video game industry", className="lead", 
      style={'color': 'black', 'fontSize': 18, 'text-align':'center'} 
    ),
    dbc.Collapse(
        dbc.Card(dbc.CardBody("On the dashboard, you will find sales trend plots and market shares charts for North American and Global, top publishers and top genres for each year as well as users and critic scores for each year. ")),
        id="collapse",
        is_open=False,
        ),
    dbc.Button(
            "Read more",
            id="collapse-button",
            className="mb-3",
            color="secondary",
            n_clicks=0,
        ),
    html.Hr(),
    html.P(
      "Sales Trend Companies", style={'color': 'black', 'fontSize': 15, 'text-align':'center'} 
    ),
    dcc.Dropdown(
      id = "company",
      options=[{'label': 'XBox', 'value': 'XBox'},
      {'label': 'PlayStation4', 'value': 'PS4'}],
      value='PS4', multi=True),
    html.Hr(),
    html.P(
      "Market Share Year", style={'color': 'black', 'fontSize': 15, 'text-align':'center'} 
    ),
    dcc.Dropdown(
        id='market_share_year',
        value=2016,  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in range(2013, 2019)]),
    html.Hr(),
    html.P(
      "Top Genres Year", style={'color': 'black', 'fontSize': 15, 'text-align':'center'} 
    ),
    dcc.Dropdown(
        id='genre_year',
        value=2016,  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in range(2013, 2019)]),
    html.Hr(),
    html.P(
      "Top Publishers Year", style={'color': 'black', 'fontSize': 15, 'text-align':'center'} 
    ),
    dcc.Dropdown(
        id='publisher_year',
        value=2016,  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in range(2013, 2019)]),
    html.Hr(),
    html.P(
      "Critic Scores Year", style={'color': 'black', 'fontSize': 15, 'text-align':'center'} 
    ),
    dcc.Dropdown(
        id='critic_year',
        value=2016,  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in range(2013, 2019)]),
    html.Hr(),
    html.P(
      "User Scores Year", style={'color': 'black', 'fontSize': 15, 'text-align':'center'} 
    ),
    dcc.Dropdown(
        id='user_year',
        value=2016,  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in range(2013, 2019)]),
    html.Hr(),
    html.P(f"""
        This dashboard was made by Amelia Tang, 
        Alex Yinan Guo, Yike Shi, and Mahmoodur Rahman.  
        Last updated 2022-03-18.
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
            dcc.Loading(
              type="cube",
              fullscreen = True,
              children=[
                dcc.Graph(id='NA_sales_chart', style={'width': '600px', 'height': '400px'}),
                dcc.Slider(
                  id="tab1-year-slider",
                  min=2013,
                  max=2018,
                  step=1,
                  value=2017,
                  marks={i: str(i) for i in range(2013, 2019, 1)},
                  tooltip={"placement": "top", "always_visible": True},
                  updatemode="drag")])]),
         html.Br(),
         html.Br(),
         html.Br(),
         dbc.Col([html.Iframe(id='na-market-share',
         style={'border-width': '2px', 'width': '100%', 'height': '400px'})])]),
         html.Br(),
         html.Hr(),
         html.Br(),
     dbc.Row([
        dbc.Col([
          dbc.Row([html.Iframe(
                id='na_genre',
                style={'border-width': '0', 'width': '900px', 'height': '200px'}),
                html.H5("Number of Top Genres to Display", style={'color': 'black', 'fontSize': 15, 'text-align':'left'} ),
                dcc.Dropdown(
                id='na_genre_rownum',
                value=5,
                options=[{'label': col, 'value': col} for col in [3, 4, 5, 6, 7, 8, 9]])]),
          html.Br(),
          html.Hr(),
          dbc.Row([html.Iframe(
                id='na_publisher',
                style={'border-width': '0', 'width': '900px', 'height': '200px'}),
                html.H5("Number of Top Publishers to Display", style={'color': 'black', 'fontSize': 15, 'text-align':'left'}),
                dcc.Dropdown(
                id='na_publisher_rownum',
                value=5,
                options=[{'label': col, 'value': col} for col in [3, 4, 5, 6, 7, 8, 9]])])]),
        dbc.Col([dbc.Row([
          dbc.Col([html.Iframe(
                id='na-critic-score',
                style={'border-width': '0', 'width': '100%', 'height': '800px'})]),
          dbc.Col([html.Iframe(
                id='na-user-score',
                style={'border-width': '0', 'width': '100%', 'height': '800px'})])])]), 
            ])]),

      dcc.Tab(label='Global', children=[
        dbc.Row([
          dbc.Col([
            dcc.Graph(id='global_sales_chart', style={'width': '600px', 'height': '400px'}),
            dcc.Slider(
              id="tab2-year-slider",
              min=2013,
              max=2018,
              step=1,
              value=2017,
              marks={i: str(i) for i in range(2013, 2019, 1)},
              tooltip={"placement": "top", "always_visible": True},
              updatemode="drag")]),
         html.Br(),
         html.Br(),
         html.Br(),
         dbc.Col([html.Iframe(id='global-market-share',
         style={'border-width': '2px', 'width': '100%', 'height': '400px'})])]),
         html.Br(),
         html.Hr(),
         html.Br(),
     dbc.Row([
        dbc.Col([
          dbc.Row([html.Iframe(
                id='global_genre',
                style={'border-width': '0', 'width': '900px', 'height': '200px'}),
                html.H5("Number of Top Genres to Display", style={'color': 'black', 'fontSize': 15, 'text-align':'left'} ),
                dcc.Dropdown(
                id='global_genre_rownum',
                value=5,
                options=[{'label': col, 'value': col} for col in [3, 4, 5, 6, 7, 8, 9]])]),
          html.Br(),
          html.Hr(),
          dbc.Row([html.Iframe(
                id='global_publisher',
                style={'border-width': '0', 'width': '900px', 'height': '200px'}),
                html.H5("Number of Top Publishers to Display", style={'color': 'black', 'fontSize': 15, 'text-align':'left'}),
                dcc.Dropdown(
                id='global_publisher_rownum',
                value=5,
                options=[{'label': col, 'value': col} for col in [3, 4, 5, 6, 7, 8, 9]])])]),
        dbc.Col([dbc.Row([
            dbc.Col([html.Iframe(
                id='global-critic-score',
                style={'border-width': '0', 'width': '100%', 'height': '800px'})]),
            dbc.Col([html.Iframe(
                id='global-user-score',
                style={'border-width': '0', 'width': '100%', 'height': '800px'})])])]),
        ])])])],
        id="page_content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# ==============================================================================
#                            Callbacks and Backend
# ==============================================================================

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

@app.callback(
    Output('global_genre', 'srcDoc'),
    Input('genre_year', 'value'),
    Input('global_genre_rownum', 'value'))
def global_genre_output(year, rownum):
    return global_genre_chart(year, rownum)

@app.callback(
    Output('global_publisher', 'srcDoc'),
    Input('publisher_year', 'value'),
    Input('global_publisher_rownum', 'value'))
def global_publisher_output(year, rownum):
    return global_publisher_chart(year, rownum)

@app.callback(
    Output('na_genre', 'srcDoc'),
    Input('genre_year', 'value'),
    Input('na_genre_rownum', 'value'))
def global_publisher_output(year, rownum):
    return na_genre_chart(year, rownum)

@app.callback(
    Output('na_publisher', 'srcDoc'),
    Input('publisher_year', 'value'),
    Input('na_publisher_rownum', 'value'))
def global_publisher_output(year, rownum):
    return na_publisher_chart(year, rownum)

@app.callback(
    Output('global-market-share', 'srcDoc'),
    Input('market_share_year', 'value'))
def global_market_share(year):
        return global_market_share_plot(year)


@app.callback(
    Output('na-market-share', 'srcDoc'),
    Input('market_share_year', 'value'))
def na_market_share(year):
    return na_market_share_plot(year)



@app.callback(
    Output('global-critic-score', 'srcDoc'),
    Input('critic_year', 'value'))
def global_critic_score(year):
    return global_critic_score_plot(year)

@app.callback(
    Output('na-critic-score', 'srcDoc'),
    Input('critic_year', 'value'))
def na_critic_score(year):
    return na_critic_score_plot(year)

@app.callback(
    Output('global-user-score', 'srcDoc'),
    Input('user_year', 'value'))
def global_user_score(year):
    return global_user_score_plot(year)

@app.callback(
    Output('na-user-score', 'srcDoc'),
    Input('user_year', 'value'))
def na_user_score(year):
    return na_user_score_plot(year)

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")])
    
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
  app.run_server(debug=True)
