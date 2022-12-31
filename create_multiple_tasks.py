import requests
import json
import time
from config import API_TOKEN, USER_ID
import helpers

list_id = ""
url = "https://api.clickup.com/api/v2/list/{}/task".format(list_id)
requests_count = 0


def create_task(name, desc, start_date, due_date, time_estimate):
    payload = json.dumps({
      "name": name,
      "description": desc,
      "assignees": [
        USER_ID
      ],
      "tags": [],
      "status": "Open",
      "priority": None,
      "due_date": due_date,
      "due_date_time": False,
      "time_estimate": time_estimate,
      "start_date" : start_date,
      "start_date_time": False,
      "notify_all": False,
      "parent": None,
      "links_to": None,
      "custom_fields": []
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': API_TOKEN
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


dates_in_year = helpers.get_all_dates_in_year()
for dt in dates_in_year:
    if requests_count > 100:
        print("Sleeping...")
        time.sleep(60)
        requests_count = 0
    start_date = helpers.get_unix_time(dt, [0,0,0])
    due_date = helpers.get_unix_time(dt, [23, 59, 59])

    create_task("Morning Exercise", "", start_date, due_date, 1800000)
    requests_count += 1



