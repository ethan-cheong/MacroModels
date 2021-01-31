import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import models

# To fix - graph initialization - initialize margins (smaller) and axis labels properly!

# Maybe plot the graph over a diff colour
# Reset button to clear the graph
# Pause button to pause plotting

model_options=['Solow Growth Model']

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("Macro Models"),
        html.P([
            'Implementation of some basic macroeconomic models in Python. Code available at ',
            html.A('github.com/ethan-cheong/MacroModels/', href='https://github.com/ethan-cheong/MacroModels/')
            ],id='description'),
    ], id='header' # Header bar that spans screen
    ),
    html.Div([
        html.Div([
            html.Div([
                html.P(
                    'Select model: ',
                    id='select-model-text'
                ),
                dcc.Dropdown(
                    id='model-dropdown',
                    options=[
                        {'label': model, 'value': model} for model in model_options
                    ],
                    value=model_options[0]
                ),
            ], id='model-select-div'),
            html.Div(id='model-options-div'),
        ],
        id='left-column',
        style={'display': 'inline-block', 'width': '30%', 'height': '100%'}),

        html.Div([
            html.Div(id='visualizations-div', style={'width':'100%', 'height':'100%'})
        ],
        id='right-column',
        style={'display': 'inline-block','float': 'right',
               'width': '65%', 'height':'100%'})

    ], id='container', style={'height':'600px'}),

])

@app.callback(
    Output('model-options-div', 'children'),
    Output('visualizations-div', 'children'),
    Input('model-dropdown', 'value')
)
def change_model_options(model):
    if model == 'Solow Growth Model':
        layout = [
            html.Div([
                html.P(
                    'Enter values for N and K: ',
                    id='population-capital-input-text'
                ),
                dcc.Input(
                    id='population-input',
                    type='number',
                    placeholder='N (starting population)',
                    value=1000
                ),
                dcc.Input(
                    id='capital-input',
                    type='number',
                    placeholder='K (starting capital)',
                    value=1000
                ),
            ], id='N-K-div'),
            html.Div([
                html.P(
                    'Population growth rate (n):',
                    id='n-slider-text'),
                dcc.Slider(
                    id='n-slider',
                    min=0,
                    max=1,
                    value=0.05,
                    marks={d:str(d) for d in [i/10 for i in range(0, 10)]},
                    step=0.01
                ),
            ], id='n-div'),
            html.Div([
                html.P(
                    'Savings rate (s):',
                    id='s-slider-text'),
                dcc.Slider(
                    id='s-slider',
                    min=0,
                    max=0.99,
                    value=0.25,
                    marks={d:str(d) for d in [i/10 for i in range(0, 10)]},
                    step=0.01
                ),
            ], id='s-div'),
            html.Div([
                html.P(
                    'Depreciation rate (d):',
                    id='d-slider-text'),
                dcc.Slider(
                    id='d-slider',
                    min=0.01,
                    max=0.99,
                    value=0.1,
                    marks={d:str(d) for d in [i/10 for i in range(0, 10)]},
                    step=0.01
                ),
            ], id='d-div'),
            html.Div([
                html.P(
                    'Labour share of output (alpha):',
                    id='alpha-slider-text'),
                dcc.Slider(
                    id='alpha-slider',
                    min=0.01,
                    max=0.99,
                    value=0.5,
                    marks={d:str(d) for d in [i/10 for i in range(0, 10)]},
                    step=0.01
                ),
            ], id='alpha-div'),
            html.Div([
                html.P(
                    'Productivity (z):',
                    id='productivity-text'),
                dcc.Input(
                    id='productivity-input',
                    type='number',
                    placeholder='z (Productivity)',
                    value=1
                ),
            ], id='z-div'),
            #html.Div([
            #    html.Button(
            #        'Start',
            #        id='start-button',
            #        n_clicks=0
            #    ),
            #    html.Button(
            #        'Reset',
            #        id='reset-button',
            #        n_clicks=0
            #    )
            #], id='button-div')
        ]
        visualization = [
            dcc.Graph(id='graph', style={'width':'100%', 'height':'100%'})
        ]
        return (layout, visualization)

@app.callback(
    Output('graph', 'figure'),
    Input('population-input', 'value'),
    Input('capital-input', 'value'),
    Input('n-slider', 'value'),
    Input('s-slider', 'value'),
    Input('d-slider', 'value'),
    Input('alpha-slider', 'value'),
    Input('productivity-input', 'value'),
)
def update_graph(N, K, n, s, d, alpha, z):
    model = models.SolowGrowth(N, K, n, s, d, z, alpha)
    N_list = [model.N]
    K_list = [model.K]
    k_list = [model.k]
    C_list = [model.C]
    SI_list = [model.S]
    Y_list = [model.Y]
    for i in range(99):
        model.increment()
        N_list.append(model.N)
        K_list.append(model.K)
        k_list.append(model.k)
        C_list.append(model.C)
        SI_list.append(model.S)
        Y_list.append(model.Y)

    fig = make_subplots(rows=2, cols=3, shared_xaxes=True,
    vertical_spacing=0.05,
    subplot_titles=('N (Total Population) against Time','K (Total Capital) against Time','k (Capital to Labour Ratio) against Time','C (Total Consumption) against Time','S/I (Total Savings/Investment) against Time','Y (Total Income) against Time'))

    fig.add_trace(
        go.Scatter(x=[i for i in range(100)], y=N_list),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=[i for i in range(100)], y=K_list),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=[i for i in range(100)], y=k_list),
        row=1, col=3
    )
    fig.add_trace(
        go.Scatter(x=[i for i in range(100)], y=C_list),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=[i for i in range(100)], y=SI_list),
        row=2, col=2
    )
    fig.add_trace(
        go.Scatter(x=[i for i in range(100)], y=Y_list),
        row=2, col=3
    )
    fig.update_layout(showlegend=False, margin=dict(r=10, l=10, t=20, b=10))
    return fig


if __name__ == "__main__":
    app.run_server(debug=False)