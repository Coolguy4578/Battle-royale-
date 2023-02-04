import time
from typing import Dict

Player_Name = input("What's your name?")
from colorama import Fore, Back, Style
import random
import json
level = 1
games ={"My_Game": {}}
first_enemys = {"Aqarita": {"Type": "Water", "Rewards": "gold: 5000"}, "Firouceous": {"Type": "Fire", "Rewards": "item: Blowtorch"}, "Poinetta": {"Type": "Poison", "Rewards": "item: Basic Healing Shroom"}, "Meatalilion": {"Type": "Metal", "Rewards": "item: Basic Magnet"}, "Juniperus": {"Type": "Plant", "Rewards": "item: Basic Pot"}, "Britedelight": {"Type": "Light", "Rewards": "suncoin: 300"}, "Lifta": {"Type": "Air", "Rewards": "gold: 300"}, "Flamer": {"Type": "Fire", "Rewards": "suncoin: 300"}}
starter_wands = {"Water": "Wave", "Fire": "Charry", "Poison": "Deathcapnetta", "Air": "Tornade", "Metal": "Knifeius", "Plant": "Leaf spinner", "Light": "Super-Lamp"}
wands_attacks = {"Wave":  ['Sea Breeze', 'Oceanic Powers', "Aquadixer"], "Charry": ['Firey fling', 'Charing', "Ravenous rendezvous"], 'Deathcapnetta': ['Poisonous spikeing', 'Death cap', "Poison essence"], "Tornade": ["Windy Day", "Phoo!!!", "Air currents"], "Knifeius": ["Metallic showdown", "Crank!!!", "Cut 'em up"], "Leaf spinner": ["Forest hurricane", "Botany Battle", "Green teen"], "Super-Lamp": ["Light-up", "Solar Showdown", "Sunshine, lollipops goodbye"]}
wands_damage_avereage = {"Wave": 1.2, "Charry": 1.7, "Deathcapnetta": 2.0, "Tornade": 1.3, "Knifeius": 0.6, "Leaf spinner": 0.8, "Super-Lamp": 0.09}
NPC_Chat_tree: dict[str, str] = {"King of the high lands": f"Hi and welcome to my lair. You have come to ask what I do young fledgling, am I correct. Well I rule the high lands by peace and charm. And now off with your head! /battle"}
keys = list(wands_damage_avereage.keys())
random_key = random.choice(keys)
random_wand_data = wands_damage_avereage.get(random_key)
first_enemys_list = ["Aqarita", "Firouceous", "Poinetta", "Meatalilion", "Juniperus", "Britedelight", "Lifta"]
random_number = random.randint(0, len(first_enemys_list))
enemy = random.choice(first_enemys_list)
wand = starter_wands.get(first_enemys[enemy]["Type"])
wand2 = wand
items = {"Apple": 5, "Power Soda": 10, "Superpowerfull Elixr": 9}
inventory = ["Apple", "Superpowerfull Elixr"]
filename = "instructions.txt"
coins = 100
def instruct(filename):
    with open(filename.rstrip()) as f:
        for line in f:
            x = line
            print(x)
