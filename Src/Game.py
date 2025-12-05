from Util.monster_factory import MonsterFactory
from Util.damage_calc import DamageCalc
from Util.type_chart import TypeChart
import random

def main():
    
    dmgCalc = DamageCalc()
    chart = TypeChart()
     
    enemy = random.randrange(1, 19)
    monster1 = MonsterFactory.create(enemy)
    player = random.randrange(1, 19)
    monster2 = MonsterFactory.create(player)
    
    print("A wild monster appears!")
    monster1.show_info()
    print("\nYou send out your monster!")
    monster2.show_info()
    
    print("\n")
    monster1.stat_change('atk', 7)
    monster2.stat_change('def', -6)
    print("\n")
    
    
    monster1.show_info()
    print("\n")
    
    monster2.show_info()
    
    """
    print("\nWho attacks first?")
    print("0: Your Monster")
    print("1: Wild Monster")
    first = int(input("Enter 0 or 1: "))
    if first == 0:
        attacker, defender = monster2, monster1
    else:
        attacker, defender = monster1, monster2
    
    dmgCalc.calculate_damage(attacker, defender, chart)
    """
    
    
    
    
    
    
    

if __name__ == "__main__":
    main()
