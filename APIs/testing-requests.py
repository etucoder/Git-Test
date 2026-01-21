import requests
print("IS THIS EVEN WORKING!!!!!!!!!!!")
response = requests.get("https://catfact.ninja/fact")
data = response.json()
print(data)