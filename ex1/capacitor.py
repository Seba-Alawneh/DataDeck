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

class Bloomelle(Creature, HealCapability):


class HealingCreatureFactory (CreatureFactory)