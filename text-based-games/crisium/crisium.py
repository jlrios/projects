currentRoom = "Common Area"

inventory = []

rooms = {
    "Hall": {
        "id": 1,
        "south": "Common Area"
    },
    "Common Area": {
        "id": 2,
        "north": "Hall",
        "item": "card",
        "itemType": "access"
    } 
} 

print("You are in the " + currentRoom)

def startGame():


def showInstructions():
    print("CRISIUM GAME")
    print("==============")
    print("Go [direction]")
    print("Get [item]")

while True:
    showInstructions()

    command = input("> ")
    action = command.split(" ", 1)
    if action[0] == "go":
        if acction[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][action[1]]
            print("You are in the " + currentRoom)

    if action[0] == "get":
        if action[1] == rooms[currentRoom]["item"]:
            print(f"You got a {action[1]}!")
            inventory.append(action[1])
            print("Inventory:", inventory)
