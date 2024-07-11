import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output #Key for call backs
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('gapminderDataFiveYear.csv')

app = dash.Dash()

#Option picker variable creation list
year_options=[]
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})

# create layout

app.layout = html.Div([
                dcc.Graph(id='myGraph'),
                dcc.Dropdown(id='yearPicker',options=year_options, value=df['year'].min())
            ])

@app.callback(Output('myGraph','figure'),
              [Input('yearPicker','value')])
def update_figure(selected_year):
    # DATA ONLY FOR SELECTED YEAR FROM DROP DOWN creation
    filtered_df = df[df['year']==selected_year]

    trace = []
    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent']==continent_name]
        trace.append(go.Scatter(
            x = df_by_continent['gdpPercap'],
            y = df_by_continent['lifeExp'],
            mode='markers',
            opacity=0.7,
            marker={'size':15},
            name=continent_name
    ))

    outPlot = {'data':trace,
            'layout':go.Layout(title='My Plot',
                               xaxis={'title':'GDP Per Cap','type':'log'},
                               yaxis={'title':'Life ExPectancy'})}

    return outPlot


if __name__=='__main__':
    app.run_server()
#something



    