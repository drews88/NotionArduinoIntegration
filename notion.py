from notion_client import Client # type: ignore
from dotenv import load_dotenv # type: ignore
import os
import json
from myutils import withinWeek

load_dotenv()

#notion api
notion = Client(auth=os.getenv("NOTION_API_KEY"))
database_id = os.getenv("NOTION_DATABASE_ID")
response = notion.databases.query(database_id=database_id)

#get courses of the calendar entries
results = response["results"]
className = ""
courseNames = []
for page in results:
    try:

        itemdate = page["properties"]["Date"]["date"]["start"]
        if withinWeek(itemdate):

            assignmentName = page["properties"]["Name"]["title"][0]["plain_text"]
            if assignmentName[0] == '!':    #in calendar, I put ! at beginning of any name to denote as exam
                className = "Exams"
            else:
                className = page["properties"]["Class"]["select"]["name"]
            courseNames.append(className)
            
    except Exception as e:
        
        try:
             print(page["properties"]["Name"]["title"][0]["plain_text"] + " is missing data")
             print(e)
        except Exception:
            print("something is wrong...")

#count frequency of work/course        
freq_names = {} 
for name in courseNames:
    if name in freq_names:
        freq_names[name] += 1
    else:
        freq_names[name] = 1

        