# Core Components
class IdentityComponent:
    def __init__(self, identity):
        self.identity = identity
    def __str__(self): return self.identity

class NameComponent:
    def __init__(self, name):
        self.name = name
    def __str__(self): return self.name

# Wizard Components
class LevelComponent:
    def __init__(self, level):
        self.level = level

class SpecialtyComponent:
    def __init__(self, specialty):
        self.specialty = specialty

class AppearanceComponent:
    def __init__(self, appearance):
        self.appearance = appearance

class GoalComponent:
    def __init__(self, goal):
        self.goal = goal

class StaffComponent:
    def __init__(self, material, top, bottom, shape, detail, signature_spell=None):
        self.material = material
        self.top = top
        self.bottom = bottom
        self.shape = shape
        self.detail = detail
        self.signature_spell = signature_spell

    def __str__(self):
        spell_str = f" [Spell: {self.signature_spell['name']}]" if self.signature_spell else ""
        return f"{self.material} staff, {self.shape}, with {self.top} on top and {self.bottom} on bottom. {self.detail}.{spell_str}"

class GenderComponent:
    def __init__(self, gender):
        self.gender = gender

# World Structural Components
class TowerComponent:
    def __init__(self, name, material, shape, connection, details, resident_id=None):
        self.name = name
        self.material = material
        self.shape = shape
        self.connection = connection
        self.details = details
        self.resident_id = resident_id
        self.level_ids = []
        self.notable_ids = []

class TowerLevelComponent:
    def __init__(self, tower_id, level_type, index, usage, appearance, equipment):
        self.tower_id = tower_id
        self.level_type = level_type
        self.index = index
        self.usage = usage
        self.appearance = appearance
        self.equipment = equipment

class ApprenticeComponent:
    def __init__(self, master_id, level):
        self.master_id = master_id
        self.level = level

class AlchemyComponent:
    def __init__(self, ingredients, potions):
        self.ingredients = ingredients
        self.potions = potions

class CastleComponent:
    def __init__(self, name, type_name, unusual, condition, keep, defenses, gatehouse, moat, garrison, people, disposition, event):
        self.name = name
        self.type_name = type_name
        self.unusual = unusual
        self.condition = condition
        self.keep = keep
        self.defenses = defenses
        self.gatehouse = gatehouse
        self.moat = moat
        self.garrison = garrison
        self.people = people
        self.disposition = disposition
        self.event = event

class AbbeyComponent:
    def __init__(self, name, residents_type, leader_title, leader_level, size, pop, locations, activities, fame, history, event, relic_id, deity_id):
        self.name = name
        self.residents_type = residents_type
        self.leader_title = leader_title
        self.leader_level = leader_level
        self.size = size
        self.pop = pop
        self.locations = locations
        self.activities = activities
        self.fame = fame
        self.history = history
        self.event = event
        self.relic_id = relic_id
        self.deity_id = deity_id
        self.notable_ids = []

class TavernComponent:
    def __init__(self, name, decorations, patrons, specific_customer, entertainers, activities, best_room, special_room, amenities, sign, menu_id):
        self.name = name
        self.decorations = decorations
        self.patrons = patrons
        self.specific_customer = specific_customer
        self.entertainers = entertainers
        self.activities = activities
        self.best_room = best_room
        self.special_room = special_room
        self.amenities = amenities
        self.sign = sign
        self.menu_id = menu_id

class TavernNPCComponent:
    def __init__(self, tavern_id, role, traits):
        self.tavern_id = tavern_id
        self.role = role
        self.traits = traits

class MenuComponent:
    def __init__(self, tavern_id, menu_type, items):
        self.tavern_id = tavern_id
        self.menu_type = menu_type
        self.items = items

class DungeonComponent:
    def __init__(self, area_id, theme, level_ids):
        self.area_id = area_id
        self.theme = theme
        self.level_ids = level_ids

class DungeonLevelComponent:
    def __init__(self, area_id, depth, room_ids, factions, wandering_monsters):
        self.area_id = area_id
        self.depth = depth
        self.room_ids = room_ids
        self.factions = factions
        self.wandering_monsters = wandering_monsters
        self.links = []

class DungeonRoomComponent:
    def __init__(self, size, r_type, detail, treasure_chance, is_lair):
        self.size = size
        self.r_type = r_type
        self.detail = detail
        self.treasure_chance = treasure_chance
        self.is_lair = is_lair
        self.notable_ids = []

