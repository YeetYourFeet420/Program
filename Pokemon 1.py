# Figuring out Type Matchups. We define Effective with the parameters x and y. 
# x being the attacking type and y being the defending type.
import random
from unicodedata import name
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
        elif y == "Ice":
            return "Effective"
        elif y == "Ghost":
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
        elif y == "Ice":
            return "Effective"
        elif y == "Ghost":
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
        elif y == "Ice":
            return "Super Effective"
        elif y == "Ghost":
            return "Immune"
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
    if x == "Ghost":
        if y == "Fire":
            return "Effective"
        elif y == "Water":
            return "Effective"
        elif y == "Grass":
            return "Effective"
        elif y == "Fighting":
            return "Effective"
        elif y == "Psychic":
            return "Super Effective"
        elif y == "Dark":
            return "Not Very Effective"
        elif y == "Ice":
            return "Effective"
        elif y == "Ghost":
            return "Super Effective"
 
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
    if move_name == "Vine Whip":
        return "Grass"
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
    if move_name == "Vine Whip":
        return 45
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
print("What pokemon are you attacking?")
Defending_name = input()
dmg = final(Lvl, Move_Power(Attack_name), Attack_stat, Defense_stat ,1, Pokemon_type(name), Move_Type(Attack_name), Pokemon_type(Defending_name))
print("Attack damage was:", dmg)

class Stats():
    def __init__(self, hp, atk, defense, spa, spd, spe):
        self.hp = hp 
        self.atk = atk
        self.defense = defense
        self.spa = spa
        self.spd = spd
        self.spe = spe
        

def Pokemon_stats(pokemon_name):
    if pokemon_name == "Charmander":
        return Stats(39,52,43,60,50,65)
    if pokemon_name == "Charmeleon":
        return Stats(58,64,58,80,65,80)
    if pokemon_name == "Charizard":
        return Stats(78,84,78,109,85,100)
    if pokemon_name == "Squirtle":
        return Stats(44,48,65,50,64,43)
    if pokemon_name == "Wartortle":
        return Stats(59,63,80,65,80,58)
    if pokemon_name == "Blastoise":
        return Stats(79,83,100,85,105,78)
    if pokemon_name == "Bulbasaur":
        return Stats(45,49,49,65,65,45)
    if pokemon_name == "Ivysaur":
        return Stats(60,62,63,80,80,60)
    if pokemon_name == "Venasaur":
        return Stats(80,82,83,100,100,80)


class Pokemon():
    def __init__(self, pokemon_name, name):
        self.nickname = name
        self.stats = Pokemon_stats(pokemon_name)
        self.type = Pokemon_type(pokemon_name)
        self.pokemon_name = pokemon_name
        self.current_hp = self.stats.hp
        self.current_atk = self.stats.atk
        self.level = 1
        self.moveset = "To-Do"
        self.possible_moves = "To-Do"
    
    def attackedBY(self, attacking_pokemon, move_name):
        dmg = final(attacking_pokemon.level, Move_Power(move_name), self.stats.defense ,1, Pokemon_type(name), Move_Type(attack_name), Pokemon_type(defending_name))
        self.current_hp = self.current_hp - 


    def AttackingPokemonAttack():
        Bulba.current_atk 






Chara = Pokemon("Charmander","Fuego")
Bulba = Pokemon("Bulbasaur","Onion")
print(Chara.current_hp)
Chara.attackedBY(Bulba,"Tackle")
print(Chara.current_hp)

HP_Stat = 0
ATK_Stat = 1
DEF_Stat = 2
SPA_Stat = 3
SPD_Stat = 4
SPE_Stat = 5
Type_Index = 6

Bulbasaur_Stats = [45,49,49,65,65,45,"Grass"]
Ivysaur_Stats = [60,62,63,80,80,60,"Grass"]
Venasaur_Stats = [80,82,83,100,100,80,"Grass"]
Charmander_Stats = [39,52,43,60,50,65,"Fire"]
Charmeleon_Stats = [58,64,58,80,65,80,"Fire"]
Charizard_Stats = [78,84,78,109,85,100,"Fire"]
Squirtle_Stats = [44,48,65,50,64,43,"Water"]
Wartortle_Stats = [59,63,80,65,80,58,"Water"]
Blastoise_Stats = [79,83,100,85,105,78,"Water"]
