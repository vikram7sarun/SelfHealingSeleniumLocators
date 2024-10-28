from dash import Dash
from layout import create_layout
from callbacks import register_callbacks
import config

# Initialize the Dash app
app = Dash(__name__, suppress_callback_exceptions=True)  # Suppress exceptions if any dynamic components are used

# Set layout and register callbacks
app.layout = create_layout(app)
register_callbacks(app)

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=config.DEBUG_MODE,port=8051)
