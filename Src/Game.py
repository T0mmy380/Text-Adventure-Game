from Src.TypeChart import TypeChart
from DamageCalc import DamageCalc
import random

from Src.Util.MonsterDex import MonsterDex


def main():

    chart = TypeChart()
    dmgCalc = DamageCalc()
    attacker = None
    defender = None

    # Random Monster enemy
    enemy = random.randrange(0, 3)
    defender = MonsterDex.MONSTER_DEX[enemy]

    # Player Monster choice
    print("Choose your Monster:")
    print("0: GrassMonster")
    print("1: WaterMonster")
    print("2: FireMonster")
    choice = int(input("Enter the number of your choice: "))
    attacker = MonsterDex.MONSTER_DEX[choice]

    print("\nYour Monster:")
    attacker.show_info()
    print("\nEnemy Monster:")
    defender.show_info()

    # Battle loop
    # Who attacks first
    print("Choose who attacks first:")
    print("0: You")
    print("1: Enemy")
    first = int(input("Enter the number of your choice: "))

    if first == 0:
        dmgCalc.calculate_damage(attacker, defender, chart)
    else:
        dmgCalc.calculate_damage(defender, attacker, chart)




if __name__ == "__main__":
    main()
