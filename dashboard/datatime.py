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

# Create a figure
fig = go.Figure()

# Add trace for Registered users
fig.add_trace(go.Scatter(x=dfd.index, y=dfd['Registered'], mode='lines', name='Registered',marker_color='#636EFA',))

# Add trace for Casual users
fig.add_trace(go.Scatter(x=dfd.index, y=dfd['Casual'], mode='lines', name='Casual',marker_color='#EF553B',))

# Update layout
fig.update_layout(
    width=1000,  # Set the width of the plot
    height=600,  # Set the height of the plot
    title='Registered and Casual Over Time',
    xaxis_title='Datetime',
    yaxis_title='Count'
)

fig.show()