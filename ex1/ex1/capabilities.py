from abc import ABC, abstractmethod
from ex0 import CreatureFactory
from ex0.factories import Creature

class HealCapability(ABC):
    @abstractmethod
    def heal(self, target:str) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self):
        self.isTrans = False
    @abstractmethod
    def transform(self) -> str:
        pass
    @abstractmethod
    def revert(self) -> str:
        pass

class Sproutling (Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")
    def attack(self):
        print("uses Vine Whip!")
    def heal(self):
        print("Sproutling heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")
    def attack(self):
        return"uses Vine Whip!"
    def heal(self):
        return"Bloomelle heals itself and others for a large amount"


class HealingCreatureFactory (CreatureFactory):

class Morphagon():
