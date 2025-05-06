from datetime import datetime, timedelta
from dateutil import parser

def withinWeek(date_str: str) -> bool:
    #print("Processing: " + date_str)
    try:
        parsed_date = parser.parse(date_str).date()
    except (ValueError, TypeError):
        return False
    
    todaysDate = datetime.today().date()
    nextWeek = todaysDate + timedelta(days=7)
    return todaysDate <= parsed_date <= nextWeek