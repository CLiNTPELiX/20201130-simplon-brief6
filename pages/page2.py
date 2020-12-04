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

from dash.dependencies import Input, Output
import plotly.express as px

from app import app


layout = html.Div(
            style={'height': '130vh','color':'white', 'backgroundcolor':'black'},
            children=[
                html.Br(),
                html.Div("Coucou")  
            ])

@app.callback(
    Output('page1-display-value', 'children'),
    Input('page1-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)

# df = pd.read_csv('./datasets/timesData.csv')

# df_2016 = df['year'] == 2016
# df_2016 = df[df_2016].head(50)

# layout = html.Div([
#     html.H3('Page 2'),
#     dcc.Dropdown(
#         id='page2-dropdown',
#         options=[
#             {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
#                 'NYC', 'MTL', 'LA'
#             ]
#         ]
#     ),
#     html.Div(id='app-1-display-value'),
#     dcc.Link('Go to Page 3', href='/page3')
# ])

# layout = html.Div(
#             #style={'height': '130vh','color':'white','backgroundImage': 'url(../assets/pexels-jessica-lewis-583846.jpg)'},
#             children=[
#                 html.Br(),
#                 html.Div(
#                     className="app-header",
#                     children=[html.Div('Data Table',className="app-header--title")]),
#                         dash_table.DataTable(
#                             columns=[{'id': c, 'name': c} for c in df_2016.columns],
#                             data= df_2016.to_dict('records'),
#                             #Style table as list view
#                             #style_as_list_view=True,
#                             fixed_rows={'headers': True},
#                             fixed_columns={'headers': True, 'data' :1},
#                             style_table={
#                                         'maxHeight': '50ex',
#                                         'overflow': 'auto',
#                                         'width': '90%',
#                                         'minWidth': '90%',
#                                         'margin-left':'auto',
#                                         'margin-right':'auto',},
#                             #Cell dim + textpos
#                             style_cell_conditional=[{'height': 'auto',
#                                 # all three widths are needed
#                                 'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
#                                 'whiteSpace': 'normal','textAlign':'center'}],
#                             #Line strip
#                             style_cell={'color': 'black'},
#                             style_data_conditional=[{
#                                     'if': {'row_index': 'odd'},
#                                     'backgroundColor': 'rgb(248, 248, 248)'}],
#                             style_header={
#                                 'backgroundColor': 'rgb(50, 50, 50)',
#                                 'fontWeight': 'bold',
#                                 'color':'white'}),
#                 html.Br(),
#                 html.H1('Quel est la meilleure Université',style={'textAlign': 'center','font-family':'sans-serif'}),
#                 dbc.Button("Back to head ", color="primary", className="mr-1", href="/apps/app1"),
#                 html.Br(),
#                 html.Div([
#                 dbc.Button("Back to home", color="primary",href="/" ,id="loading-button"),
#                 dbc.Spinner(html.Div(id="loading-output"))
#                         ])
#                     ]
# )

# @app.callback(
#     Output("download", "data"), 
#     [Input("btn", "n_clicks")])
# def func(n_nlicks):
#     return send_data_frame(df_2016.to_csv, "export.csv", index=False)