# noinspection PyMethodMayBeStatic
class InnerCode:
    """Replacement for the failed attempt to call functions from inner_code.py"""
    def __init__(self):
        """Start up class InnerCode"""
    def make_boss(self,boss_name,boss_hp,boss_attacks,miss_rate, playerHP, wand_data, coins):
        """Make a boss to battle. Boss data will be stored in a dictionary and will be passed as arguments to create the boss"""
        print(f"Battle: You vs. {boss_name.title()}!")
        print(f"You have {playerHP} Hp. The enemy has {boss_hp} HP.")
        player_attacks = wands_attacks.get(wand)
        while True:
            player_move_choice = input("What do you want to use on your turn? B: block, A: attack, U: use item")
            if player_move_choice == "A":
                player_attack = input(f"What attack do you want to use? {player_attacks}")
                if player_attack in player_attacks:
                    print("Real attack!")
                    attack_damage = self.calucate_damage(wand_data, False)
                    print(f"{Player_Name} used {player_attack} on {boss_name}! It did {attack_damage} damage.")
                    boss_hp = boss_hp - attack_damage
                    print(f"{boss_name}'s turn:")
                    boss_attack = random.choice(boss_attacks)
                    boss_damage = self.calucate_damage(wand_data, Boss_Turn=True)
                    print(f"The boss, {boss_name} used {boss_attack} on you!")
                    print(f"It dealt {boss_damage} damage.")
                    playerHP = playerHP - boss_damage
                    print(f"The player now has {playerHP} HP.")
                else:
                    print("Invalid attack.")
                    exit(56)
            elif player_move_choice == "B":
                print("Spinning for block successful...")
                block_success = random.randint(1,10)
                if block_success < 5:
                    block_success = True
                else:
                    block_success = False
                if block_success:
                    print("Your Block worked!")
                    print(f"Now for your opponent, {boss_name}:")
                    print(f"{boss_name} attacks but it was thwarted by {Player_Name}'s block!")
                else:
                    print("Sadly your block failed. You will be attacked and you can't do anything.")
            elif player_move_choice == "U":
                if inventory == []:
                    print("Sorry, battle some more to get items. You don't have any.")
                else:
                    print("Here are all the items in your inventory:")
                    item_id = 0
                    for item in inventory:
                        print(f"ItemID: {item_id}, Item:{item}")
                        item_id = item_id + 1
                    item_id = input("Enter the ItemID of the item you want to equip.")
                    item_id = int(item_id)
                    item = inventory[item_id]
                    correct = input(f"Is this it? {inventory[item_id]} Yes/No")
                    if correct == "Yes":
                        print("Equipping Item...")
                        time.sleep(1)
                        print("Item used. Healing or increasing health...")
                        health_increase = items.get(item)
                        playerHP = playerHP + health_increase
                        inventory.pop(item_id)
                        print(f"You now have {playerHP} HP.")
                    elif correct == "No":
                        print("We will show you again:")
                        for item in inventory:
                            item_id = item_id + 1
                            print(f"ItemID: {item_id}, Item:{item}")
                        item_id = input("Please double check this time: Which item do you want?")
                        print(f"This is it: {inventory[item_id]}")
                        print("OK")
                        health_increase = items.get(item)
                        playerHP = playerHP + health_increase
                        print(f"You now have {playerHP} HP.")
                    else:
                        print("Sorry, invalid move choice bye-bye!")
                        exit("I will miss you")
            if playerHP < 0 or playerHP == 0 and boss_hp > 0:
                print(f"Sorry {Player_Name}, you died!")
                break
            elif playerHP > 0 and boss_hp > 0:
                continue
            elif playerHP > 0 and boss_hp <= 0:
                print("You defeated the boss!")
                coins = coins + miss_rate * 3
                print(f"You just got {miss_rate * 3} coins!")
                break
            else:
                print("You both died.")
                break

        return coins
    def Brute_First_Battle_Explain(self, enemy, wand):
        damage_calucater = self.calucate_damage(random_wand_data)
        """Walk through first battle using 'Brute'."""
        print("Hi my name is Brute. I'll walk you through your first battle.")
        print("Let's spin the Wheel of foes.")
        print(f"Spinning... Spinning... Spinning... it landed on {enemy}!")
        print(f"Your enemy, {enemy} has 15 health.")
        print(f"Hmm... My psychic senses predict {enemy} is a {first_enemys.get(enemy)['Type']} type.")
        print(f"{Player_Name.title()} on your turn the game will ask you what you want your move to be.")
        print(f"Let's battle {enemy.title()}!")
        enemy_value = enemy
        Brute_enemy_health = 15
        wand = starter_wands.get(first_enemys[enemy]["Type"])
        health = random.randrange(start=13, stop=17, step=1)
        print(f"I'll give you a wand. Your wand will be The {wand} wand.")
        print(f"The wand {wand} has the following attacks: ")
        for attack in wands_attacks.get(wand):
            print(attack)
        print("Let's see how much health you have.")
        print(f"It seems you have {health} health.")
        if health > 15:
            bigger_or_smaller_then_usual = "you have more health then the average wizard."
        elif 15 > health:
            bigger_or_smaller_then_usual = "you have less health then average wizard."
        else:
            bigger_or_smaller_then_usual = "you have the amount of health the average wizard has."
        print(f"It also seems {bigger_or_smaller_then_usual}")
        print(f"It's your turn first, {Player_Name}.")
        move = input("You can choose from a(attack), b(block) and i(item).")
        if move == "a":
            my_attack = input("Do you want to use " + wands_attacks.get(wand)[0] + " or " + wands_attacks.get(wand)[1] + "?")

            if my_attack == wands_attacks.get(wand)[0]:
                print(f"Solid choice going {wands_attacks.get(wand)[0]}, {Player_Name}.")
                print("")
            elif my_attack == wands_attacks.get(wand)[1]:
                print(f"Good idea going the best, {Player_Name}.")
            else:
                print("Invalid attack choice.")
                exit()
            print(f"Your {my_attack} dealed {self.calucate_damage()} damage.")
        return wand
        return enemy
        return health
    def calucate_damage(self,damage_factor, Boss_Turn):
        if not Boss_Turn:
            damage = (1 * level * random.randint(1, 100) / random.randint(1,6) + random_number)
            damage = round(damage)
        else:
            damage = (random_wand_data * level * random.randint(1, 100)) / (random.randint(1,1000000006) + random_number)
            damage = round(damage)
        # damage = (wands_damage_avereage.get(wand) * level * random.randrange(1, 5 , 1) / random.randrange(1, 5, 1) + random_number)
        return damage
    def shop(self, shopName, coins):
        print(f"Welcome to {shopName}!")
        item_choice = input(f"What would you like to buy? Enter exact name!(or copy and paste){items.keys()}")
        if item_choice in items:
            print(f"You chose a real item!\n The price is {items.get(item_choice)} coins.")
            print(f"You have {coins} coins.")
            if coins > items.get(item_choice) or coins == items.get(item_choice):
                print("You have enough coins to buy!")
                purchase_gone_through = input(f"Enter Yes or yes or Y or y for yes. Enter No, no, N or n to access no. Do you want to buy {item_choice}?")
                if "Y" or "y" in purchase_gone_through:
                    print("Purchasing item...")
                    time.sleep(0.5)
                    coins = coins - items.get(item_choice)
                    inventory.append(item_choice)
                    print(f"Purchase Success!\n Bye! Thank you for shopping at {shopName}!")
                elif "n" in purchase_gone_through or "N" in purchase_gone_through:
                    print(f"Well bye then! Come back soon {Player_Name}!")
            else:
                print("Sorry you don't have enough coins. Get some more coins in battle, or by accepting missions.")
            return coins
    def NPC(self, NPCname):
        print(NPC_Chat_tree.get(NPCname)
        if "/battle" in NPC_Chat_tree.get(NPCname):
            make_boss(NPCname, 1000, ["Hangman", "Royalty", "Treat the guests without mercy"], 34, 900, random_wand_data, coins)
        else:
            print("hi")
        code = InnerCode()

load_tasks = ["Importing Assets...", "Building Assets...", "Connecting to server...", "Gathering scripts...", "Generating Terrain...", "Loading Dialogue...", "Minting Coins..."]
print("Welcome to Battle-Royal.")
# my_boss = code.make_boss()
game_or_new_game = input("Do you want a new game? Type in Yes if you do, No if you don't. ")
"""Start up game"""
if game_or_new_game == "Yes":
    game_name = input("Please name your game. ")
    games[game_name] = {'Level': 0, 'Last-X': 1, 'Last-Y': 1, 'Playername': Player_Name}
    print(games)
elif game_or_new_game == "No":
    if games == []:
        print("You have No games.")
        game_name = input("Please name your game. ")
        Player_Name = input("Player's Name.")
        games[game_name] = {'Level': 0, 'Last-X': 1, 'Last-Y': 1, 'Playername': Player_Name}
        print(games)
    else:
        print(f"Here are your games: ")
        with open("games.json", 'w'):
            for game in games:
                    print(game)
                    is_it = input("Is this the game you want? Yes or No?")
                    if is_it == "Yes":
                        print(f"{game.title()} is the game you want.")
                    break
        print(f'In {game.title()} your level is {games[game]["Level"]} and your name is {games[game]["Playername"]}.')
x = 0
for x in range(0,6):
    print(f"{load_tasks[x]} We are on the  {x}st/nd/rd/th second.")
print("Load complete")
print("Now Let's play Battle-Royal!")
print(f"Coins started at {coins}")
code.NPC("King of the high lands")
code.make_boss("Baby",5,["Hate Is great", "Mean World"], 34, 1000,67, coins)
print(f"Coins are now {coins}")
code.shop("Felette's", coins)

