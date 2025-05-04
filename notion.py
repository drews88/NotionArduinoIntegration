from notion_client import Client # type: ignore
from dotenv import load_dotenv # type: ignore
import os
import json

load_dotenv()

#notion api
notion = Client(auth=os.getenv("NOTION_API_KEY"))
database_id = os.getenv("NOTION_DATABASE_ID")
response = notion.databases.query(database_id=database_id)

#get courses of the calendar entries
results = response["results"]
names = []
for page in results:
    try:
        name = page["properties"]["Class"]["select"]["name"]
        names.append(name)
        print(name)
    except Exception as e:
        try:
            print(page["properties"]["Name"]["title"][0]["plain_text"] + " Is not affiliated with a course")
        except Exception:
            print("???")

#count frequency of work/course        
freq_names = {}
for name in names:
    if name in freq_names:
        freq_names[name] += 1
    else:
        freq_names[name] = 1

        