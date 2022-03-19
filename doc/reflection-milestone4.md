# Reflection for Milestone 4

Group 20: Amelia Tang, Alex Yinan Guo, Maeve Yike Shi, Mahmood Rahman

The goal for this final milestone is to reproduce the same dashboard we built in `Python` in `R` and address feedback from the peer review and the TAs. We did not receive the TA feedback earlier in the week, so we did not have a chance to incorporate them, but we definitely will include these in our future improvements.

### Has it been easy to use your app?  

- From the peer feedback, in general, our dashboards are easy and intuitive to use and does not require long loading time. 
- The user can use this dashboard interactively leveraging the drop down menus on the sidebar. 
- To improve the user experience, we might consider some re-design for the drop down menus to show the numbers of top publishers and top genres are under the graph and might not be very obvious to users. 

### What differences are there between the DashR and DashPy app?

In general, we were able to implement all the features and plots we originally planned for the dashboards in both R and Python. We used `ggplot` package is case of `R` to make the plots, whereas we used `altair` and `plotly` to make the plots in python. We used `faviscon` to make logo showing up in the python dashboard, where we did not make logo for R dashboard. In both the dashboards we used `bootstrap` of `dash` to build the sidebar. In `R` dashboard, our plots at the bottom are arranged as 4x4 tiles and the layout is slightly different from the `Python` dashboard, mainly to make the plots look organized based on their shapes. Furthermore, the deployment time on Heroku was much shorter with `Python` than `R`. The `R` dashboard seemed to load a bit faster than the `Python` one. 


### Are there reoccurring themes in your feedback on what is good and what can be improved?

There are re-occurring feedback on the organizations of the charts as well as providing more information about the dashboard, so we include a collapse button to provide more information and re-organized our plots. 

### Is there any feedback (or other insight) that you have found particularly valuable during your dashboard development?

#### Feedback from Group 19
- `Inclusion of user scores plot`: We decided to include the a user score plot for both R and Python to make the dashboard more informative (Commit IDs: R [20b50b4](https://github.com/UBC-MDS/video_game_sales_dashboard_R/commit/20d50b4a032d7236839a1f63211a59621bdfae23), Python [a8daf7c](https://github.com/UBC-MDS/video_game_sales_dashboard/commit/a8daf7ce887962aaac13227271728e56c6ba0e35) )

#### General feedback 
- `Minimal explanation of the app`: we created a collapse button to explain the dashboard and also included a link to the github repo (commit IDs: R [7070ec1](https://github.com/UBC-MDS/video_game_sales_dashboard_R/commit/7070ec168d110829ffd22f651646d4541563003b)  Python [ffa87eb](https://github.com/UBC-MDS/video_game_sales_dashboard/commit/ffa87eb88269e5cd5f386a4860c4d9c04cd932e5))
- `Re-organized the charts`: We re-organized the charts so they look more organized and we also added a dividing line
 - `Added Regions to plot titles`: Commits IDs: Python  [01b54b1](https://github.com/UBC-MDS/video_game_sales_dashboard/commit/01b54b113672d2ae1c9ed0a152a5a0b8e8d13a25) R: [20d50b4](https://github.com/UBC-MDS/video_game_sales_dashboard_R/commit/20d50b4a032d7236839a1f63211a59621bdfae23)
 - `Edited the axis labels` to make them more descriptive: Commits IDs: Python [07f90e](https://github.com/UBC-MDS/video_game_sales_dashboard/commit/07f90e31400c7b0d85bef529b7780ab75d813266) R [20d50b4](https://github.com/UBC-MDS/video_game_sales_dashboard_R/commit/20d50b4a032d7236839a1f63211a59621bdfae23) 
 - `Added a scollbar for the sidebar`: the dashboards should be functional on a full screen and our original sidebar is fixed and cannot scroll down so some information will be missed ona  fill screen. (Commit IDs Python [66c1f89](https://github.com/UBC-MDS/video_game_sales_dashboard/commit/66c1f8905cd6144cd21fc608fde70cba337866af) R [6d2c39f](https://github.com/UBC-MDS/video_game_sales_dashboard_R/commit/6d2c39f6bcb0d9d358a708039925053db729cf48))

#### Improvements based on new materials in the lecture notes
- `Adding a loading feature` (from Lecture 3 optional reading): We added a loading feature for the `Python` dashboard because it seems take a bit longer time to load than `R`. (Commit ID: Python [58af58d](https://github.com/UBC-MDS/video_game_sales_dashboard/commit/58af58d806ef5470c9cf9fde4f5b9cbfcb9a56ed)) 


### Strength of the Dashboard

Our dashboard presents a comprehensive and primary descriptive analysis on some of the most important variables for a sales analyst of a video game company. The app is very easy to use with filtering criteria and simple visualizations. The large buttons and straight-forward clean layout avoid condensation of elements in the dashboard. Another advantage is, due to simplicity the app is less resource-hungry and visualizations are snappy which prevents fatigue and makes the experience pleasant and satisfying.

### Limitation of the Dashboard / Future improvements 
-  Information on how reactivity works: Although our plots are mostly self-explanatory, but adding information will help audiences to be more compatible.
- On the year range-selector for the sales trend according to companies, adding text "Select a year range": We believe the slider is self-explanatory, but it is a nice suggestion
 - A difference in screen size, it was a bit difficult to see all the plots in the dashboard at once: We optimized the dashboard to be viewed in a laptop screen in `Full view` mode, as instructed by the instructions of milestone 4.
 - For the Sales trend plot, the x-axis slider with two knobs to select the minimum and maximum years: We designed to use the dashboard to visualize the change over the years in comparison to year 2013.
 - Visualize genres associated with the least sales: We plotted the most popular genres, but yes, inclusion of least popular genres would have given more information.
 - Inclusion of  time-series plot with stats such as mean and standard deviation: Our dashboard summaries the frequencies at a high level. But inclusion of time-series plots along with statistical summaries will provide more information.
 - Inclusion of more regions in `Tab` such as Europe and Japan: Through our dashboard we tried to summarize the findings on a global scale Vs North American stats. But definitely adding more regions will make this dashboard useful to other audiences as well.
- Improve the documentations of the script based on the TA feedback

