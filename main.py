import requests
import re

region = "PH"
gamesList = []
game = ""

# Get game id user input, until user types "EXIT"
while game != "EXIT":
    game = input("Enter the name of a game (or type 'EXIT' to quit): ")
    if game != "EXIT":
        gamesList.append(game)

# Loop the list of games, and fetch the game name and discount from SteamSpy API
for i in range(len(gamesList)):

    # Use Steam store suggest search to get the app ID
    searchGame = requests.get("https://store.steampowered.com/search/suggest",
        params={"term": gamesList[i], "f": "games", "cc": region, "l": "en"}
    )
    searchGame = searchGame.text
    print(searchGame)
    appId = re.findall(r'data-ds-appid="(\d+)"', searchGame)
    price = re.findall(r'match_price">\s*([^<]+)', searchGame)
    price = float(re.sub(r"[^\d.]", "", price[0]))

    data = requests.get(
        "https://steamspy.com/api.php",
        params={"request": "appdetails", "appid": appId[0]},
    ).json()

    name = data["name"]
    discount = data["discount"]
    original = price / (1 - int(discount)/100)

    print("Name:", name)
    print("Discount:", discount, "%")
    print("Price: ", price)
    print("Original Price: ", original)