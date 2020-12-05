#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:29:59 2020

@author: dan
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

from dash.dependencies import Input, Output
from app import app

#####################################################
################# Pre treatment #####################
#####################################################

df = pd.read_csv("./datasets/timesData.csv")

df_2016 = df[df.year == 2016].iloc[:50,:]
df_2016 = df_2016.dropna()

df_2016.world_rank = [int(each.replace('=','')) for each in df_2016.world_rank]

df.world_rank = pd.to_numeric(df.world_rank, errors='coerce')
df.income = pd.to_numeric(df.income, errors='coerce')
df.international = pd.to_numeric(df.international, errors='coerce')
df.total_score = pd.to_numeric(df.total_score, errors='coerce')

df.num_students  = [str(each).replace(',','') for each in df.num_students]
df.num_students = pd.to_numeric(df.num_students, errors='coerce')

df_2016.international_students = [str(each).replace('%','') for each in df_2016.international_students]
#df_2016.rename(columns = {"international_students":"international_students_%"})

#df.international_students = pd.to_numeric(df.international_students, errors='coerce')

df_2016['female_male_ratio'] = [str(each).split() for each in df_2016.female_male_ratio]
df_2016.female_male_ratio = [(float(each[0]) / float(each[2])) for each in df_2016.female_male_ratio] 
df_2016.female_male_ratio = pd.to_numeric(df_2016.female_male_ratio, errors='coerce')
df_2016

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig = px.scatter(df, x='income', y='international', color='year', title='International score in terms of the income score per year' )

def generate_table(dataframe, max_rows=5):
    return html.Table([
                     html.Thead(
                                 html.Tr([html.Th(col) for col in dataframe.columns])
                                 ),
                     html.Tbody([
                                 html.Tr([
                                         html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                                         ]) for i in range(min(len(dataframe), max_rows))
                                 ])
                     ])

layout = html.Div([
    dbc.Button("Télécharger le CSV ", color="info", id="example-button", className="mr-2"),
    html.Span(
        id="example-output", 
        style={"vertical-align": "middle"}
    ),
    dbc.Table.from_dataframe(
        df_2016, 
        striped=True, 
        bordered=True, 
        hover=True, 
        dark=True, 
        responsive=True
    ),
#    ]),
html.Div(
    style={'backgroundColor': colors['background']}, 
    children=[
        html.H1(
        children='Test',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
        )
    ]
),
html.Div(style={'backgroundColor': colors['background']}, 
         children=html.Div(
             'Plot on dash',
             style={
                'textAlign': 'center',
                'color': colors['text']
            })
),
dcc.Graph(
    id='example-graph-2',
    figure=fig
)
])

@app.callback(
    Output("example-output", "children"), 
    Input("example-button", "n_clicks")
)
def on_button_click(n):
    if n is None:
        return "Not clicked."
    else:
        return f"Clicked {n} times."
    
@app.callback(
    Output('page2-display-value', 'children'),
    Input('page2-dropdown', 'value')
)
def display_value(value):
    return 'You have selected "{}"'.format(value)