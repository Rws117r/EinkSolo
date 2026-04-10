import random
from ecs import Registry
from components import NameComponent, IdentityComponent, TrapComponent
from generators import trap_logic

class TrapGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_trap(self, category="mechanical"):
        if category == "complex":
            return self.generate_complex_trap()
        elif category == "magical":
            return self.generate_magical_trap()
        elif category == "natural":
            return self.generate_natural_trap()
        
        trap_roll = trap_logic.roll_d100()
        trap_type = trap_logic.get_from_table(trap_logic.BASIC_MECHANICAL_TRAPS, trap_roll)
        
        conceal_roll = trap_logic.roll_d100()
        concealment = trap_logic.get_from_table(trap_logic.TRAP_CONCEALMENT, conceal_roll)
        
        trigger_roll = trap_logic.roll_d100()
        trigger = trap_logic.get_from_table(trap_logic.COMPLICATED_TRIGGER, trigger_roll)
        
        detail = None
        behavior = None
        
        trap_type_lower = trap_type.lower()
        
        if "gas" in trap_type_lower or "vent" in trap_type_lower or "chemical reaction" in trap_type_lower:
            detail = trap_logic.get_from_table(trap_logic.GAS_EFFECTS, trap_logic.roll_d100())
            behavior = trap_logic.get_from_table(trap_logic.GAS_BEHAVIORS, trap_logic.roll_d100())
        elif "missile" in trap_type_lower:
            m_type, m_spec = trap_logic.get_from_table(trap_logic.MISSILE_TRAPS, trap_logic.roll_d100())
            detail = f"Missile: {m_type}"
            if m_spec != "None": detail += f" ({m_spec})"
        elif "pit" in trap_type_lower:
            pit_type = trap_logic.get_from_table(trap_logic.PITS, trap_logic.roll_d100())
            detail = f"Pit: {pit_type}"
            if "liquid" in pit_type.lower():
                liq = trap_logic.get_from_table(trap_logic.TRAP_LIQUIDS, trap_logic.roll_d100())
                detail += f" ({liq})"

        return self._create_trap_entity(trap_type, concealment, trigger, detail, behavior)

    def generate_complex_trap(self):
        profile = trap_logic.get_from_table(trap_logic.COMPLEX_TRAP_PROFILE, trap_logic.roll_d6())
        
        stages = []
        
        # 1. The Draw
        if profile['draw'] != "None":
            if "Physical" in profile['draw']:
                draw_type = trap_logic.get_from_table(trap_logic.TRAP_DRAWS, trap_logic.roll_d100())
            else:
                draw_type = profile['draw'] # e.g. "Greed"
            stages.append(f"DRAW: {draw_type}")
            
        # 2. The Prison
        prison_cat = random.choice(list(trap_logic.TRAP_PRISONS.keys()))
        prison_type = trap_logic.get_from_table(trap_logic.TRAP_PRISONS[prison_cat], trap_logic.roll_d100())
        stages.append(f"PRISON ({profile['prison']}): {prison_type}")
        
        # 3. The Kill Mechanism
        kill_cat = random.choice(list(trap_logic.TRAP_KILL_MECHANISMS.keys()))
        kill_type = trap_logic.get_from_table(trap_logic.TRAP_KILL_MECHANISMS[kill_cat], trap_logic.roll_d100())
        life_measure = trap_logic.get_from_table(trap_logic.MEASURING_LIFE, trap_logic.roll_d100())
        stages.append(f"KILL ({profile['kill']}): {kill_type} (Measured by {life_measure})")
        
        # 4. Kill-Switch
        switch_type = trap_logic.get_from_table(trap_logic.KILL_SWITCH_WORKING, trap_logic.roll_d100())
        stages.append(f"SWITCH ({profile['switch']}): Found via {switch_type}")
        
        # 5. Complication
        if random.random() < 0.5:
            complication = trap_logic.get_from_table(trap_logic.MAGIC_WEAKNESS, trap_logic.roll_d100())
            stages.append(f"COMPLICATION: {complication}")
            
        trap_desc = " | ".join(stages)
        return self._create_trap_entity("Complex", "Integrated into Architecture", "Multi-stage sequence", trap_desc)

    def generate_magical_trap(self):
        profile, effect_category, trigger = trap_logic.get_from_table(trap_logic.MAGICAL_TRAPS, trap_logic.roll_d100())
        
        # Determine Trigger
        if "Magical Trigger" in profile:
            trigger_desc = trap_logic.get_from_table(trap_logic.MAGICAL_TRAP_TRIGGERS, trap_logic.roll_d100())
        else:
            trigger_desc = trap_logic.get_from_table(trap_logic.COMPLICATED_TRIGGER, trap_logic.roll_d100())
            
        # Determine Effect
        if "Magical Effect" in profile:
            effect = trap_logic.get_from_table(trap_logic.MAGICAL_TRAP_CORE_EFFECTS, trap_logic.roll_d100())
        else:
            effect = trap_logic.get_from_table(trap_logic.BASIC_MECHANICAL_TRAPS, trap_logic.roll_d100())
            
        # Special Effect
        special = trap_logic.get_from_table(trap_logic.MAGICAL_SPECIAL_EFFECTS, trap_logic.roll_d100())
        
        return self._create_trap_entity(f"Magical ({profile})", "Magical Sigil", trigger_desc, f"{effect}. Special: {special}")

    def generate_natural_trap(self):
        feature, rigging = trap_logic.get_from_table(trap_logic.RIGGED_NATURAL_FEATURES, trap_logic.roll_d100())
        return self._create_trap_entity("Natural", feature, rigging)

    def _create_trap_entity(self, trap_type, concealment, trigger, detail=None, behavior=None):
        trap_entity = self.registry.create_entity()
        comp = TrapComponent(trap_type, concealment, trigger, detail, behavior)
        self.registry.add_component(trap_entity, comp)
        self.registry.add_component(trap_entity, IdentityComponent("Trap"))
        self.registry.add_component(trap_entity, NameComponent(f"{trap_type} Trap"))
        return trap_entity
