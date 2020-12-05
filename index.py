#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:32:40 2020

@author: dan
"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from pages import page1, page2, page3, page4

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# CSS
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "19rem",
    "padding": "2rem 1rem",
    "background-color": "#BCF",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


# Navbar
sidebar = html.Div(
    [
        html.H2("Dashboard", className="display-4"),
        html.H4("TimesData", className="display-6"),
        html.Hr(),
        html.P(
            "Affichage du set de données du Times : Années 2016", className="lead"
        ),
        html.P(
            "Menu"
            ),
        dbc.Nav(
            [
                dbc.NavLink("Question 1", href="/page1", id="page1-link"),
                dbc.NavLink("Question 2", href="/page2", id="page2-link"),
                dbc.NavLink("Test 3", href="/page3", id="page3-link"),
                dbc.NavLink("Test 4", href="/page4", id="page4-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on

@app.callback(
    [Output(f"page{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page{i}" for i in range(1, 4)]

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page1"]:
        return page1.layout
    elif pathname == "/page2":
        return page2.layout
    elif pathname == "/page3":
        return page3.layout
    elif pathname == "/page4":
        return page4.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    app.run_server(port=8888, debug=True)