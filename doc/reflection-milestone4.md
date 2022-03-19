# Reflection for Milestone 4

Group 20: Amelia Tang, Alex Yinan Guo, Maeve Yike Shi, Mahmood Rahman

The goal for this final milestone is to reproduce the same dashboard in `R`, which we previously did in `python` for milestone 3, and incorporated all the feedback from prior iterations. 

## Implementations 

### Data Wrangling 

We used the Kaggle dataset [Video Games Sales Dataset](https://www.kaggle.com/sidtwr/videogames-sales-dataset?select=Video_Games_Sales_as_at_22_Dec_2016.csv) and conducted data wrangling. The processed data sets contain all the data we need to create the graphs in our proposal. 

### Dashboard creation

#### Dash in python

Link to the dashboard : https://video-game-dashboard.herokuapp.com/
We used dash in Python to create the dashboard. The dashboard has two tabs showing information relating to video games sales by two regions, North America and Global. A line-chart showing trend according to year-span and can be manipulated through the year range slider. A doughnut chart showing market shares by companies (Gaming platforms). At the bottom of the dashboard, we can see the top-ranking Genres and Publishers of video games, and a bar chart showing platforms' Critic score and we can choose on the sidebar to view these rankings of different years. We can also change the numbers of the rankings we would like to see using the drop down menu at the bottom of the two ranking bar charts. We decided to let the year-slider's left side fixed because we did not have many years of data available. The line plot was to demonstrate the trends and it would be visually not meaningful if the year range was to small. We also decided to implement a doughnut chart with the percentage of each company (gaming platform) shown if hovered over instead of a tree map because we believe the doughnut chart would visualize the proportions better in our case.  
![demo](../src/fig/demo_py.gif)

#### Dash in R

Link to the dashboard : https://video-game-dashboard-r.herokuapp.com/
We used dash in R to create the dashboard. The dashboard has two tabs showing information relating to video games sales by two regions, North America and Global. A line-chart showing trend according to year-span and can be manipulated through the year range slider. A doughnut chart showing market shares by companies (Gaming platforms). At the bottom of the dashboard, we can see the top-ranking Genres and Publishers of video games, and a bar chart showing platforms' Critic score and we can choose on the sidebar to view these rankings of different years. We can also change the numbers of the rankings we would like to see using the drop down menu at the bottom of the two ranking bar charts. We decided to let the year-slider's left side fixed because we did not have many years of data available. The line plot was to demonstrate the trends and it would be visually not meaningful if the year range was to small. We also decided to implement a doughnut chart with the percentage of each company (gaming platform) shown if hovered over instead of a tree map because we believe the doughnut chart would visualize the proportions better in our case.  
![demo](../src/fig/demo_r.gif)

## Contrast: Python and R version

We used `ggplot` package is case of `R` to make the plots, whereas we used `altair` and `plotly` to make the plots in python. We used `faviscon` to make logo showing up in the python dashboard, where we did not make logo for R dashboard. In both the dashboards we used `bootstrap` of `dash`. In `R` dashboard, our plots at the bottom are arranged as 4x4 tiles, in contrast to our `python` dashboard. Furthermore, the deployment time on Heroku was much shorter on the Python version of the app. However, one of the main issues was the performance in terms of load speed. The R version performed significantly better than the Python version. 

## Adaptation

### General improvemnt

 - Added the loading feature
 - Re-organized the charts so they look a bit more well organized, add a dividing line
 - added Regions to plot titles
 - We add regions (i.e. North America or Global) to each plot title for clear description.
 - Added user score plots
 - In the previous version of our dashboard, there was incoherence regarding the format of axis titles. In the new version, we uniformed all axis title to capitalize the first word.

### Feedback from Group 19

 - Inclusion of user scores: We already included a plot on `User score` at the bottom.
 - Fixed the issue where x-axis starts to show decimal values (e.g. 2013.5) when the range of years is smaller.

### General feedback

 - Our plots are understand and the legends have explanatory names. The legends are different from the variable names
 - We are using classical white background. So feedback relating to background does not imply.
 - Our dashboard has a one-line introduction on what is the dashboard about. Our names are also added to the dashboard
 - Our widgets have proper labels
 
## Unresolved issues

### Feedback from Group 19

 - On the year range-selector for the sales trend according to companies, adding text "Select a year range": We believe the slider is self-explanatory, but it is a nice suggestion
 - A difference in screen size, it was a bit difficult to see all the plots in the dashboard at once: We optimized the dashboard to be viewed in a laptop screen in `Full view` mode, as instructed by the instructions of milestone 4.
 - For the Sales trend plot, the x-axis slider with two knobs to select the minimum and maximum years: We designed to use the dashboard to visualize the change over the years in comparison to year 2013.
 - Visualize genres associated with the least sales: We plotted the most popular genres, but yes, inclusion of least popular genres would have given more information.
 - Inclusion of  time-series plot with stats such as mean and standard deviation: Our dashboard summaries the frequencies at a high level. But inclusion of time-series plots along with statistical summeries will provide more information.
 - Inclusion of more regions in `Tab` such as Europe and Japan: Through our dashboard we tried to summerizes the findings on a global scale Vs North American stats. But definitely adding more regions will make this dashboard useful to other audiances as well.

### General feedback

 - Information on how reactivity works: Although our plots are mostly self-explanatory, but adding information will help audiances to be more compatible.

## Limitation of the Dashboard

Most of our limitations are discussed in unresolved issues. Apart from those, we have room to work on our tooltips to include more information. Also inclusion of maps would make the users idea of traits and trends according to geographical distribution.  

## Strength of the Dashboard

Our dashboard presents a comprehensive and primary descriptive analysis on some of the most important variables for a sales analyst of a video game company. The app is very easy to use with filtering criteria and simple visualizations. The large buttons and straight-forward clean layout avoid condensation of elements in the dashboard. Another advantage is, due to simplicity the app is less resource-hungry and visualizations are snappy which prevents fatigue and makes the experience pleasant and satisfying.
