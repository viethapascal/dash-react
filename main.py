import dash_ace
import dash_mantine_components as dmc
from dash import Dash, Input, Output, html

app = Dash(__name__,
           external_stylesheets=["https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css"])

header = dmc.Header(
    height=60, p='xs',
    children=[
        "HOMEPAGE",
        dmc.Group(
            sx="{{height: '100%'}}",
            px="20",
            position="apart",
            children=[])
    ])
navbar = dmc.Navbar(
    p="xs",
    sx={
        "width": "300px"
    },
    children=[
        # html.Section([
            dmc.Button(
                unstyled=True,
                fullWidth=True,
                sx={
                    "display": "block",
                    "border-radius": "1px",
                    "border": "none",
                    "background": "white",
                    "width": "100%",
                    "&:hover": {
                        "background": "#F8F9FA"
                    }
                },
                p="xs",
                children=[
                    dmc.Group([
                        dmc.ThemeIcon(color="blue", variant="light", className="ti ti-git-pull-request", size=16),
                        dmc.Text(styles={"size": "sm"}, children="Register")
                    ])
                ]
            )
        # ])
    ],
)
code_edtior = dash_ace.DashAceEditor(
            # id='input',
            style={"max-height": "600px"},
            value='def test(a: int) -> str : \n'
                  '    return f"value is {a}"',
            theme='github',
            mode='python',
            tabSize=2,
            enableBasicAutocompletion=True,
            enableLiveAutocompletion=True,
            autocompleter='/autocompleter?prefix=',
            placeholder='Python code ...'
        )
database_form = html.Form([
    dmc.TextInput(label="DSN", placeholder="Postgres DSN"),
    dmc.Select(label="Schema", placeholder="Choose schema"),
    dmc.Group([
        dmc.Button(variant="outline", children="Fetch Tables")
    ], mt="xl"),
    dmc.Group(code_edtior, mt="xl"),
])
app.layout = html.Div(
    [
        dmc.AppShell(
            padding='md',
            header=header,
            navbar=navbar,
            children=[
                dmc.SimpleGrid([
                    database_form,
                    html.Div([
                        dmc.Text("Real-time log", mb="xl"),
                        dmc.Timeline([
                            dmc.TimelineItem(bullet=dmc.ActionIcon(className="ti ti-git-pull-request"), title="Step 1", children=[dmc.Text("This is step 1")]),
                            dmc.TimelineItem(bullet=dmc.ActionIcon(className="ti ti-2fa"), title="Step 2", active=1, children="This is step 2"),
                            dmc.TimelineItem(bullet=dmc.ActionIcon(className="ti ti-2fa"), title="Step 3", children="This is step 3"),
                            dmc.TimelineItem(bullet=dmc.ActionIcon(className="ti ti-2fa"), title="Step 3", children="This is step 4"),
                        ], bulletSize=30, lineWidth=5, active=1)
                    ]),
                ], cols=2)

            ],
            fixed=False)

    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)