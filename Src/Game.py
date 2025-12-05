from TypeChart import TypeChart
from DamageCalc import DamageCalc
import random

from Util.MonsterDex import MonsterDex

def main():

    chart = TypeChart()
    dmgCalc = DamageCalc()
    dex = MonsterDex()
    attacker = None
    defender = None

    # Random Monster enemy
    enemy = random.randrange(1, 19)
    #defender = MonsterDex.MONSTER_DEX[enemy]

    # Player Monster choice
    print("Choose your Monster:")
    print("1: Normal Monster")
    print("2: Fire Monster")
    print("3: Water Monster")
    print("4: Grass Monster")
    print("5: Electric Monster")
    print("6: Ice Monster")
    print("7: Fighting Monster")
    print("8: Poison Monster")
    print("9: Ground Monster")
    print("10: Flying Monster")
    print("11: Psychic Monster")
    print("12: Bug Monster")
    print("13: Rock Monster")
    print("14: Ghost Monster")
    print("15: Dragon Monster")
    print("16: Dark Monster")
    print("17: Steel Monster")
    print("18: Fairy Monster")
    choice = int(input("Enter the number of your choice: "))
    #attacker = MonsterDex.MONSTER_DEX[choice]

    print("\nYour Monster:")
    #attacker.show_info()
    print("\nEnemy Monster:")
    #defender.show_info()
    
    dex.list_monsters()
    
    

   




if __name__ == "__main__":
    main()
