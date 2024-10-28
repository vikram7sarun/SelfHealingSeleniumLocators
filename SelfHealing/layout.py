from dash import dcc, html, dash_table


def create_layout(app):
    return html.Div([
        html.H1("Self-Healing Locator Dashboard"),

        # Container for Date Picker and buttons to align them horizontally
        html.Div([
            # Date picker for date-based filtering
            dcc.DatePickerRange(
                id="date-picker-range",
                display_format="YYYY-MM-DD"
            ),

            # Filter by Date button
            html.Button(
                "Filter by Date",
                id="filter-date-button",
                n_clicks=0,
                style={
                    'backgroundColor': '#007bff',  # Primary blue
                    'color': 'white',
                    'border': 'none',
                    'padding': '10px 20px',
                    'fontSize': '16px',
                    'borderRadius': '5px',
                    'cursor': 'pointer',
                    'marginLeft': '10px'  # Space between Date Picker and button
                }
            ),

            # Apply Healing button
            html.Button(
                "Apply Healing",
                id="apply-healing",
                n_clicks=0,
                style={
                    'backgroundColor': '#28a745',  # Success green
                    'color': 'white',
                    'border': 'none',
                    'padding': '10px 20px',
                    'fontSize': '16px',
                    'borderRadius': '5px',
                    'cursor': 'pointer',
                    'marginLeft': '10px'  # Space between buttons
                }
            )
        ], style={'display': 'flex', 'alignItems': 'center', 'gap': '10px', 'margin-top': '10px'}),

        # Data table for displaying locator information
        dash_table.DataTable(
            id="locator-table",
            columns=[
                {"name": "Original Locator", "id": "Original Locator"},
                {"name": "Alternative Locator", "id": "Alternative Locator"},
                {"name": "Status", "id": "Status"},
                {"name": "Heal", "id": "Heal", "presentation": "dropdown", "type": "text", "editable": True},
                {"name": "Healed Timestamp", "id": "Healed Timestamp"},
                {"name": "Screenshot", "id": "Screenshot"},
            ],
            style_cell={'textAlign': 'left', 'padding': '5px'},
            style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
            style_data_conditional=[
                {'if': {'filter_query': '{Status} = "Found"'}, 'backgroundColor': '#d4edda', 'color': 'black'},
                {'if': {'filter_query': '{Status} = "Not Found"'}, 'backgroundColor': '#fff3cd', 'color': 'black'},
                {'if': {'filter_query': '{Status} = "Failed"'}, 'backgroundColor': '#f8d7da', 'color': 'black'},
                {'if': {'filter_query': '{Status} = "Healed"'}, 'backgroundColor': '#cce5ff', 'color': 'black'}
            ],
            editable=True,

            # Define dropdown options for the "Heal" column
            dropdown={
                "Heal": {
                    "options": [
                        {"label": "Yes", "value": True},
                        {"label": "No", "value": False}
                    ]
                }
            }
        ),

        # Output message for healing result
        html.Div(id="healing-result")
    ])
