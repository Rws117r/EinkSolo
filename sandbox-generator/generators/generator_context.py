from ecs import Registry
from generators.alchemy_generator import AlchemyGenerator
from generators.wizard_generator import WizardGenerator
from generators.tower_generator import TowerGenerator
from generators.item_generator import ItemGenerator
from generators.book_generator import BookGenerator
from generators.religion_generator import ReligionGenerator
from generators.relic_generator import RelicGenerator
from generators.tavern_generator import TavernGenerator
from generators.abbey_generator import AbbeyGenerator
from generators.guild_generator import GuildGenerator
from generators.house_generator import HouseGenerator
from generators.landmark_generator import LandmarkGenerator
from generators.monarch_generator import MonarchGenerator
from generators.dragon_generator import DragonGenerator
from generators.spell_generator import SpellGenerator
from generators.village_generator import VillageGenerator
from generators.city_generator import CityGenerator
from generators.hamlet_generator import HamletGenerator
from generators.castle_generator import CastleGenerator
from generators.dungeon_generator import DungeonGenerator
from generators.lair_generator import LairGenerator
from generators.dungeon_room_generator import DungeonRoomGenerator
from generators.dungeon_level_generator import DungeonLevelGenerator
from generators.hook_generator import HookGenerator
from generators.dialogue_generator import DialogueGenerator
from generators.gem_generator import GemGenerator
from generators.trap_generator import TrapGenerator
from generators.dressing_generator import DressingGenerator

class GeneratorContext:
    """
    A centralized suite of generators to avoid redundant instantiation 
    and provide global context for world-wide lore.
    """
    def __init__(self, registry: Registry):
        self.registry = registry
        
        # Level 2 (Lore and Atomic)
        self.religion_gen = ReligionGenerator(self)
        self.item_gen = ItemGenerator(self)
        self.book_gen = BookGenerator(self)
        self.wiz_gen = WizardGenerator(self)
        self.alchemy_gen = AlchemyGenerator(self.registry)
        self.spell_gen = SpellGenerator(self.registry)
        self.gem_gen = GemGenerator(self)
        self.trap_gen = TrapGenerator(self)
        self.dressing_gen = DressingGenerator(self)
        
        # Level 3 (Structural & Specialized)
        self.relic_gen = RelicGenerator(self)
        self.tavern_gen = TavernGenerator(self)
        self.house_gen = HouseGenerator(self)
        self.guild_gen = GuildGenerator(self)
        self.land_gen = LandmarkGenerator(self)
        self.mon_gen = MonarchGenerator(self)
        self.dra_gen = DragonGenerator(self)
        
        # Level 4 (Sub-Orchestrators)
        self.room_gen = DungeonRoomGenerator(self)
        self.level_gen = DungeonLevelGenerator(self)
        self.hook_gen = HookGenerator(self)
        self.dial_gen = DialogueGenerator(self)
        
        # Level 5 (Complex Organizations)
        self.abbey_gen = AbbeyGenerator(self) 
        self.tow_gen = TowerGenerator(self)
        self.vil_gen = VillageGenerator(self)
        self.cit_gen = CityGenerator(self)
        self.ham_gen = HamletGenerator(self)
        self.cas_gen = CastleGenerator(self)
        self.dun_gen = DungeonGenerator(self)
        self.lair_gen = LairGenerator(self)
