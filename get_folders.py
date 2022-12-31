from config import API_TOKEN
import requests


space_id = ""
url = "https://api.clickup.com/api/v2/space/{}/folder".format(space_id)

payload = ""
headers = {
  'Content-Type': 'application/json',
  'Authorization': API_TOKEN
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
