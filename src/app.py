import dash
import dash_table as dt
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import datetime

pio.templates.default = "simple_white"


# Read in global data
movies = pd.read_csv("../data/processed/videoGame.csv")

# Setup app and layout/frontend
app = dash.Dash(
    __name__, title="Video Games Sales Analytics App", external_stylesheets=[dbc.themes.LUMEN]
)
server = app.server

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "z-index": 4000000,
}

CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "z-index": -1,
}


cards = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6("Average User Score", className="card-title"),
                    html.H4(id="average-vote", className="card-text"),
                ]
            ),
            color="primary",
            outline=True,
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6("Average User Count", className="card-title"),
                    html.H4(id="vote-count", className="card-text"),
                ]
            ),
            color="primary",
            outline=True,
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H6("Average Sales", className="card-title"),
                    html.H4(id="average-revenue", className="card-text"),
                ]
            ),
            color="primary",
            outline=True,
        ),
    ]
)


genre_graphs = dbc.CardDeck(
    [
        dbc.Card(
            [
                dbc.CardHeader(html.H4(id="vote-plot-title")),
                dbc.CardBody(
                    dcc.Graph(
                        id="vote-plot",
                    )
                ),
            ],
            color="success",
            outline=True,
        ),
        dbc.Card(
            [
                dbc.CardHeader(html.H4(id="revenue-plot-title")),
                dbc.CardBody(dcc.Graph(id="revenue-plot")),
            ],
            color="success",
            outline=True,
        ),
    ]
)

studio_graphs = dbc.CardDeck(
    [
        dbc.Card(
            [
                dbc.CardHeader(html.H4(id="vote-scatter-title")),
                dbc.CardBody(
                    dcc.Graph(
                        id="vote-scatter-plot",
                    )
                ),
            ],
            color="info",
            outline=True,
        ),
        dbc.Card(
            [
                dbc.CardHeader(html.H4(id="table-title")),
                dbc.CardBody([html.Div(id="movies-data-frame")]),
            ],
            color="info",
            outline=True,
        ),
    ]
)

content = html.Div(
    [
        cards,
        html.Br(),
        genre_graphs,
        html.Br(),
        studio_graphs,
        html.Hr(),
        dcc.Markdown(
            """
            This app was made by Group 20 Consulting Co using [Kaggle dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset?select=movies_metadata.csv). Our team is composed of [Person 1](https://person1), [Person 2](https://person2), [Person 3](https://person3) and [Mahmoodur Rahman](https://www.linkedin.com/in/drmrahman/).
            The app follows [MIT's license](https://github.com/UBC-MDS/video_game_sales_dashboard/blob/main/LICENSE) and the source code can be found on [GitHub](https://github.com/UBC-MDS/video_game_sales_dashboard).
            """
        ),
        html.P(
            f"""The app was last updated on {datetime.datetime.now().date()}.
        """
        ),
    ],
    id="page-content",
    style=CONTENT_STYLE,
)

controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Platform"),
                dcc.Dropdown(
                    id="xgenre-widget",
                    value=[]",  # REQUIRED to show the plot on the first page load
                    multi=True,
                    options=[
                        {"label": col, "value": col}
                        for col in movies["genres"].unique()
                    ],
                    clearable=False,
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Year Range (US$ mil)"),
                dcc.RangeSlider(
                    id="xbudget-widget",
                    min=1985,
                    max=2016,
                    value=[1985, 2016,
                    marks={
                        1985: "19",
                        1990: "1990",
                        1995: "1995",
                        2000: "2000",
                        2005: "2005",
                        2010: "2010",
                        2016: "2016",
                    },
                ),
            ]
        ),
    ],
    body=True,
    className="text-dark",
)

sidebar = html.Div(
    [
        html.H2("Video Games Sales Analytics App", className="display-4"),
        html.Hr(),
        controls,
        html.Hr(),
        html.P(
            "The app is designed to allow sales analyst of video game companies to identify sales trends and understand competitive landscape.",
            className="lead",
        ),
    ],
    style=SIDEBAR_STYLE,
    className="bg-primary text-white",
)

app.layout = html.Div([sidebar, content])

def color_map(studios, primary_list, secondary_list):
    if studios in primary_list:
        return 1
    if studios in secondary_list:
        return 2
    return 0

# Set up callbacks/backend

