import dash
from layout import create_layout
from callbacks import register_callbacks
import plotly.graph_objects as go

# TOKEN-FREE MAPS:
go.layout.mapbox.style = "open-street-map"

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = create_layout()
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
