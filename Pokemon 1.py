# Figuring out Type Matchups. We define Effective with the parameters x and y. 
# x being the attacking type and y being the defending type.
import random
def Effective(x, y):
    if x == "Fire":
        if y == "Grass":
            return "Super Effective"
        elif y == "Water":
            return "Not Very Effective"
        elif y == "Fire":
            return "Not Very Effective"
        elif y == "Fighting":
            return "Effective"
        elif y == "Psychic":
            return "Effective"
        elif y == "Dark":
            return "Effective"
        elif y == "Ice":
            return "Super Effective"
        elif y == "Ghost":
            return "Effective"
    if x == "Water":
        if y == "Fire":
            return "Super Effective"
        elif y == "Grass":
            return "Not Very Effective"
        elif y == "Water":
            return "Not Very Effective"
        elif y == "Fighting":
            return "Effective"
        elif y == "Psychic":
            return "Effective"
        elif y == "Dark":
            return "Effective"
    if x == "Grass":
        if y == "Water":
            return "Super Effective"
        elif y == "Fire":
            return "Not Very Effective"
        elif y == "Grass":
            return "Not Very Effective"
        elif y == "Fighting":
            return "Effective"
        elif y == "Psychic":
            return "Effective"
        elif y == "Dark":
            return "Effective"
    if x == "Fighting":
        if y == "Fire":
            return "Effective"
        elif y == "Grass":
            return "Effective"
        elif y == "Water":
            return "Effective"
        elif y == "Fighting":
            return "Effective"
        elif y == "Psychic":
            return "Not Very Effective"
        elif y == "Dark":
            return "Super Effective"
    if x == "Psychic":
        if y == "Fire":
            return "Effective"
        elif y == "Water":
            return "Effective"
        elif y == "Grass":
            return "Effective"
        elif y == "Fighting":
            return "Super Effective"
        elif y == "Psychic":
            return "Not Very Effective"
        elif y == "Dark":
            return "Immune"
        elif y == "Ice":
            return "Effective"
        elif y == "Ghost":
            return "Effective"
    if x == "Dark":
        if y == "Fire":
            return "Effective"
        elif y == "Water":
            return "Effective"
        elif y == "Grass":
            return "Effective"
        elif y == "Fighting":
            return "Not Very Effective"
        elif y == "Psychic":
            return "Super Effective"
        elif y == "Dark":
            return "Not Very Effective"
        elif y == "Ice":
            return "Effective"
        elif y == "Ghost":
            return "Super Effective"
    if x == "Ice":
        if y == "Fire":
            return "Not Very Effective"
        elif y == "Water":
            return "Not Very Effective"
        elif y == "Grass":
            return "Super Effective"
        elif y == "Fighting":
            return "Effective"
        elif y == "Psychic":
            return "Effective"
        elif y == "Dark":
            return "Effective"
        elif y == "Ice":
            return "Not Very Effective"
        elif y == "Ghost":
            return "Effective"
 
# We define the Effectiveness_Multiplier and set our parameter for Effectivness
def Effectiveness_Multiplier(Effectiveness):
    if Effectiveness == "Not Very Effective":
        return 1/2
    elif Effectiveness == "Effective":
        return 1
    elif Effectiveness == "Super Effective":
        return 2
    elif Effectiveness == "Immune":
        return 0
# We define product which is our final function to get the end result by combining all of our previous functions together.
def product(attacking_type,defending_type):
    tank = Effective(attacking_type,defending_type)
    barrel = Effectiveness_Multiplier(tank)
    return barrel
# We define STAB which will increase a moves power,
# if the type of the move and the type of the pokemon using that move are the same.
def STAB (attacking_type,move_type):
    if attacking_type == move_type:
        return 1.5
    else:
        return 1

def random_multiplier():
    return random.randrange(85,100)/100

def base_damage(level,power,atk_stat,opp_def_stat):
    return ((2*level/5+2)*power*atk_stat/opp_def_stat)/50+2

def final(level,power,atk_stat,opp_def_stat,critical,attacking_type,same_type,defending_type):
    base = base_damage(level,power,atk_stat,opp_def_stat)
    Guess= random_multiplier()
    Knife = STAB(attacking_type,same_type)
    Type = product(attacking_type,defending_type)
    End = base*Guess*Knife*Type*critical
    return End

def Pokemon_type(pokemon_name):
    if pokemon_name == "Charmander":
        return "Fire"
    if pokemon_name == "Charmeleon":
        return "Fire"
    if pokemon_name == "Charizard":
        return "Fire"
    if pokemon_name == "Squirtle":
        return "Water"
    if pokemon_name == "Wartortle":
        return "Water"
    if pokemon_name == "Blastoise":
        return "Water"
    if pokemon_name == "Bulbasaur":
        return "Grass"
    if pokemon_name == "Ivysaur":
        return "Grass"
    if pokemon_name == "Venasaur":
        return "Grass"

def Move_Type(move_name):
    if move_name == "Water Gun":
        return "Water"
    if move_name == "Ember":
        return "Fire"
    if move_name == "Ice Beam":
        return "Ice"
    if move_name == "Tackle":
        return "Normal"
    if move_name == "Shadow Ball":
        return "Ghost"
    if move_name == "Psychic":
        return "Psychic"
    if move_name == "Dark Pulse":
        return "Dark"

def Move_Power(move_name):
    if move_name == "Water Gun":
        return 60
    if move_name == "Ember":
        return 60
    if move_name == "Tackle":
        return 50
    if move_name == "Ice Beam":
        return 90
    if move_name == "Shadow Ball":
        return 80
    if move_name == "Psychic":
        return 90
    if move_name == "Dark Pulse":
        return 80
    

print("What is the name of your Pokemon?")
name = input()
print("What level is your", name)
Lvl = int(input())
print("What move are you using?")
Attack_name = input()
print("What is your Pokemons Attack Stat?")
Attack_stat = int(input())
print("What pokemon are you attacking?")
Defending_name = input()
print("What is the pokemons defense stat?")
Defense_stat = int(input())
dmg = final(Lvl, Move_Power(Attack_name), Attack_stat, Defense_stat ,1, Pokemon_type(name), Move_Type(Attack_name), Pokemon_type(Defending_name))
print("Attack damage was:", dmg)
