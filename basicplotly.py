import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

#Setup Data
np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

#Setting up the data
data = [go.Scatter(x=random_x,
                   y=random_y, 
                   mode='markers',
                   marker=dict(
                       size=10,
                       color='rgb(51,403,203)',
                       symbol='pentagon',
                       line={'width':3}
                   ))]

#Setting up the layout of the graph
layout = go.Layout(title='Hello First Plot',
                   xaxis= {'title':'My X-axis'},
                   yaxis=dict(title='My Y-axis'),
                   hovermode='closest')

#fig object
fig = go.Figure(data=data,layout=layout)

#plot fig object
pyo.plot(fig,filename='scatter.html')

