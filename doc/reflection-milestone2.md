# Reflection for Milestone 2
## Group 20 
## Amelia Tang, Alex Yinan Guo, Maeve Yike Shi, Mahmood Rahman

In this section, your group should document on what you have implemented in your dashboard so far and explain what is not yet implemented. It is important that you include what you know is not working in your dashboard, so that your TAs can distinguish between features in development and bugs.

Reflect on what you think your dashboard does well what its limitations are, and what are good future improvements and additions. This section should not be more than 500 words and the reflection-milestone2.md document should live in your GitHub.com repo in the doc folder.


# Reflection of milestone 2

## Executables 

### Data 

We used the kaggle dataset [Video Games Sales Dataset](https://www.kaggle.com/sidtwr/videogames-sales-dataset?select=Video_Games_Sales_as_at_22_Dec_2016.csv), which has 3 datasets (.csv files) having information on platform, Year of Release, Genre, Publisher, NASales, EUSales, JPSales, OtherSales and Global_Sales. After preprocessing and cleaning the data we had a total of 11563 observations.

### Dashboard creation

We chose dash and python to create the dashboard which has two tabs showing information information relating to video games sales by two regions, North America and Global. A line-chart showing trend according to year-span, which can be manually set by manipulating scale. A doughnut chart showing market shares by companies (Gaming platforms). At the bottom of the dashboard, we can see the top-ranking Genres and Publishers of video games, and a bar chart showing platforms according to critic scores.

![demo](../src/fig/demo.gif)
  Figure 1. Overview of the dashboard
</p>

## Limitation of the Dashboard

- The dashboard can be viewed on a mobile device, but with limited visibility.  Can be optimized in terms of scaling to make it more compatible for viewing in mobile devices.
- A pointer can be helpful to guide user for a more interactive experience. 
- Work can be done on the aesthetics of the elements of visualization like smoothing of edges, animated tab-changes and fonts that stand out. 