class LairComponent:
    def __init__(self, monster_type, total_count, inside_count, outside_count, location_relative, room_ids):
        self.monster_type = monster_type
        self.total_count = total_count
        self.inside_count = inside_count
        self.outside_count = outside_count
        self.location_relative = location_relative
        self.room_ids = room_ids

# Map Components
class HexComponent:
    def __init__(self, q, r, s, biome):
        self.q = q
        self.r = r
        self.s = s
        self.biome = biome
        self.feature_id = None
        self.faction_id = None

class FactionComponent:
    def __init__(self, name, leader_id):
        self.name = name
        self.leader_id = leader_id
        self.hex_ids = []
        self.relationships = {}
        self.active_event = None

# Minor Structural Components
class HouseComponent:
    def __init__(self, type, details):
        self.type = type
        self.details = details

class GuildComponent:
    def __init__(self, name, focus, activity):
        self.name = name
        self.focus = focus
        self.activity = activity

class LandmarkComponent:
    def __init__(self, l_type, category, nature, content, detail, treasure_chance):
        self.l_type = l_type
        self.category = category
        self.nature = nature
        self.content = content
        self.detail = detail
        self.treasure_chance = treasure_chance
        self.notable_ids = []

class MonarchComponent:
    def __init__(self, name, base_title, official_term, base_address, fantasy_address, gender, m_type):
        self.name = name
        self.base_title = base_title
        self.official_term = official_term
        self.base_address = base_address
        self.fantasy_address = fantasy_address
        self.gender = gender
        self.m_type = m_type

class DragonComponent:
    def __init__(self, name, age, color, personality):
        self.name = name
        self.age = age
        self.color = color
        self.personality = personality

# Settlement Components
class VillageComponent:
    def __init__(self, name, population, ruler):
        self.name = name
        self.population = population
        self.ruler = ruler

class CityComponent:
    def __init__(self, name, population, districts):
        self.name = name
        self.population = population
        self.districts = districts

class HamletComponent:
    def __init__(self, name, feature):
        self.name = name
        self.feature = feature

# Specialized Object Components
class BookComponent:
    def __init__(self, title, physical_detail, content, writing_style):
        self.title = title
        self.physical_detail = physical_detail
        self.content = content
        self.writing_style = writing_style

class RelicComponent:
    def __init__(self, full_name, powers, history):
        self.full_name = full_name
        self.powers = powers
        self.history = history

class ItemComponent:
    def __init__(self, item_name):
        self.item_name = item_name

class GemComponent:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class TrapComponent:
    def __init__(self, trap_type, concealment, trigger, detail=None, behavior=None):
        self.trap_type = trap_type
        self.concealment = concealment
        self.trigger = trigger
        self.detail = detail
        self.behavior = behavior

    def __str__(self):
        base = f"[{self.trap_type}] {self.concealment} (Trigger: {self.trigger})"
        if self.detail: base += f" | Detail: {self.detail}"
        if self.behavior: base += f" | Behavior: {self.behavior}"
        return base

# Deity Components
class DeityComponent:
    def __init__(self, name, role, areas, description, status=None):
        self.name = name
        self.role = role
        self.areas = areas
        self.description = description
        self.status = status

class PantheonComponent:
    def __init__(self, culture, pattern, lead_id, deity_ids):
        self.culture = culture
        self.pattern = pattern
        self.lead_id = lead_id
        self.deity_ids = deity_ids

# Utility Components
class DialogueComponent:
    def __init__(self, bark):
        self.bark = bark

class HookComponent:
    def __init__(self, description, source_entity_id=None):
        self.description = description
        self.source_entity_id = source_entity_id

class ContainerComponent:
    def __init__(self, container_type, description, special=None):
        self.container_type = container_type
        self.description = description
        self.special = special

    def __str__(self):
        base = f"[{self.container_type}] {self.description}"
        if self.special:
            base += f" | Feature: {self.special}"
        return base

class FurnitureComponent:
    def __init__(self, furniture_type, aspect):
        self.furniture_type = furniture_type
        self.aspect = aspect

    def __str__(self):
        return f"[Furniture] {self.furniture_type} ({self.aspect})"
