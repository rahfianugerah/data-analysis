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


# Assuming dfd is a DataFrame with 'Registered' and 'Casual' columns
registered_sum = dfd['Registered'].sum()
casual_sum = dfd['Casual'].sum()

# Create a subplot with 1 row and 2 columns, with the first column being the bar chart and the second column being the pie chart
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "bar"}, {"type": "pie"}]],
)

# Add bar chart to the first column
fig.add_trace(
    go.Bar(
        x=["Registered", "Casual"],
        y=[registered_sum, casual_sum],
        marker_color=["#EF553B", "#636EFA"],
        showlegend=False  # Hide legend for the bar chart
    ),
    row=1, col=1
)

# Add pie chart to the second column
fig.add_trace(
    go.Pie(
        labels=["Registered", "Casual"],
        values=[registered_sum, casual_sum],
        marker=dict(colors=["#EF553B", "#636EFA"]),
        showlegend=False  # Hide legend for the pie chart
    ),
    row=1, col=2
)

# Update layout for the figure
fig.update_layout(
    width=1000,  # Set the width of the plot
    height=600,  # Set the height of the plot
    title_text="Total and Proportional Rides by User Type",
    template="plotly_white"
)

# Show the plot
fig.show()

# Print the counts
print(f"Count of Registered Users: {registered_sum}")
print(f"Count of Casual Users: {casual_sum}")