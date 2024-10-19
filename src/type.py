#!/usr/bin/env python3
import sys
#class Base(type):
#    # create a class for me.
#    def __new__(cls, class_name, bases, attrs):
#        #if not 'cls.health' in attrs:
#        #    raise ValueError("Value "'health'" must be defined")
#        #else:
#        #    if 'cls.health' in attrs and not isinstance(attrs['cls.health'], int):
#        #        raise TypeError("'value' must be an integer.")
#
#        #instance = super().__new__(cls, name, bases, attrs)
#        #return instance
#
#        required_attrs = {
#                "name": str, 
#                "health": int
#        }
#
#        for attr in required_attrs.keys():
#            attr_type = required_attrs[attr]
#
#            print(attrs)
#            if attr in attrs and not isinstance(attrs[attr], attr_type):
#                raise TypeError(f"Value {attr} must be defined correctly: {required_attrs[attr]}")
#
#        return super().__new__(cls, class_name, bases, attrs)
#
#
#
#class Character(metaclass=Base):
#    name: int  = "test"
#    health: int = 100

#c = Character()
#print(c.name)

class Character:
    def __init_subclass__(cls, 
            /, 
            name: str = "", 
            health: int = 0, 
            agility: int = 0, 
            dexterity: int = 0, 
            intelligence: int = 0, 
            **kwargs
        ):

        super().__init_subclass__(**kwargs)
        cls.name = name
        cls.health = health
        cls.agility = agility
        cls.dexterity = dexterity

    def attack(cls):
        pass

    def take_damage(cls, amount):
        pass

    def heal(cls, amount):
        pass

    def block(cls):
        pass


class Hero(Character):
    def __init__(self):
        self.name = name
        self.health = health
        self.agility = agility
        self.dexterity = dexterity
        self.intelligence = intelligence

        self.inventory = []

        def add_to_inventory(self, item):
            self.inventory.append(item)

        def list_inventory(self):
            return self.inventory

        def remove_from_inventory(self, item):
            pass

        def take_damage(self, amount):
            pass

        def heal(self, amount):
            pass

        def attack(self, item):
            pass


class AssistentHero(Hero):
    pass

class Enemy(Character, name="Bob", health=100, agility=10, dexterity=10, intelligence=1):
    pass


h = Hero(name="Batman", health=100, agility=10, dexterity=10, intelligence=10)
r = AssistentHero("Robin", 100, 2, 5, 8)


print(b.name)
print(r.name)

