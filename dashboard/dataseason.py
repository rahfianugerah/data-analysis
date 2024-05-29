import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

dfh = pd.read_csv("data/hour.csv")
dfd = pd.read_csv("data/day.csv")

# Renaming all the column
dfd.rename(columns={'yr':'year',
                    'mnth':'month',
                    'hum':'humidity',
                    'cnt':'count',
                    'dteday':'Datetime'
                    }, inplace=True)

# Capitalize each column name
dfd.columns = dfd.columns.str.title()

# Change the 'Datetime' data type from object to datetime
dfd['Datetime'] = pd.to_datetime(dfd['Datetime'])
dfd.set_index('Datetime', inplace=True)

# Renaming all the column
dfh.rename(columns={'yr':'year',
                    'mnth':'month',
                    'hum':'humidity',
                    'cnt':'count',
                    'dteday':'Datetime',
                    'hr':'Hour'
                    }, inplace=True)

# Capitalize each column name
dfh.columns = dfh.columns.str.title()


# Distribution Figure
fig = go.Figure()
fig.update_layout(title='Distribution of Seasons',
                  xaxis_title='Season',
                  yaxis_title='Count')

# Correlation Figure
fig.add_trace(go.Bar(
    x=['Spring', 'Summer', 'Fall', 'Winter'],
    y=dfd.groupby('Season')['Registered'].mean(),
    name='Registered Users',
    marker_color='#EF553B',
    width=0.5
))

fig.add_trace(go.Bar(
    x=['Spring', 'Summer', 'Fall', 'Winter'],
    y=dfd.groupby('Season')['Casual'].mean(),
    name='Casual Users',
    marker_color='#636EFA',
    width=0.5
))

fig.update_layout(
    barmode='group',
    width=1000,  # Set the width of the plot
    height=600,  # Set the height of the plot
    title='Registered and Casual Users (Seasons)',
    xaxis_title='Season',
    yaxis_title='Users Count')

fig.show()