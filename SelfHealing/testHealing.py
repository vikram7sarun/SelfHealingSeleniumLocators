from models import session, LocatorData

# Test database connection
try:
    result = session.query(LocatorData).first()
    print("Database connection successful, first entry:", result)
except Exception as e:
    print("Database connection error:", e)