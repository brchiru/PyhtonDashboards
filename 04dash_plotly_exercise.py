import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('OldFaithful.csv')

print(df.head(5))

# Launch the application

app = dash.Dash()

#Create a Dash Layout that contains a Graph Component

app.layout = html.Div([dcc.Graph(id='old_faithful',
                                  figure={'data':[go.Scatter(x=df['TimeEruption'],
                                                         y=df['TimeWaiting'],
                                                         mode='markers')],
                                                         
                                        'layout':go.Layout(title='Old Faithful Eruptions',
                                                         xaxis={'title':'TimeEruption'},
                                                         yaxis={'title':'TimeWaiting'})
                                        }
                                )
])

if __name__=='__main__':
    app.run_server()