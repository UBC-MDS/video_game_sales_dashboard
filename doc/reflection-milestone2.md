# Reflection for Milestone 2
Group 20: Amelia Tang, Alex Yinan Guo, Maeve Yike Shi, Mahmood Rahman

## Implementations 

### Data Wrangling 

We used the Kaggle dataset [Video Games Sales Dataset](https://www.kaggle.com/sidtwr/videogames-sales-dataset?select=Video_Games_Sales_as_at_22_Dec_2016.csv) and conducted data wrangling. The processed data sets contains all the data we need to create the graphs in our proposal. 

### Dashboard creation

We used dash in Python to create the dashboard. The dashboard has two tabs showing information relating to video games sales by two regions, North America and Global. A line-chart showing trend according to year-span and can be manipulated through the year range slider. A doughnut chart showing market shares by companies (Gaming platforms). At the bottom of the dashboard, we can see the top-ranking Genres and Publishers of video games, and a bar chart showing platforms' Critic score and we can choose on the sidebar to view these rankings of different years. We can also change the numbers of the rankings we would like to see using the drop down menu at the bottom of the two ranking bar charts. We decided to let the year-slider's left side fixed because we did not have many years of data available. The line plot was to demonstrate the trends and it would be visually not meaningful if the year range was to small. We also decided to implement a doughnut chart with the percentage of each company (gaming platform) shown if hovered over instead of a tree map because we believe the doughnut chart would visualize the proportions better in our case.  

![demo](../src/fig/demo.gif)
  Figure 1. Overview of the dashboard
</p>

## Limitation of the Dashboard
- We do not have as many years of data available as it assumed in our original sketch / proposal.     
- The dashboard can be viewed on a mobile device, but with limited visibility. We can improve browser and mobile compatibility. 
- A pointer can be helpful to guide user for a more interactive experience. 
- Work can be done on the aesthetics of the elements of visualization including but not limited to making the graphs look more organized, choosing fonts that stand out and implement an animation when the page is loading. 
