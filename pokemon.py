class Pokemon:
    def __init__(self, name, level, element, maximum_health, current_health, knocked_out=False, disadvantage=None):
        self.name = name
        self.level = level
        self.element = element
        self.maximum_health = level
        self.current_health = current_health
        self.knocked_out = knocked_out
        weakness = {"Fire": ["Water", "Rock"], "Water": ["Grass"], "Grass": ["Fire", "Flying"],
        "Rock": ["Flying"], "Flying": ["Rock"]}
        self.disadvantage = weakness.get(self.element)

        
    def __repr__(self):
        return self.name

    def poke_status(self):
        return "{}'s Stats \nLvl.: {}  Type: {} \nHp: {} \nUnconscious: {} \nWeaknesses: {}".format(
            self.name, self.level, self.element, self.current_health, self.knocked_out, self.disadvantage)

    def loose_hp(self, damage):
        self.damage = damage
        self.current_health = self.current_health - damage
        if self.current_health == 0:
            return self.is_knocked_out(self.current_health)
        return "{}'s hp is now at {}".format(self.name, self.current_health)
    
    def gain_hp(self, health):
        self.health = health
        self.current_health = self.current_health + health
        if self.current_health > self.maximum_health:
            self.current_health = self.maximum_health
        if self.current_health > 0:
            self.knocked_out = False
        return "{}'s hp is now at {}".format(self.name, self.current_health)

    def is_knocked_out(self, current_health):
        if self.current_health == 0:
            self.knocked_out = True
            return "{} is knocked the fuck out!".format(self.name)
    
    def attack(self, damage, other):
        modifier = 3
        for i in self.disadvantage:
            if i == other.element:
                damage = damage - modifier
        for i in other.disadvantage:
            if i == self.element:
                damage = damage + modifier
        
        return other.loose_hp(damage)
        
        

class Trainer:
    def __init__(self, name, creatures, potions, current_pokemon):
        self.name = name
        self.creatures = creatures
        self.potions = potions
        self.current_pokemon = creatures[current_pokemon]

    def trainer_stats(self):
        return "Name: {} \nInventory: {} \npotions: {} \nselected pokemon: {}".format(
        self.name, self.creatures, self.potions, self.current_pokemon)

    def remove_creature(self, creature):
        self.creatures.remove(creature)
        return self.trainer_stats()

    def add_creature(self, creature):
        if len(self.creatures) < 6:
            self.creatures.append(creature)
        elif len(self.creatures) == 6:
            value = input("Discard a pokemon: {}\n".format(self.creatures))
            value = eval(value)  #this only works if the user knows the object's variable name e.g. "old_greg" for Old Greg
            self.remove_creature(value)
            self.creatures.append(creature)
        return self.trainer_stats()

    def heal_poke(self,creature):
        print(creature.gain_hp(10))
        self.potions -= 1
        if self.potions == 0:
            print("You don't have any potions")
        return self.trainer_stats()

    def attack_trainer(self, damage, trainer):
        return self.current_pokemon.attack(damage, trainer.current_pokemon)
    
    def change_pokemon(self, new_pokemon):
        if new_pokemon.knocked_out == True:
            print("{} is knocked out. Choose another pokemon".format(new_pokemon.name))
        else:
            new_pokemon = self.creatures.index(new_pokemon)
            self.current_pokemon = self.creatures[new_pokemon]
        return self.trainer_stats()


charmander = Pokemon("Charmander", 50, "Fire", 50, 50)
squirtle = Pokemon("Squirtle", 50, "Water", 50, 50)
bulbasaur = Pokemon("Bulbasaur", 50, "Grass", 50, 50)
old_greg = Pokemon("Old Greg", 50, "Water", 50, 50)
growlithe = Pokemon("Growlithe", 50, "Fire", 50, 50)
poliwhirl = Pokemon("Poliwhirl", 50, "Water", 50, 50)
oddish = Pokemon("Oddish", 50, "Grass", 50, 50)
bellsprout = Pokemon("Bellsprout", 50, "Grass", 50, 50)


ash = Trainer("Ash",[charmander, squirtle, bulbasaur, old_greg, growlithe, poliwhirl], 5, 4)
gary = Trainer("Gary", [bulbasaur, bellsprout, poliwhirl, old_greg, growlithe, squirtle], 5, 2)

print(squirtle.attack(20, oddish))

