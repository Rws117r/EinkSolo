import random
from ecs import Registry
from components import GuildComponent, IdentityComponent, NameComponent
from generators import guild_logic

class GuildGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_guild(self):
        # 1) Field & Sub-field
        field_roll = random.randint(1, 8)
        field = guild_logic.FIELDS[field_roll]
        sub_field = random.choice(guild_logic.SUB_FIELDS[field])
        
        # 2) Expertise
        expertise = self._get_from_dict(guild_logic.EXPERTISE, random.randint(1, 12))
        
        # 3) Name
        name_template = self._get_from_dict(guild_logic.NAME_STRUCTURES, random.randint(1, 12))
        raw_field = sub_field
        name = name_template.format(field=raw_field)
        
        # 4) Power
        power = {
            "Renown": self._get_from_dict(guild_logic.RENOWN, random.randint(1, 12)),
            "Resources": self._get_from_dict(guild_logic.RESOURCES, random.randint(1, 12)),
            "Guildhouses": self._get_from_dict(guild_logic.GUILDHOUSES, random.randint(1, 6)),
            "Special Asset": self._get_from_dict(guild_logic.SPECIAL_ASSETS, random.randint(1, 12)),
            "Motivation": self._get_from_dict(guild_logic.MOTIVATION, random.randint(1, 8))
        }
        
        # 5) Members
        members = {
            "Initiation": guild_logic.INITIATIONS[self._roll_to_key(guild_logic.INITIATIONS, random.randint(1, 20))],
            "Appearance": guild_logic.APPEARANCES[self._roll_to_key(guild_logic.APPEARANCES, random.randint(1, 20))],
            "Quirk": guild_logic.QUIRKS[self._roll_to_key(guild_logic.QUIRKS, random.randint(1, 20))]
        }
        
        # 6) Event & 7) Problem (5 or 6 on 1d6)
        event = None
        if random.randint(1, 6) >= 5:
            if random.randint(1, 6) <= 4:
                event = random.choice(list(guild_logic.EVENTS_COMMON.values()))
            else:
                event = random.choice(list(guild_logic.EVENTS_FIELD[field].values()))
                
        problem = None
        if random.randint(1, 6) >= 5:
            if random.randint(1, 6) <= 4:
                problem = random.choice(list(guild_logic.PROBLEMS_COMMON.values()))
            else:
                problem = random.choice(list(guild_logic.PROBLEMS_FIELD[field].values()))

        # Create Entity
        guild = self.registry.create_entity()
        comp = GuildComponent(name, field, sub_field, expertise, power, members, event, problem)
        self.registry.add_component(guild, comp)
        self.registry.add_component(guild, NameComponent(name))
        self.registry.add_component(guild, IdentityComponent("Guild"))
        
        return guild

    def _get_from_dict(self, d, roll):
        keys = sorted(d.keys())
        last_val = d[keys[0]]
        for k in keys:
            if roll >= k:
                last_val = d[k]
            else:
                break
        return last_val

    def _roll_to_key(self, d, roll):
        keys = sorted(d.keys())
        last_key = keys[0]
        for k in keys:
            if roll >= k:
                last_key = k
            else:
                break
        return last_key
