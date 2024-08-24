# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://promilaseth.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0DzJZE1Gjap8qZQmcGvX2oT4tEUasqGIHtUA2u37zGGx8tFJy88qRuFQEXmlhA_OT-VjZlodsh1LYtUDCr1deVmWb4xeWEYbZPDYhzoN2EB0xD11PiMgdJVWQzj3X8zKGY21Ignpd6FlfIBJwaSg7ntxZQOCQqHRAXkupbbxnXcU=7261D226"

auth = HTTPBasicAuth("hoshankseth@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text)[0]["name"], sort_keys=True, indent=4, separators=(",", ": ")))