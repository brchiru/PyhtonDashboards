import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# Creating Data

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# app layout creation

app.layout = html.Div(
                    [
                    # Graph 1
                    dcc.Graph(id='scatterplot',
                                figure={
                                        'data':[
                                            go.Scatter(
                                                        x=random_x,
                                                        y=random_y,
                                                        mode='markers',
                                                        marker = {
                                                            'size':12,
                                                            'color':'rgb(50,200,300)',
                                                            'symbol':'triangle-up',
                                                            'line':{'width':2}
                                                        },
                                                        )
                                            ],
                                        'layout':go.Layout(title='My ScatterPlot',
                                                           xaxis= {'title':'Iam X-Axis'},
                                                            yaxis={'title':'Iam Y-Axis'}
                                                            )
                                        }
                    ),
                    #Graph 2
                    dcc.Graph(id='scatterplot2',
                                figure={
                                        'data':[
                                            go.Scatter(
                                                        x=random_x,
                                                        y=random_y,
                                                        mode='markers',
                                                        marker = {
                                                            'size':5,
                                                            'color':'rgb(50,200,300)',
                                                            'symbol':'pentagon',
                                                            'line':{'width':2}
                                                        },
                                                        )
                                            ],
                                        'layout':go.Layout(title='2nd ScatterPlot',
                                                           xaxis= {'title':'Iam 2nd graph X-Axis'},
                                                            yaxis={'title':'Iam 2nd graph Y-Axis'}
                                                            )
                                        }
                    )])

if __name__=='__main__':
    app.run_server()
