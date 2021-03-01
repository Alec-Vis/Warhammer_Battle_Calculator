import main
#should the weapons be a seperate file within a faction folder?

class Death_Guard(main.Core):
    # Plague Company
    # strategems? or create a DeathGuard strat class?
    pass

class Weapon:
    # Weapons should be seperate classes within each faction file
    # should each weapon be its own class?
    # Then each weapon would have its own Attack Method inside it
    def __init__(self, Num, Strength, ArmorPen, Dmg):
        #self.Type = Type
        self.Num = Num # should this be part of the class? or simply added to each instance?
        self.Strength = Strength
        self.ArmorPen = ArmorPen
        self.Dmg = Dmg

class RangedWp(Weapon):
    pass

class MeleeWp(Weapon):
    pass

class Infantry(Death_Guard):
    # Maybe the common infantry keywords can go here? 
    # unique ones can be tagged onto each individual unit class
    # each particular unit should inherit from two classes
    # The faction/unit_type and the weapon class
    # reference for later
    # https://www.programiz.com/python-programming/multiple-inheritance
    pass

class Vehicle(Death_Guard):
    pass

class Character(Death_Guard):
    pass

class Plague_Marines(Infantry, RangedWp , MeleeWp):
    # will need to change the melee/ranged weapons
    #class attributes/variables? will be unit tags and types
    #should the weapons be class variables?
    # i am thinking weapons should be in the form of dictionaries?
    UnitType = {'Chaos','Nurgle','Heretic Astartes','Death Guard'}
    KeyWords = {'Infantry','Core', 'Bubonic Astartes','Plague Marines'}
    def __init__(self):
        Infantry.__init__(self)
        RangedWp.__init__(self) #maybe select only available options
        MeleeWp.__init__(self) #maybe select only available options