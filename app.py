#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 20:47:02 2022

This script generates a dashboard enabling the computation of Hedges' g for 
both between- and within-subject designs. 

@author: Franziska Usée
"""

# Run this app with `python app_effect_sizes.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output
import numpy as np 

app    = Dash(__name__)

server = app.server

app.layout = html.Div(children = [html.Div([
    
    # heading 
    html.H1(children = "Calculation of Effect Sizes",                   
            style    = {"textAlign" : "center", 
                        "color"     : "navy",
                        "fontSize"  : "30px", 
                        "fontWeight": "bold"}),
    
    html.Br(),                                                                  # line break
    
    # text component 
    html.Div([html.P("Please select the type of experimental design and test statistic.")],
             style    = {"textAlign" : "left", 
                         "color"     : "navy",
                         "fontSize"  : "20px"}),
    
    html.Br(),
    
    # first dropdown menu
    html.Div([html.Label(["Type of experimental design:"],                      
                         style = {"fontWeight" : "bold"}),
              dcc.Dropdown(id      = "design",                             
                           options = ["Between", "Within"], 
                           value   = "Between",
                           style   = {"backgroundColor": "whitesmoke"})],
              style = {"width"      : "45%",
                       "display"    : "inline-block",
                       "textAlign"  : "center", 
                       "marginLeft" : "15px",
                       "fontSize"   : "16px",
                       "color"      : "black"}),

    # second dropdown menu
    html.Div([html.Label(["Type of test statistic:"],
                         style = {"fontWeight" : "bold"}),
              dcc.Dropdown(id      = "statistic",
                           options = ["t", "F", "Mean/Std"], 
                           value   = "t",
                           style   = {"backgroundColor": "whitesmoke"})],
              style = {"width"      : "45%",
                       "display"    : "inline-block",
                       "textAlign"  : "center", 
                       "marginLeft" : "15px",
                       "fontSize"   : "16px",
                       "color"      : "black"}),
    
    html.Br(),
    html.Br(),
    html.Br(),
    
    # text component
    html.Div([html.P("As far as possible, please provide the following information. Note that depending on the type of test statistic, not all information is required.")],
             style    = {"textAlign" : "left", 
                         "color"     : "navy",
                         "fontSize"  : "20px"}),
    
    # input component: numeric value 
    html.Div([html.Label(["Value of test statistic:"],
                         style = {"fontWeight" : "bold"}),
              html.Br(),
              dcc.Input(id    = "stat_value",
                        type  = "number",
                        value = 1,
                        style = {"backgroundColor": "whitesmoke",
                                 "textAlign"      : "center",
                                 "width"          : "100%"})],
              style = {"width"      : "25%",
                       "display"    : "inline-block",
                       "textAlign"  : "center", 
                       "marginLeft" : "60px",
                       "fontSize"   : "16px",
                       "color"      : "black"}),
    
    html.Div([html.Label(["Sample mean of experimental group:"],
                         style = {"fontWeight" : "bold"}),
              html.Br(),
              dcc.Input(id    = "mean_e",
                        type  = "number",
                        value = 0,
                        style = {"backgroundColor": "whitesmoke",
                                 "textAlign"      : "center",
                                 "width"          : "100%"})],
              style = {"width"      : "25%",
                       "display"    : "inline-block",
                       "textAlign"  : "center", 
                       "marginLeft" : "60px",
                       "fontSize"   : "16px",
                       "color"      : "black"}),
    
    html.Div([html.Label(["Sample mean of control group:"],
                         style = {"fontWeight" : "bold"}),
              html.Br(),
              dcc.Input(id    = "mean_c",
                        type  = "number",
                        value = 0,
                        style = {"backgroundColor": "whitesmoke",
                                 "textAlign"      : "center",
                                 "width"          : "100%"})],
              style = {"width"      : "25%",
                       "display"    : "inline-block",
                       "textAlign"  : "center", 
                       "marginLeft" : "60px",
                       "fontSize"   : "16px",
                       "color"      : "black"}),
    
    html.Br(),
    html.Br(),
    html.Div([html.Label(["Sample standard deviation of experimental group:"],
                         style = {"fontWeight" : "bold"}),
              dcc.Input(id    = "std_e",
                        type  = "number",
                        value = 0,
                        style = {"backgroundColor": "whitesmoke",
                                 "textAlign"      : "center",
                                 "width"          : "100%"})],
              style = {"width"      : "25%",
                       "display"    : "inline-block",
                       "textAlign"  : "center", 
                       "marginLeft" : "60px",
                       "fontSize"   : "16px",
                       "color"      : "black"}),
    
    html.Div([html.Label(["Sample standard deviation of control group:"],
                         style = {"fontWeight" : "bold"}),
              dcc.Input(id    = "std_c",
                        type  = "number",
                        value = 0,
                        style = {"backgroundColor": "whitesmoke",
                                 "textAlign"      : "center",
                                 "width"          : "100%"})],
              style = {"width"      : "25%",
                       "display"    : "inline-block",
                       "textAlign"  : "center", 
                       "marginLeft" : "60px",
                       "fontSize"   : "16px",
                       "color"      : "black"}),
    
    html.Br(),
    html.Br(),
    html.Div([html.Label(["Sample size of experimental group:"],
                         style = {"fontWeight" : "bold"}),
              dcc.Input(id    = "n_e",
                        type  = "number",
                        value = 10,
                        style = {"backgroundColor": "whitesmoke",
                                 "textAlign"      : "center",
                                 "width"          : "100%"})],
              style = {"width"      : "25%",
                       "display"    : "inline-block",
                       "textAlign"  : "center", 
                       "marginLeft" : "60px",
                       "fontSize"   : "16px",
                       "color"      : "black"}),
    
    html.Div([html.Label(["Sample size of control group:"],
                         style = {"fontWeight" : "bold"}),
              dcc.Input(id    = "n_c",
                        type  = "number",
                        value = 10,
                        style = {"backgroundColor": "whitesmoke",
                                 "textAlign"      : "center",
                                 "width"          : "100%"})],
              style = {"width"      : "25%",
                       "display"    : "inline-block",
                       "textAlign"  : "center", 
                       "marginLeft" : "60px",
                       "fontSize"   : "16px",
                       "color"      : "black"}),
    
    html.Div([html.Label(["Total sample size:"],
                         style = {"fontWeight" : "bold"}),
              dcc.Input(id    = "n",
                        type  = "number",
                        value = 20,
                        style = {"backgroundColor": "whitesmoke",
                                 "textAlign"      : "center",
                                 "width"          : "100%"})],
              style = {"width"      : "25%",
                       "display"    : "inline-block",
                       "textAlign"  : "center", 
                       "marginLeft" : "60px",
                       "fontSize"   : "16px",
                       "color"      : "black"}),
    
    ]),
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div([html.P("Hedges` g:")],
             style    = {"textAlign" : "center", 
                         "color"     : "navy",
                         "fontSize"  : "20px",
                         "fontWeight": "bold"}),
    
    # result table 
    html.Table([
        html.Tr([html.Td(["g = "]), html.Td(id = "g")]),
        html.Tr([html.Td(["g", html.Sup("*"), "="]), html.Td(id = "g_star")]),
        ],
        style = {"backgroundColor": "whitesmoke",
                 "textAlign"      : "center",
                 "marginLeft"     : "Auto",
                 "marginRight"    : "Auto",
                 "fontSize"       : "20px"}),
    
    ])

@app.callback(Output("g", "children"),
              Output("g_star", "children"),
              Input("design", "value"),
              Input("statistic", "value"), 
              Input("stat_value", "value"),
              Input("mean_e", "value"),
              Input("mean_c", "value"),
              Input("std_e", "value"),
              Input("std_c", "value"),
              Input("n_e", "value"),
              Input("n_c", "value"),
              Input("n", "value"),
              )                  
    
def compute_g(design, statistic, stat_value, mean_e, mean_c, std_e, std_c, n_e, 
              n_c, n):
    
    """
    This function computes Hedges' g for both between- and within-subject 
    designs. Test statistics may be t-, F-, sample mean, and standard deviation 
    values. 
    
    Inputs:
        design    : type of experimental design,
                    possible values: 'Between', 'Within'
        statistic : type of test statistic,
                    possible values: 't', 'F', 'Mean/Std'
        stat_value: value of test statistic (integer)
        mean_e    : sample mean of experimental group (integer)
        mean_c    : sample mean of control group (integer)
        std_e     : sample standard deviation of experimental group (integer)
        std_c     : sample standard deviation of control group (integer)
        n_e       : sample size of experimental group (integer)
        n_c       : sample size of control group (integer)
        n         : total sample size (integer)
        
    Output:     
        g         : Hedges' g
        g_star    : corrected Hedges' g
    
    """
    
    if design == "Between":
    
        if statistic == "t":
            g   = stat_value*np.sqrt((1/n_e)+(1/n_c))
            
        elif statistic == "F":
            g   = np.sqrt((stat_value*(n_e+n_c))/(n_e*n_c))
            
        elif statistic == "Mean/Std":
            s_p = np.sqrt(((n_e-1)*std_e**2)+((n_c-1)*std_c**2)/(n_e+n_c-2))
            g   = (mean_e-mean_c)/s_p
            
    else: 
        g = stat_value/np.sqrt(n)
    
    g_star = g*(1-(3/(4*(n_c+n_e)-9)))
    
    return g, g_star

if __name__ == "__main__":
    app.run_server(debug = False)
