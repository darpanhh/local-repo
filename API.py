import requests

url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(" Here's your joke:")
    print(data["joke"])
else:
    print("Failed to get a joke. Status code:", response.status_code)