import requests
from config import API_TOKEN

team_id = ""
url = "https://api.clickup.com/api/v2/team/{}/space".format(team_id)

payload = ""
headers = {
  'Content-Type': 'application/json',
  'Authorization': API_TOKEN
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
