from dash.dependencies import Input, Output, State
from database import load_data_by_date, format_data, update_entry
import datetime
import dash
import base64
from selenium import webdriver

# Set up Selenium WebDriver for capturing screenshots
driver = webdriver.Chrome()


def capture_screenshot_as_binary():
    """Capture a screenshot in binary format and return it."""
    driver.get("https://example.com")  # Replace with your actual URL
    screenshot = driver.get_screenshot_as_png()  # Capture screenshot as binary (PNG format)
    return screenshot


def register_callbacks(app):
    @app.callback(
        [Output("locator-table", "data"), Output("healing-result", "children")],
        [Input("filter-date-button", "n_clicks"), Input("apply-healing", "n_clicks")],
        [State("date-picker-range", "start_date"),
         State("date-picker-range", "end_date"),
         State("locator-table", "data")]
    )
    def update_data(filter_clicks, heal_clicks, start_date, end_date, rows):
        # Determine which button was clicked
        ctx = dash.callback_context
        if not ctx.triggered:
            return dash.no_update, dash.no_update
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        # If Filter by Date button was clicked
        if button_id == "filter-date-button":
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d") if end_date else None
            data = load_data_by_date(start_date, end_date)
            formatted_data = format_data(data)
            return formatted_data, "Data filtered by date."

        # If Apply Healing button was clicked
        elif button_id == "apply-healing":
            healed_count = 0
            for row in rows:
                if row["Heal"]:
                    # Capture screenshot as binary and update database entry
                    screenshot_binary = capture_screenshot_as_binary()
                    update_entry(row, screenshot_binary)
                    healed_count += 1
            result_message = f"Healed {healed_count} locator(s)"
            return rows, result_message
