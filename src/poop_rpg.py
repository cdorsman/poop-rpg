#!/usr/bin/env python3

from abc import ABC
from random import choice
from time import sleep

class BaseCharacter(ABC, abstractmethod):
    def __init__(self):
        self.health = 100
        self.speed = 0
        self.dexterity = 0
        self.intelligence = 0
        self.agility = 0

        self.inventory = []

    @property
    @abstractmethod
    def attack(self, entity):
        ...

    @property
    @abstractmethod
    def take_damage(self, amount):
        ...

    @property
    @abstractmethod
    def block(self, entity):
        ...

    @property
    @abstractmethod
    def heal(self, amount):
        ...

def main():
    ...


if __name__ == '__main__':
    main()
