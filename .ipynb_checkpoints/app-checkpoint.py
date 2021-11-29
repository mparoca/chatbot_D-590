import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

#from app import server
#from app import app

#Use if you want to change the style later or if you wanna make your own css
BS = "https://bootswatch.com/5/vapor/bootstrap.min.css"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
#CUSTOM_STYLE = "/assets/style.css"
external_stylesheets=[BS, FONT_AWESOME]

print("OK")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def textbox(text, box="other"):
    style = {
        "max-width": "55%",
        "width": "max-content",
        "padding": "10px 15px",
        "border-radius": "25px",
    }

    if box == "self":
        style["margin-left"] = "auto"
        style["margin-right"] = 0

        color = "primary"
        inverse = True

    elif box == "other":
        style["margin-left"] = 0
        style["margin-right"] = "auto"

        color = "light"
        inverse = False

    else:
        raise ValueError("Incorrect option for `box`.")

    return dbc.Card(text, style=style, body=True, color=color, inverse=inverse)

conversation = html.Div(
    style={
        "width": "80%",
        "max-width": "800px",
        "height": "70vh",
        "margin": "auto",
        "overflow-y": "auto",
    },
    id="display-conversation",
)

controls = dbc.InputGroup(
    style={"width": "80%", "max-width": "800px", "margin": "auto"},
    children=[
        dbc.Input(id="user-input", placeholder="Ask a Factual Question...", type="text"),
        dbc.InputGroup(dbc.Button("Submit", id="submit", color="success", outline=True)),
    ],
)



# Define Layout
app.layout = dbc.Container(
    fluid=True,
    children=[
        html.H1(["Topo's ", html.I(className="fab fa-wikipedia-w ml-0"),"iki-Bot ", html.I(className="fas fa-robot ml-0")]),
        html.H5("I am a knowledge-based question answering bot."),
        html.H5("Learn more about me below:"),
        dbc.Button(html.Span(["", html.I(className="fab fa-github ml-2")]), href="https://github.com/mparoca/chatbot_D-590", color="secondary"),
        dbc.Button(html.Span(["", html.I(className="fab fa-linkedin ml-2")]), href="https://www.linkedin.com/in/maria-paula-aroca-42a0a5166/"),
        dcc.Store(id="store-conversation", data=""),
        conversation,
        controls,
        html.Hr(),
    ],
)

server = app.server
app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
    app.run_server(debug=True)