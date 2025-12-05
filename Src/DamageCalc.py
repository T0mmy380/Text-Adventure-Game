from Monster import Monster

class DamageCalc:

    @staticmethod
    def calculate_damage(attacker: Monster, defender: Monster, type_chart) -> int:
        # Base damage formula
        base_damage = attacker.attack_power - defender.defense
        print(f"Base Damage (Attack - Defense): {attacker.attack_power} - {defender.defense} = {base_damage}")
        if base_damage < 0:
            base_damage = 0

        # Type effectiveness
        effectiveness = type_chart.get_effectiveness(attacker.type, defender.type)
        print(f"Type Effectiveness ({attacker.type} vs {defender.type}): {effectiveness}")
        damage = int(base_damage * effectiveness)
        print("Total Damage after applying effectiveness:", damage)

        return damage