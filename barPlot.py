import pandas as pd

import plotly.express as px

#readind data from csv files
df = pd.read_csv("data.csv")
fig = px.bar(df, x='Country', y='InternetUsers')
fig.show()