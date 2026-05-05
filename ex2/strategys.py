from abc import ABC, abstractmethod
from ex1.capabilities import HealCapability, TransformCapability

class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass
    @abstractmethod
    def act(self, creature) -> None:
        pass
   


class  NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return True
    def act(self, creature) -> None:
        print(creature.attack())


class  AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)
    
    def act(self, creature) -> None:
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

class  DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)
    
    def act(self, creature) -> None:
        print(creature.attack())
        print(creature.heal())
