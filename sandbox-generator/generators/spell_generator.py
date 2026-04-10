import random
from . import spell_logic

class SpellGenerator:
    def __init__(self, registry):
        self.registry = registry

    def generate_spell(self, is_attack=None):
        """Generates a unique spell name and its general effect."""
        if is_attack is None:
            is_attack = random.random() < 0.5
        
        if is_attack:
            name = self.generate_attack_name()
        else:
            name = self.generate_arcane_name() # Just a placeholder for now if we want non-attack names

        effect = self.generate_general_effect()
        command = self.generate_command_word()
        
        return {
            "name": name,
            "effect": effect,
            "command": command
        }

    def generate_attack_name(self):
        """Rolls on Table 3-172: Attack Spells."""
        p1 = random.choice(spell_logic.ATTACK_PART_ONE)
        p2 = random.choice(spell_logic.ATTACK_PART_TWO)
        return f"{p1} {p2}"

    def generate_arcane_name(self):
        """Fallback for non-attack names or flavored arcane names."""
        prefixes = ["Greater", "Lesser", "Superior", "Inferior", "Ancient", "Lost", "Celestial", "Abyssal"]
        suffixes = ["Aura", "Shield", "Ward", "Blast", "Warp", "Link", "Surge", "Sigil"]
        return f"{random.choice(prefixes)} {random.choice(suffixes)}"

    def generate_general_effect(self):
        """Rolls on Table 3-173: Generalized Spell Effects."""
        roll = spell_logic.roll_d100()
        return spell_logic.GENERAL_EFFECTS.get(roll, "Surprising effect")

    def generate_command_word(self):
        """Rolls on Table 3-174: Command Words."""
        p1 = random.choice(spell_logic.COMMAND_FIRST)
        p2 = random.choice(spell_logic.COMMAND_SECOND)
        p3 = random.choice(spell_logic.COMMAND_ENDING)
        return f"{p1} {p2} {p3}"
