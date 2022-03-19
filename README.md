Video Game Sales Analytics Dashboard
================
Amelia Tang, Alex Yinan Guo, Yike Shi, and Mahmoodur Rahman
<br>Dashboard link: https://video-game-dashboard.herokuapp.com/ 

## Background

Our dashboard visualizes North American and global sales and
sales-related data, such as top publishers and top genres based on sales
and market share based on sales by year. More in details in our
[proposal](https://github.com/UBC-MDS/video_game_sales_dashboard/blob/main/doc/proposal.md).

## Table of Content

-   [What are we doing?](#what-are-we-doing)
-   [Dashboard description](#dashboard-description)
-   [Future development](#future-development)
-   [License](#license)

## What are we doing?

Electronic video games in 2020 generated a revenue of around $165
billion. To thrive in this competitive industry, video game companies
have sales analysts who need to keep their eyes on stats relating to
sales. We built this simple dashboard to provide visual aids for the
sales analysts and to save their time on data wrangling for regional and
yearly data.

## Dashboard Description

![demo](./src/fig/demo_py.gif) Figure 1. Overview of the dashboard
</p>

The dashboard contains a landing page that by default shows the North
America sales line plot for PlayStation4, top publishers in the most
recent years available in the data set, top genres for the most recent
available year, a chart shows market share of the major players in the
industry in the most recent available year and an average critic score
of games on different platform in the most recent available year in the
data set. On the top of the page, a user can use the tabs to navigate
between the North America and global sales to show sales trends in North
America and the sales trend globally (under the `Global` tab). Moreover,
a user can use the year slider under the sales line plot to choose the
range of years of sales he/she would like to view from 2013. From the
filter on the side bar, a user can choose to show sales of different
companies, PS4 and/or Xbox. In addition, a user can also use the drop
down menus on the side bar to choose the year of top publishers, top
genres, market share and average critic score he/she would like to view.
At the bottom of the `Top Genre` and `Top Publisher` charts, a user can
choose how many top genres or publishers he/she want to see from 5 to 9.

## Future development

We are calling for developers to help us improve the existing features
and implement new ones. For those who are interested in develop the
`video game sales analytics` dashboard, you can follow the steps to run
the app locally.

#### Installation

Clone the repository using `git clone` Install virtual environment using
[venv](https://docs.python.org/3/library/venv.html):

    # Create an venv virual environment 
    python -m venv videogame 

    # Activate the environment 
    source videogame/bin/activate 

    # Install the requirements 
    pip install -r requirements.txt

or if you would like to create the environment locally, at the project
root:

    conda env create -f videogame.yaml
    conda activate videogame

### Run the app locally

Via the command line: 
```
python src/app.py
```
or via Docker Compose: 

To run this app using Docker write the following commands after cloning the repo:

```bash
cd video_game_sales_dashboard
docker-compose up
```
Finally, open the app in the following URL http://0.0.0.0:8050


#### Contribution Guidelines

If you have some ideas regarding this project and wish to help, please
review our [contributing guidelines](CONTRIBUTING.md).

#### Suggestions

All suggestions for improvements are welcomed! We would particularly
appreciate developments in the following areas: <br>- Real-time tracking
of the sales data using the companies’ quarterly or annual financial
statements published online <br>- North America regional sales analysis
such as heap maps to indicate the amount of sales in different U.S.
States and Canadian provinces <br>- A plot associate Critic scores with
sales to examine the relationship between the two

## License

`Video Game Sales Analytics` dashboard is licensed under the
terms of the MIT license.
