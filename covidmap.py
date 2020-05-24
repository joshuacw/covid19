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
covid_cases = pd.read_csv('time_series_covid_19_confirmed_US.csv')

start_date = datetime.date(2020, 1, 22)

def days_from_start(days):
    """Days from start date of 1/22/20."""
    return (start_date + datetime.timedelta(days=days))\
            .strftime('%-m/%-d/%y')

def state_date_death_count(state, date):
    """Returns death count by state + date."""
    return sum(covid_deaths.loc[covid_deaths["Province_State"] == state, date])

def state_date_case_count(state, date):
    """Returns case count by state + date."""
    return sum(covid_cases.loc[covid_cases["Province_State"] == state, date])

state_cases = {}
state_deaths = {}

for n in range(50):
    state_deaths[state_codes[n]] = state_date_death_count(states[n], days_from_start(119))

for n in range(50):
    state_cases[state_codes[n]] = state_date_case_count(states[n], days_from_start(119))

data_cases = dict(type='choropleth',
    locations=tuple(state_cases.keys()),
    z = tuple(state_cases.values()),
    locationmode = 'USA-states',
    colorscale = [
            [0, 'rgb(255, 233, 229)'],
            [0.01, 'rgb(225, 233, 229)'],

            [0.01, 'rgb(255, 175, 161)'],
            [0.05, 'rgb(255, 175, 161)'],

            [0.05, 'rgb(255, 116, 92)'],
            [0.1, 'rgb(255, 116, 92)'],

            [0.1, 'rgb(255, 58, 23)'],
            [0.5, 'rgb(255, 58, 23)'],

            [0.5, 'rgb(154, 25, 3)'],
            [1.0, 'rgb(154, 25, 3)'],
            ],
    colorbar = dict(title="Cases", len=0.5, y=0.8,
                    tickvals=[1,3000,7500,30000,75000],
                    ticktext=["0 - 1000",
                              "1000 - 5000",
                              "5000 - 10000",
                              "10000 - 50000",
                              " > 50000"],
                    ),
    zmax = 100000,
    zmid = 50000,
    zmin = 0,
    geo = 'geo2',
    )

data_deaths = dict(type='choropleth',
    locations=tuple(state_deaths.keys()),
    z = tuple(state_deaths.values()),
    locationmode = 'USA-states',
    colorscale = [
            [0, 'rgb(230, 230, 230)'],
            [0.01, 'rgb(230, 230, 230)'],

            [0.01, 'rgb(204, 204, 204)'],
            [0.05, 'rgb(204, 204, 204)'],

            [0.05, 'rgb(153, 153, 153)'],
            [0.1, 'rgb(153, 153, 153)'],

            [0.1, 'rgb(102, 102, 102)'],
            [0.5, 'rgb(102, 102, 102)'],

            [0.5, 'rgb(51, 51, 51)'],
            [1.0, 'rgb(51, 51, 51)'],
            ],
    colorbar = dict(title = "Deaths", len=0.5, y = 0.2,
                    tickvals=[1,300,750,3000, 7500],
                    ticktext=["0 - 100",
                              "100 - 500",
                              "500 - 1000",
                              "1000 - 5000",
                              " > 5000"],
                    ),
    zmax = 10000,
    zmid = 5000,
    zmin = 0,
    geo = 'geo',
    )

layout = dict(title_text="Covid-19 in the U.S.", height=800)
layout['geo'] = dict(scope='usa', domain = dict(x = [0, 1.0], y = [0, 0.5]))
layout['geo2'] = dict(scope='usa', domain = dict(x = [0, 1.0], y = [0.5, 1.0]))

fig = go.Figure(data=[data_cases, data_deaths], layout=layout)
#fig.update_layout(title_text="Covid-19 in the U.S.")
fig.show()
