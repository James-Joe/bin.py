class Pokemon:
    def __init__(self, name, level, element, maximum_health, current_health, knocked_out):
        self.name = name
        self.level = level
        self.element = element
        self.maximum_health = level
        self.current_health = current_health
        self.knocked_out = knocked_out

    def poke_status(self):
        return "{}'s Stats \nLvl.: {}  Type: {} \nHp: {} \nUnconscious: {}".format(self.name, self.level, self.element, self.current_health, self.knocked_out)

    def loose_hp(self, damage):
        self.damage = damage
        self.current_health = self.current_health - damage
        if self.current_health == 0:
            return self.is_knocked_out(self.current_health)
        return "{}'s hp is now at {}".format(self.name, self.current_health)
    
    def gain_hp(self, potion):
        self.potion = potion
        self.current_health = self.current_health + potion
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
        advantage = ""
        disadvantage = ""
        modifier = 3
        weakness = {"Fire": "Water", "Water" :"Grass", "Grass": "Fire"}
        advantage = advantage + weakness.get(other.element)
        disadvantage = disadvantage + weakness.get(self.element)
        if other.element == disadvantage:
            damage = damage - modifier
        if self.element == advantage:
            damage = damage + modifier
        return other.loose_hp(damage)
        
        
charmander = Pokemon("Charmander", 50, "Fire", 50, 50, False)
squirtle = Pokemon("Squirtle", 50, "Water", 50, 50, False)
bulbasaur = Pokemon("Bulbasaur", 50, "Grass", 50, 50, False)
old_greg = Pokemon("Old Greg", 50, "Water", 50, 50, False )

print(charmander.attack(20, old_greg))
print(old_greg.poke_status())
