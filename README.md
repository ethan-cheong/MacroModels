# MacroModels
Macro models from EC102.

To-do:
1. Make graphs update by year (instead of all at once). Put in start, pause and reset buttons.
  1. Possible solution: https://stackoverflow.com/questions/63589249/plotly-dash-display-real-time-data-in-smooth-animation 
2. Add in graphs for per-worker variables (from week 2 live session)
3. Add in option for growth rate of z (default set to 0)
4. Add in box containing selected model information + currently set parameters (need a callback to update this)
5. Change colour scheme

## models.py
Contains the following models:
* Solow Growth Model

## app.py
Dash front-end. App is currently hosted on heroku

