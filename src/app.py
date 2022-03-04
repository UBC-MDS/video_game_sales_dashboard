from dash import Dash, html, dcc, Input, Output
import numpy as np
import pandas as pd
import dash_bootstrap_components as dbc
import os
import altair as alt

# Read in dataset
summary = pd.read_csv(os.path.join('../data/processed/summary.csv'))
ps4 = pd.read_csv(os.path.join('../data/processed/ps4.csv'))
videoGame = pd.read_csv(os.path.join('../data/processed/videoGame.csv'))
xbox = pd.read_csv(os.path.join( '../data/processed/xbox.csv'))

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server

app.layout = dbc.Container([
    dbc.Tabs([
  
        dbc.Tab([
            html.H1('Video Game Dashboard'),
            dbc.Row([
                dbc.Col([dcc.Dropdown(
                    id='global-year',
                    value=2016,  # REQUIRED to show the plot on the first page load
                    options=[{'label': col, 'value': col} for col in summary["Year"].unique()])])]),
            dbc.Col([
                dbc.Row(
                    html.Iframe(
                        id='global-market-share',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'})),
                dbc.Row(
                    html.Iframe(
                        id = 'global-critic-score',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'}
                        ))])], label='Global'),
        
        dbc.Tab([
            html.H1('Video Game Dashboard'),
            dbc.Row([
                dbc.Col([dcc.Dropdown(
                    id='na-year',
                    value=2016,  # REQUIRED to show the plot on the first page load
                    options=[{'label': col, 'value': col} for col in summary["Year"].unique()])])]),
            dbc.Col([
                dbc.Row(
                    html.Iframe(
                        id='na-market-share',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'})),
                dbc.Row(
                    html.Iframe(
                        id = 'na-critic-score',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'}
                        ))])], label='North America')
        ])])

# Set up callbacks/backend
@app.callback(
    Output('global-market-share', 'srcDoc'),
    Input('global-year', 'value'))
def global_market_share_plot(year):
    global_sales = (
        summary.groupby(["tag", "Year"]).sum()[["North America"]].reset_index()
    )
    global_sales_year = global_sales[global_sales.iloc[:, 1] == year].replace(
        "Video Games", "Others"
    )
    global_sales_year["percent"] = (
        global_sales_year["North America"] / global_sales_year["North America"].sum()
    )
    plot = (
        alt.Chart(global_sales_year, title="Market Shares of Companies")
        .mark_arc(innerRadius=70)
        .encode(
            theta=alt.Theta(field="North America", type="quantitative"),
            color=alt.Color(field="tag", type="nominal", legend=alt.Legend(title="Company")),
            tooltip=["percent"],
        )
    )
    return plot.to_html()

@app.callback(
    Output('na-market-share', 'srcDoc'),
    Input('na-year', 'value'))
def na_market_share_plot(year):
    na_sales = summary.groupby(["tag", "Year"]).sum()[["Global"]].reset_index()
    na_sales_year = na_sales[na_sales.iloc[:, 1] == year].replace("Video Games", "Others")
    na_sales_year["percent"] = na_sales_year["Global"] / na_sales["Global"].sum()
    plot = (
        alt.Chart(na_sales_year, title="Market Shares of Companies")
        .mark_arc(innerRadius=70)
        .encode(
            theta=alt.Theta(field="Global", type="quantitative"),
            color=alt.Color(field="tag", type="nominal", legend=alt.Legend(title="Company")),
            tooltip=["percent"],
        )
    )
    return plot.to_html()


@app.callback(
    Output('global-critic-score', 'srcDoc'),
    Input('global-year', 'value'))
def global_critic_score_plot(year):
    score = (videoGame.groupby(["Platform", "Year"]).mean())[
        ["Critic_Score"]
    ].reset_index()
    score_year = score[score.iloc[:, 1] == year].rename(
        columns={"Critic_Score": "Critic Score"}
    )
    plot = (
        alt.Chart(score_year, title="Critic Scores")
        .transform_window(
            rank="rank(Critic Score)",
            sort=[alt.SortField("Critic Score", order="descending")],
        )
        .mark_bar()
        .encode(
            x=alt.X("Platform", sort="-y"),
            y='Critic Score',
            tooltip=["Critic Score"]
        )
        .interactive()
    )
    return plot.to_html()

@app.callback(
    Output('na-critic-score', 'srcDoc'),
    Input('na-year', 'value'))
def na_critic_score_plot(year):
    score = (videoGame.groupby(["Platform", "Year"]).mean())[
        ["Critic_Score"]
    ].reset_index()
    score_year = score[score.iloc[:, 1] == year].rename(
        columns={"Critic_Score": "Critic Score"}
    )
    plot = (
        alt.Chart(score_year, title="Critic Scores")
        .transform_window(
            rank="rank(Critic Score)",
            sort=[alt.SortField("Critic Score", order="descending")],
        )
        .mark_bar()
        .encode(
            x=alt.X("Platform", sort="-y"),
            y='Critic Score',
            tooltip=["Critic Score"]
        )
        .interactive()
    )
    return plot.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)