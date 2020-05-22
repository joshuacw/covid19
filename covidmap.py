#!/usr/bin/env python3

import plotly.graph_objects as go
import pandas as pd
import datetime
import time

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

state_codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]



covid_deaths = pd.read_csv('time_series_covid_19_deaths_US.csv')
#alabama = covid_deaths.loc[covid_deaths["Province_State"] == "Alabama", "1/22/20":]
#alabama = covid_deaths.loc[covid_deaths["Province_State"] == "Alabama", "1/22/20"]

start_date = datetime.date(2020, 1, 22)

def days_from_start(days):
    """Days from start date of 1/22/20."""
    return (start_date + datetime.timedelta(days=days))\
            .strftime('%-m/%-d/%y')

def state_date_death_count(state, date):
    """Returns death count by state + date."""
    return sum(covid_deaths.loc[covid_deaths["Province_State"] == state, date])

state_deaths = {}

for n in range(50):
    state_deaths[state_codes[n]] = state_date_death_count(states[n], days_from_start(119))

fig = go.Figure(data=go.Choropleth(
    locations=tuple(state_deaths.keys()),
    z = tuple(state_deaths.values()),
    locationmode = 'USA-states',
    colorscale = [
            [0, 'rgb(204, 204, 204)'],
            [0.02, 'rgb(204, 204, 204)'],

            [0.02, 'rgb(153, 153, 153)'],
            [0.1, 'rgb(153, 153, 153)'],

            [0.1, 'rgb(102, 102, 102)'],
            [0.2, 'rgb(102, 102, 102)'],

            [0.2, 'rgb(51, 51, 51)'],
            [0.5, 'rgb(51, 51, 51)'],

            [0.5, 'rgb(0, 0, 0)'],
            [1.0, 'rgb(0, 0, 0)']
            ],
    colorbar_title = "Covid-19 deaths",
    zmax = 10000,
    zmid = 5000,
    zmin = 0
    ))

fig.update_layout(
    title_text = "Covid-19 deaths",
    geo_scope='usa',
    )

fig.show()
