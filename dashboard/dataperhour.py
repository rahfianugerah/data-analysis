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

sumhours = dfh.groupby("Hour").Count.sum().sort_values(ascending=False).reset_index()

# Data for the most bike rentals
most_rentals = sumhours.head(5)
least_rentals = sumhours.sort_values(by="Hour", ascending=True).head(5)

# Create subplot with 1 row and 2 columns
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Hours with Most Bike Rentals", "Hours with Fewest Bike Rentals")
)

# Add bar chart for the most bike rentals
fig.add_trace(
    go.Bar(
        x=most_rentals["Hour"],
        y=most_rentals["Count"],
        marker_color="#EF553B",  # Set color
        showlegend=False  # Hide legend for the bar chart
    ),
    row=1, col=1
)

# Add bar chart for the fewest bike rentals
fig.add_trace(
    go.Bar(
        x=least_rentals["Hour"],
        y=least_rentals["Count"],
        marker_color="#636EFA",  # Set color
        showlegend=False  # Hide legend for the bar chart
    ),
    row=1, col=2
)

# Update layout for the figure
fig.update_layout(
    width=1000,
    height=600,
    title_text="Bike Rentals by Hour",
    template="plotly_white"
)

# Update x-axis and y-axis properties for both subplots
fig.update_xaxes(title_text="Hours (PM)", row=1, col=1, tickfont=dict(size=15))
fig.update_yaxes(tickfont=dict(size=15), row=1, col=1)

fig.update_xaxes(title_text="Hours (AM)", row=1, col=2, tickfont=dict(size=15))
fig.update_yaxes(tickfont=dict(size=15), row=1, col=2)

# Reverse x-axis for the second plot
fig['layout']['xaxis2']['autorange'] = 'reversed'