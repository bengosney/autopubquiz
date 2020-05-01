import requests

response = requests.get('https://opentdb.com/api.php', params={'amount': 10})
response.raise_for_status()
# access JSON content
jsonResponse = response.json()
print("Entire JSON response")
print(jsonResponse)
