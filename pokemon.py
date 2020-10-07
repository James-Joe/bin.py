class Pokemon:
    def __init__(self, name, level, element, maximum_health, current_health, knocked_out):
        self.name = name
        self.level = level
        self.element = element
        self.maximum_health = level
        self.current_health = current_health
        self.knocked_out = knocked_out
    
    def poke_status(self):
        return "Hp: {} \nUnconscious: {}".format(self.current_health, self.knocked_out)

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
        
charmander = Pokemon("Charmander", 4, "Fire", 4, 4, False)
squirtle = Pokemon("Squirtle", 4, "Water", 4, 4, False)
bulbasaur = Pokemon("Bulbasaur", 4, "grass", 4, 4, False)
old_greg = Pokemon("Old Greg", 4, "water", 4, 4, False )

charmander.loose_hp(4)
charmander.gain_hp(200)
print(charmander.poke_status())
