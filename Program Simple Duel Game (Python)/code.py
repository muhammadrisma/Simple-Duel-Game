player1 = {"name":"Naruto", "power":500}
player2 = {"name":"Sasuke", "power":400}
player3 = {"name":"Gara", "power":350}

#to increase player power
def train(player):
    player['power'] += 100

#to attack other player 
def attack(attacker, defender):
    if attacker["power"] > defender["power"]:
        print("Kamu Menang ", attacker["name"])
    elif attacker["power"] == defender["power"]:
        print("Nampaknya Kita Setara ", attacker["name"])
    else:
        print("Kamu Lemah ", attacker["name"])

attack(player1, player2)
#train the player so they can increase their power
train(player2)
attack(player1, player2)