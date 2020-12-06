#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:29:59 2020

@author: dan
"""

import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import dash_table
import plotly.graph_objs as go

from dash.dependencies import Input, Output
from plotly.subplots import make_subplots



from app import app

df = pd.read_csv('./datasets/timesData.csv')

df_2016 = df['year'] == 2016
df_2016 = df[df_2016].head(50)

df = pd.read_csv('./datasets/timesData.csv')

years = df.year.unique()
fig = make_subplots(rows=3, cols=2, start_cell="bottom-left",shared_xaxes=True, shared_yaxes=True)
xy = [(1,1), (1,2), (2,1), (2,2), (3,1), (3,2) ]
for i in range(len(years)):
    dfy=df.loc[df.year == 2016]
    fig.add_trace(go.Scatter(
        x=dfy.income, 
        y=dfy.international, 
        mode='markers', 
        name=str(years[i])),
        row=xy[i][0], 
        col=xy[i][1]
    )

fig.update_xaxes(title_text="income", row=1,col=2)   
fig.update_xaxes(title_text="income", row=1,col=1) 
fig.update_yaxes(title_text="international", row=2, col=1)
fig.update_layout(height=800, width=1200, title_text="Income in relation to international per year")

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])

layout = html.Div(
            children=[
                html.H1(
                    children='Dash Test',
                    style={'textAlign': 'center'}
                ),
                dcc.Graph(
                    id='example-graph-3',
                    figure=fig
                )
            ]
        )

@app.callback(
    Output("download", "data"), 
    [Input("btn", "n_clicks")])
def func(n_nlicks):
    return send_data_frame(df_2016.to_csv, "export.csv", index=False)

@app.callback(
    Output('page1-display-value', 'children'),
    Input('page1-dropdown', 'value')
    )
def display_value(value):
    return 'You have selected "{}"'.format(value)

