import json
import os
from monster import Monster

class MonsterFactory:
    # raw JSON data, not Monster objects
    _monster_data: dict[str, dict] = {}

    @classmethod
    def _load_if_needed(cls):
        """Load monsters.json once, when first needed."""
        if cls._monster_data:
            return  # already loaded

        # Find resources/monsters.json relative to *this* file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "..", "..", "resources", "monsters.json")

        with open(file_path, "r") as f:
            cls._monster_data = json.load(f)

    @classmethod
    def create(cls, ref) -> Monster:
        """
        Create a Monster from monsters.json.

        - If ref is a str: treat it as the JSON key (e.g. "fire_monster")
        - If ref is an int: treat it as the monster's numeric id
        """
        cls._load_if_needed()

        data = None

        if isinstance(ref, str):
            data = cls._monster_data.get(ref)

        elif isinstance(ref, int):
            # search by "id" field
            for entry in cls._monster_data.values():
                if entry["id"] == ref:
                    data = entry
                    break

        if data is None:
            raise KeyError(f"Monster '{ref}' not found in monsters.json")

        # Build and return a Monster object
        return Monster(
            mon_id=data["id"],
            name=data["name"],
            types=data["type"],        # keep as string for now
            health=data["health"],
            attack_power=data["attack_power"],
            defense=data["defense"],
            speed=data["speed"],
            ability=data["ability"],
            move_list=data["move_list"],
        )
