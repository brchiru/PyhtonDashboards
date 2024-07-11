import dash
import dash_core_components as dcc
import dash_html_components as html

#Start the app
app = dash.Dash()


colors = {'background':'#11121','text':'#7FDBFF'}

app.layout = html.Div(children=[
                            html.H1('Hello Dash...!',
                                    style= {
                                                'textAlign':'center',
                                                'color':colors['text']
                                            }
                                    ),

                            dcc.Graph(id='example',
                                        figure={'data':
                                                        [
                                                            {'x':[1,2,3],'y':[4,2,1],'type':'bar','name':'SF'},
                                                            {'x':[1,2,3],'y':[3,2,5],'type':'bar','name':'NYC'}
                                                        ],
                            'layout':
                            {
                                'plot_bgcolor':colors['background'],
                                'paper_bgcolor':colors['background'],
                                'font':{'color':colors['text']},
                                'title':'BAR PLOTS!'
                            }})
                        ],  style={'backgroundColor':colors['background']}
)

if __name__== '__main__':
    app.run_server()
