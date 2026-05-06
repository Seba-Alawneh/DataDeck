from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import DefensiveStrategy, AggressiveStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print("* Battle *")
            print(creature1.describe())
            print("VS.")
            print(creature2.describe())
            print("now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    trans_factory = TransformCreatureFactory()
    normal_strat = NormalStrategy()
    defensive_strat = DefensiveStrategy()
    aggressive_strat = AggressiveStrategy()
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents_0 = [
        (flame_factory, normal_strat),
        (heal_factory, defensive_strat)
    ]
    battle(opponents_0)
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_1 = [
        (flame_factory, aggressive_strat),
        (heal_factory, defensive_strat)
    ]
    battle(opponents_1)
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents_2 = [
        (aqua_factory, normal_strat),
        (heal_factory, defensive_strat),
        (trans_factory, aggressive_strat)
    ]
    battle(opponents_2)


if __name__ == '__main__':
    main()
