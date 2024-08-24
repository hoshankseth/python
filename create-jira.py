# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://promilaseth.atlassian.net/rest/api/3/issue"

API_TOKEN="ATATT3xFfGF0DzJZE1Gjap8qZQmcGvX2oT4tEUasqGIHtUA2u37zGGx8tFJy88qRuFQEXmlhA_OT-VjZlodsh1LYtUDCr1deVmWb4xeWEYbZPDYhzoN2EB0xD11PiMgdJVWQzj3X8zKGY21Ignpd6FlfIBJwaSg7ntxZQOCQqHRAXkupbbxnXcU=7261D226"

auth = HTTPBasicAuth("hoshankseth@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10001"
    },
    "project": {
      "key": "SCRUM"
    },
    "summary": "First JIRA ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))