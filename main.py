import requests

data = requests.get(
    "https://steamspy.com/api.php",
    params={"request": "appdetails", "appid": 413150}
).json()

name = data["name"]
discount = data["discount"]

print("Name:", name)
print("Discount:", discount, "%")