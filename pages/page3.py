import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html

from plotly.subplots import make_subplots
from app import app
from dash.dependencies import Input, Output


df = pd.read_csv('./datasets/timesData.csv')

years = df.year.unique()
fig = make_subplots(rows=3, cols=2, start_cell="bottom-left",shared_xaxes=True, shared_yaxes=True)
xy = [(1,1), (1,2), (2,1), (2,2), (3,1), (3,2) ]
for i in range(len(years)):
    dfy=df.loc[df.year == years[i]]
    fig.add_trace(go.Scatter(x=dfy.income, y=dfy.international, mode='markers', name=str(years[i]))
              ,row=xy[i][0], col=xy[i][1])

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

layout = html.Div(children=[
    html.Div(children=[
        html.H1(
            children='Dash Test',
            style={
                'textAlign': 'center',
                }
            )
        ]),

    dcc.Graph(
        id='example-graph-3',
        figure=fig
        )
    ])

@app.callback(
    Output('page3-display-value', 'children'),
    Input('page3-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)