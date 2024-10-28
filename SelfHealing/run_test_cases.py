from database import populate_initial_data, execute_test_cases, update_entry

# Path to test screenshot
screenshot_path = "test_screenshot.png"

# Read screenshot as binary data
with open(screenshot_path, 'rb') as file:
    screenshot_binary = file.read()

# Test data for update_entry
test_row = {
    "Original Locator": "By.ID='username'",
    "Alternative Locator": "By.XPATH='//*[@id=\"username\"]'"
}

# Run test functions
populate_initial_data()
execute_test_cases()

# Update entry with binary screenshot data
update_entry(test_row, screenshot_binary=screenshot_binary)
