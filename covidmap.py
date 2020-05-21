#!/usr/bin/env python3

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

covid_deaths = pd.read_csv('time_series_covid_19_deaths_US.csv')
#alabama = covid_deaths.loc[covid_deaths["Province_State"] == "Alabama", "1/22/20":]
#alabama = covid_deaths.loc[covid_deaths["Province_State"] == "Alabama", "1/22/20"]

start_date = datetime.date(2020, 1, 22)
col_lab_start_date = start_date.strftime('%m/%d/%y').lstrip('0')

def days_from_start(days):
    """Days from start date of 1/22/20."""
    return (start_date + datetime.timedelta(days=days))\
            .strftime('%-m/%-d/%y')

def state_date_death_count(state, date):
    """Returns death count by state + date."""
    return sum(covid_deaths.loc[covid_deaths["Province_State"] == state, date])

for n in range(119):
    print(state_date_death_count("Washington", days_from_start(n)))
    time.sleep(.5)
