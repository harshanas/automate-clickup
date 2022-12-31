import requests
from config import API_TOKEN


url = "https://api.clickup.com/api/v2/team"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Authorization': API_TOKEN
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
