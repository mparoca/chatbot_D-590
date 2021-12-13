import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from get_answer import get_answer

#from app import server
#from app import app

#Theme
#https://bootswatch.com/vapor/ 

#Icons
# https://fontawesome.com/v5.15/icons?d=gallery&p=2


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
        html.H1([html.I(className="fab fa-wikipedia-w ml-0"),"iki-QA-Bot ", html.I(className="fas fa-robot ml-0")]),
        html.H5("I am a question-answering bot fine-tuned on WikiQA"),
        html.H5("Learn more below:"),
        dbc.Button(html.Span(["", html.I(className="fab fa-github ml-2")]), href="https://github.com/mparoca/chatbot_D-590", color="secondary"),
        dbc.Button(html.Span(["", html.I(className="fab fa-windows ml-2")]), href="https://www.microsoft.com/en-us/research/publication/wikiqa-a-challenge-dataset-for-open-domain-question-answering/", color="info"),
        dbc.Button(html.Span(["", html.I(className="fab fa-linkedin ml-2")]), href="https://www.linkedin.com/in/maria-paula-aroca-42a0a5166/"),
        html.Hr(),
        dcc.Store(id="store-conversation", data="Hello! I am a knowledge-based question answering bot. If you ask me a factual question I will give you the answer. Try asking : what does the president of the usa do?"),
        conversation,
        controls,
        html.Hr(),
    ],
)


## CALLBACKS
@app.callback(
    Output("display-conversation", "children"), [Input("store-conversation", "data")]
)
def update_display(chat_history):
    return [
        textbox(x, box="self") if i % 2 == 0 else textbox(x, box="other")
        for i, x in enumerate(chat_history.split(">"))
    ]


@app.callback(
    [Output("store-conversation", "data"), Output("user-input", "value")],
    [Input("submit", "n_clicks"), Input("user-input", "n_submit")],
    [State("user-input", "value"), State("store-conversation", "data")],
)
def run_chatbot(n_clicks, n_submit, user_input, chat_history):
    if n_clicks == 0:
        return "", ""

    if user_input is None or user_input == "":
        return chat_history, ""
    
    try:
        get_answer(user_input)
        return chat_history + ">Q: " + user_input + ">A: " + get_answer(user_input), ""
    
    except:
        return chat_history + ">Q: " + user_input + ">Sorry, please be more specific, I'm still learning", ""

    

server = app.server
app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
    app.run_server(debug=True)