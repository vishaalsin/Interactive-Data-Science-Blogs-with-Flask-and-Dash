import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from processing.polyFit import *
import matplotlib
matplotlib.use('TkAgg')


print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'https://cdn.jsdelivr.net/gh/lwileczek/Dash@master/v5.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True      #otherwise dash thinks we are doing something wrong during mudular callback

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    html.Div(id='output-graph'),
])


#graph1 layout
graph1 = html.Div([
    html.Div(children='''No. of points:'''),
    dcc.Input(id='numPoints', value=25, type='number'),
    html.Div(children='''degree of polynomial to generate data:'''),
    dcc.Input(id='genDeg', value=2, type='number'),
    html.Div(id='output-graph1'),
])

#graph1 callback

@app.callback(
    Output(component_id='output-graph1', component_property='children'),
    [Input(component_id='numPoints', component_property='value'),
     Input(component_id='genDeg', component_property='value')]
)

def update_graph1(numPoints,genDeg):
    x, xCalm, y, yCalm = setup(genDeg, numPoints)
    return dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': xCalm, 'y': yCalm, 'mode': 'lines+markers', 'name': "data without noise"},
                    {'x': x, 'y': y, 'mode': 'markers', 'name': "data with noise", 'marker':{'color':'red'}}

                ],
            },
        config = {
            'displayModeBar': False
        }
        )


#graph2 layout
graph2 = html.Div([
    html.Div(children='''No. of points:'''),
    dcc.Input(id='numPoints', value=25, type='number'),
    html.Div(children='''degree of polynomial to generate data:'''),
    dcc.Input(id='genDeg', value=2, type='number'),
    html.Div(children='''degree of polynomials to fit:'''),
    dcc.Input(id='fitDeg', value='2,3', type='text'),
    html.Div(id='output-graph2'),
])

#graph2 callback

@app.callback(
    Output(component_id='output-graph2', component_property='children'),
    [Input(component_id='numPoints', component_property='value'),
     Input(component_id='genDeg', component_property='value'),
     Input(component_id='fitDeg', component_property='value')]
)


def update_graph2(numPoints,genDeg, fitDeg):
    x, xCalm, y, yCalm = setup(genDeg, numPoints)
    i = -1
    data = [
        {'x': x, 'y': y, 'mode': 'markers', 'name': "data with noise", 'marker':{'color':'red'}},
    ]
    for deg in fitDeg.split(','):
        i+=1
        if deg.isdigit():
         fit, lin, poly = fitPoly(x, y, int(deg))
         ein,eout, x_out, y_out, yPred_out = predictOut(lin,poly,fit,y,int(deg))
         data.append({'x': x, 'y': fit, 'type': 'line', 'name': 'degree: {} Ein = {}'.format(str(deg),ein)})
         # data.append({'x': x_out, 'y': y_out, 'mode': 'markers', 'name': 'original extension : degree: {} '.format(str(deg))})
         data.append({'x': x_out, 'y': yPred_out, 'type': 'line', 'name': 'degree: {} Eout = {} '.format(str(deg),eout)})

    return  dcc.Graph(
        id='example-graph',
        figure={
            'data': data,
        },
        config = {
            'displayModeBar': False
        }
    )

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [dash.dependencies.Input('url', 'pathname')]
)

def render(pathname):
    if pathname=="/":
        return graph1
    if pathname == "/1":
        return graph2
    return "INVALID URL"


def setup(genDeg, numPoints):
    np.random.seed(0)
    if (numPoints == 0):
        numPoints = 2
    noise = np.random.randn(numPoints)
    xCalm, eta, yCalm = getPoints(numPoints, 0, genDeg, noise)
    x, eta, y = getPoints(numPoints, 1, genDeg, noise)
    return x, xCalm, y, yCalm

if __name__ == '__main__':
    app.run_server(debug=False)