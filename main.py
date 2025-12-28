import requests

gamesList = []
game = ""

# Get game id user input, until user types "EXIT"
while game != "EXIT":
    game = input("Enter the name of a game (or type 'EXIT' to quit): ")
    if game != "EXIT":
        gamesList.append(game)

# Loop the list of games, and fetch the game name and discount from SteamSpy API
for i in range(len(gamesList)):
    data = requests.get(
        "https://steamspy.com/api.php",
        params={"request": "appdetails", "appid": gamesList[i]},
    ).json()

    name = data["name"]
    discount = data["discount"]

    print("Name:", name)
    print("Discount:", discount, "%")