@app.callback(
    Output("vote-plot", "figure"),
    Output("revenue-plot", "figure"),
    Output("vote-scatter-plot", "figure"),
    Output("average-revenue", "children"),
    Output("vote-plot-title", "children"),
    Output("revenue-plot-title", "children"),
    Output("vote-scatter-title", "children"),
    Output("table-title", "children"),
    Output("average-vote", "children"),
    Output("vote-count", "children"),
    Output("average-profit", "children"),
    Output("movies-data-frame", "children"),
    Input("xgenre-widget", "value"),
    Input("xbudget-widget", "value"),
    Input("revenue-plot", "selectedData"),
    Input("vote-plot", "selectedData"),
)
def app_builder(
    xgenre, budget, revenue_selected, vote_selected
):  
    """The function to return all call-back for the app given inputs from end-users

    Parameters
    ----------
    xgenre : str
        the chosen genre by user
    budget : list
        the chosen budget range specified by user in a list of lower-bound and upper-bound numbers
    revenue_selected : str
        the name of the studio selected under revenue plot
    vote_selected : str
        the name of the studio selected under vote plot

    Returns
    -------
    figure/plot object
        vote boxplot, revenue boxplot, scatter plot
    float
        average revenue, average vote, average vote count, average profit
    str:
        titles for the respective plot
    DashTable:
        a table of most popular movies
    """
    
    studios_by_revenue = (
        movies.groupby("Platform")["Global"].median().sort_values().index.tolist()
    )
    filtered_movies = movies[movies["Platform"] == xgenre].query(
        "@budget[0] < budget and budget < @budget[1]"
    )

    # Cards
    average_revenue = "US${:,.2f} mil".format(filtered_movies["Global"].mean())
    average_vote = str(round(filtered_movies["User_Score"].mean(), 1))
    vote_count = str(round(filtered_movies["User_Count"].mean()))

    # Genre graphs
    studios_list = []
    studios_str = ""
    revenue_list = []
    vote_list = []

    if revenue_selected is not None:
        revenue_list = [point["y"] for point in revenue_selected["points"]]
        studios_list += revenue_list
        studios_list = list(set(studios_list))
        studios_str = "for the Platforms: "
        studios_str += ", ".join(studios_list)
    if vote_selected is not None:
        vote_list = [point["y"] for point in vote_selected["points"]]
        studios_list += vote_list
        studios_list = list(set(studios_list))
        studios_str = "for the Platforms: "
        studios_str += ", ".join(studios_list)

    if not studios_list:
        studios_list = filtered_movies.studios.unique()

    studio_movies = filtered_movies[filtered_movies["Platform"].isin(studios_list)]

    vote_chart = px.box(
        filtered_movies,
        x="vote_average",
        y="Platform",
        labels={"Platform": "Platform", "vote_average": "Vote Average"},
        boxmode='overlay',
        color=filtered_movies.studios.apply(color_map, args=(vote_list, revenue_list)),
        category_orders={'color': [0,1,2]},
        color_discrete_map={0: 'grey',1: '#1f77b4',2: 'skyblue'}
    )

    vote_chart.add_bar(
        x=[filtered_movies.vote_average.max()] * filtered_movies.studios.nunique(),
        y=filtered_movies.studios.unique(),
        orientation="h",
        opacity=0.0001,
        hoverinfo="none",
        showlegend=False,
    )

    vote_chart.add_vline(
        x=filtered_movies["User_Score"].mean(),
        line_width=3,
        line_dash="dash",
        line_color="green",
        annotation_text="Mean Vote Average",
        annotation_position="top",
        annotation_font_color="green",
        annotation_font_size=10,
    )

    vote_chart.update_layout(clickmode="event+select", showlegend=False, yaxis_categoryorder = 'category ascending')
    revenue_chart = px.box(
        filtered_movies,
        x="revenue",
        y="studios",
        labels={"Platform": "Platform", "Global": "Sales (US$ mil)"},
        boxmode='overlay',
        color=filtered_movies.studios.apply(color_map, args=(revenue_list, vote_list)),
        category_orders={'color': [0,1,2]},
        color_discrete_map={0: 'grey',1: '#1f77b4',2: 'skyblue'}
    )

    revenue_chart.add_bar(
        x=[filtered_movies.revenue.max()] * filtered_movies.studios.nunique(),
        y=filtered_movies.studios.unique(),
        orientation="h",
        opacity=0.0001,
        hoverinfo="none",
        showlegend=False,
    )

    revenue_chart.add_vline(
        x=filtered_movies["Global"].mean(),
        line_width=3,
        line_dash="dash",
        line_color="green",
        annotation_text="Mean Revenue",
        annotation_position="top",
        annotation_font_color="green",
        annotation_font_size=10,
    )

    revenue_chart.update_layout(clickmode="event+select", showlegend=False, yaxis_categoryorder = 'category ascending')

    # Studio-specific graphs
    vote_scatter_chart = px.scatter(
        studio_movies,
        x="User_Score",
        y="User_Count",
        labels={"User_Count": "User Count", "User_Score": "Average Score"},
        hover_name="title"
    )

    top_movies_df = (studio_movies.drop_duplicates(subset = ["Game"]).nlargest(15, ["User_Score"]))[
        ["Game", "User_Score", "Global", "Platform"]
    ]

    top_movies_df.profit = round(top_movies_df.profit, 2)
    top_movies_df.vote_average = round(top_movies_df.vote_average, 2)
    top_movies_df.rename(
        columns={
            "Game": "Title",
            "User_Score": "Vote Average",
            "Global": "Sales (US$ mil)",
            "Platform": "Platform",
        },
        inplace=True,
    )
    
    top_movies_df['Vote Average'] = top_movies_df['Vote Average'].map(lambda x: '{0:.2f}'.format(x))


    return (
        vote_chart,
        revenue_chart,
        vote_scatter_chart,
        average_revenue,
        f"{xgenre} Movies Vote Average by Studio",
        f"{xgenre} Movies Financials by Studio",
        f"Voting Profile for {xgenre} Movies {studios_str}",
        f"Most Popular {xgenre} Movies (by Vote Average) {studios_str}",
        average_vote,
        vote_count,
        dt.DataTable(
            data = top_movies_df.to_dict('rows'),
            columns = [{"id": x, "name": x} for x in top_movies_df.columns],
            sort_action='native',
            style_cell={
                'textAlign': 'right', 
                'font_size': '13px', 
                'font-family':'Open Sans',
                'whiteSpace': 'normal', 
                'height': 'auto'
                },
            style_cell_conditional=[
                {
                    'if': {'column_id': 'Title'},
                    'textAlign': 'left'
                }
            ],
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold',
                'font_size': '14px',
                'font-family':'Open Sans'
            },
            style_as_list_view=True,
        )
    )


if __name__ == "__main__":
    app.run_server(debug=True)