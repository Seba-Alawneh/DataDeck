from abc import ABC, abstractmethod
from ex0 import CreatureFactory
from ex0.factories import Creature

class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
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

class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")
        
    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"
        
    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"

class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")
        
    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"
        
    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"

class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
        TransformCapability.__init__(self)
        
    def attack(self) -> str:
        if self.isTrans:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."
        
    def transform(self) -> str:
        self.isTrans = True
        return "Shiftling shifts into a sharper form!"
        
    def revert(self) -> str:
        self.isTrans = False
        return "Shiftling returns to normal."

class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)
        
    def attack(self) -> str:
        if self.isTrans:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."
        
    def transform(self) -> str:
        self.isTrans = True
        return "Morphagon morphs into a dragonic battle form!"
        
    def revert(self) -> str:
        self.isTrans = False
        return "Morphagon stabilizes its form."

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()

class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
