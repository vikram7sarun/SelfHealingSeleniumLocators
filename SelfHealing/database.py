import datetime
from models import session, LocatorData
from sqlalchemy import and_
import base64

def load_data_by_date(start_date=None, end_date=None):
    query = session.query(LocatorData)
    if start_date and end_date:
        query = query.filter(and_(LocatorData.healed_timestamp >= start_date, LocatorData.healed_timestamp <= end_date))
    return query.all()

def format_data(data):
    return [
        {
            "Original Locator": d.original_locator,
            "Alternative Locator": d.alternative_locator,
            "Status": d.status,
            "Heal": d.heal,
            "Healed Timestamp": d.healed_timestamp.strftime("%Y-%m-%d %H:%M:%S") if d.healed_timestamp else "",
            "Screenshot": d.screenshot  # Note: In practice, you may want to decode this to display in Dash.
        }
        for d in data
    ]

def update_entry(row, screenshot_binary):
    entry = session.query(LocatorData).filter_by(original_locator=row["Original Locator"]).first()
    if entry:
        entry.status = "Healed"
        entry.healed_timestamp = datetime.datetime.now()
        entry.screenshot = screenshot_binary
        entry.heal = True
    else:
        entry = LocatorData(
            original_locator=row["Original Locator"],
            alternative_locator=row["Alternative Locator"],
            status="Healed",
            heal=True,
            healed_timestamp=datetime.datetime.now(),
            screenshot=screenshot_binary
        )
        session.add(entry)
    session.commit()

def format_data(data):
    return [
        {
            "Original Locator": d.original_locator,
            "Alternative Locator": d.alternative_locator,
            "Status": d.status,
            "Heal": d.heal,
            "Healed Timestamp": d.healed_timestamp.strftime("%Y-%m-%d %H:%M:%S") if d.healed_timestamp else "",
            "Screenshot": f"data:image/png;base64,{base64.b64encode(d.screenshot).decode()}" if d.screenshot else ""
        }
        for d in data
    ]