from dash import Dash 
from dash_html_components import Div, H1, P
from dash_core_components import Graph 

external_stylesheets = [

]


app = Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = Div (
    children=[
    H1("Olá mundo"),
    P("Bem vindo ao dash"),
    Graph(
        figure={
            'data': [
                {'y': [1, 2, 3, 4],
                 'y': [1, 2, 3, 4],
                 'type': 'line'
                 }
            ]
        }
    )
    ]
    )

app.run_server(debug=True)