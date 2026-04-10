from ecs import Registry
from components import (
    LevelComponent, NameComponent, IdentityComponent, 
    SpecialtyComponent, AppearanceComponent, GoalComponent, 
    StaffComponent, GenderComponent, TowerComponent, ApprenticeComponent, TowerLevelComponent,
    DragonComponent, TavernComponent, TavernNPCComponent, MenuComponent, HouseComponent, GuildComponent, ItemComponent, AbbeyComponent, RelicComponent, CastleComponent, MonarchComponent, BookComponent, DeityComponent, PantheonComponent, HamletComponent, VillageComponent, CityComponent,
    DungeonComponent, DungeonLevelComponent, HookComponent, DialogueComponent
)

from generators import hex_logic, dungeon_logic
from generators.hex_generator import HexGenerator
from generators.village_generator import VillageGenerator
from generators.city_generator import CityGenerator
from generators.hamlet_generator import HamletGenerator
from generators.castle_generator import CastleGenerator
from generators.tower_generator import TowerGenerator
from generators.abbey_generator import AbbeyGenerator

def main():
    registry = Registry()
    
    # 1) World Orchestrator (owns the Context)
    hex_gen = HexGenerator(registry)
    ctx = hex_gen.context

    print("\n--- Generating Mythology (Foundation) ---")
    creator = ctx.religion_gen.generate_creator_deity()
    ctx.religion_gen.generate_pantheon("The High Kingdom", creator)
    ctx.religion_gen.generate_pantheon("The Wild Tribes")

    print("\n--- Generating 10 Wizards ---")
    for _ in range(10):
        ctx.wiz_gen.generate_wizard()

    print("\n--- Generating 3 Towers ---")
    for _ in range(3):
        ctx.tow_gen.generate_tower()

    print("\n--- Generating 1 Dragon ---")
    ctx.dra_gen.generate_dragon()

    print("\n--- Generating 1 Tavern ---")
    ctx.tavern_gen.generate_tavern()

    print("\n--- Generating 2 Houses ---")
    ctx.house_gen.generate_house("Peasant")
    ctx.house_gen.generate_house("Noble")

    print("\n--- Generating 1 Guild ---")
    ctx.guild_gen.generate_guild()

    print("\n--- Generating 5 General Items ---")
    for _ in range(5):
        ctx.item_gen.generate_item()

    print("\n--- Generating 2 Abbeys (Linked to Gods) ---")
    ctx.abbey_gen.generate_abbey()
    ctx.abbey_gen.generate_abbey()

    print("\n--- Generating 1 Standalone Relic ---")
    ctx.relic_gen.generate_relic()

    print("\n--- Generating 1 Castle ---")
    ctx.cas_gen.generate_castle()

    print("\n--- Generating 5 Monarchs ---")
    for _ in range(5):
        ctx.mon_gen.generate_monarch()

    print("\n--- Generating 5 Legendary Books ---")
    for _ in range(5):
        ctx.book_gen.generate_book()

    print("\n--- Generating 3 Adventure Hooks ---")
    from components import HookComponent
    for _ in range(3):
        h = ctx.hook_gen.generate_hook()
        h_comp = ctx.registry.get_component(h, HookComponent)
        print(f"      - Hook: {h_comp.description}")

    print("\n--- Generating 1 Hamlet ---")
    ctx.ham_gen.generate_hamlet()

    print("\n--- Generating 1 Village ---")
    ctx.vil_gen.generate_village()

    print("\n--- Generating 1 City ---")
    ctx.cit_gen.generate_city()

    print("\n--- Generating 19-Hex Map (The Snowflake) ---")
    hex_gen.generate_map()
    
    print("\n--- Standalone Dungeon Area ---")
    ctx.dun_gen.generate_new_area("The Echoing Crypts")

    print("\n--- Generating Random Traps ---")
    ctx.trap_gen.generate_trap("mechanical")
    ctx.trap_gen.generate_trap("magical")
    ctx.trap_gen.generate_trap("natural")
    ctx.trap_gen.generate_trap("complex")

    print("\n--- Generating Dressing ---")
    ctx.dressing_gen.generate_container()
    ctx.dressing_gen.generate_container()
    ctx.dressing_gen.generate_furniture()
    ctx.dressing_gen.generate_furniture()

    # --- DISPLAY LOGIC ---

    # Helper for ID resolution
    def get_c(eid, ctype):
        ent = registry.get_entity_by_id(eid)
        return registry.get_component(ent, ctype) if ent else None

    # Display Towers
    for entity in registry.view(TowerComponent, NameComponent):
        tower = registry.get_component(entity, TowerComponent)
        print(f"\nGenerated Tower: {tower.name}")
        print(f"  Appearance: {tower.shape} {tower.material} tower")
        if tower.details:
            print(f"  Details: {', '.join(tower.details)}")
        print(f"  Internal Connection: {tower.connection}")
        
        # Resident
        res_comp = get_c(tower.resident_id, NameComponent)
        res_name = res_comp.name if res_comp else "Unknown"
        print(f"  Resident: {res_name}")

        # Display Levels
        levels = []
        for level_entity in registry.view(TowerLevelComponent):
            lvl = registry.get_component(level_entity, TowerLevelComponent)
            if lvl.tower_id == entity.id:
                levels.append(lvl)
        
        def level_sort_key(l):
            order = {"Top": 0, "Aboveground": 1, "Ground": 2, "Underground": 3, "Bottom": 4}
            idx = -l.level_index if l.level_type == "Aboveground" else l.level_index
            return (order[l.level_type], idx)
        
        levels.sort(key=level_sort_key)
        
        print("  Levels:")
        for lvl in levels:
            lvl_name = f"{lvl.level_type} {lvl.level_index}" if lvl.level_index > 0 else lvl.level_type
            print(f"    - [{lvl_name}] {lvl.usage}")
            print(f"      Appearance: {lvl.appearance}, Equipment: {lvl.equipment}")

    # Display Apprentices
    print("\n--- Apprentices ---")
    apps = registry.view(ApprenticeComponent, NameComponent)
    if not apps:
        print("No apprentices generated this run.")
    for entity in apps:
        app = registry.get_component(entity, ApprenticeComponent)
        app_name = registry.get_component(entity, NameComponent).name
        master_comp = get_c(app.master_id, NameComponent)
        master_name = master_comp.name if master_comp else "Unknown Master"
        print(f"Apprentice: {app_name} (Level {app.level})")
        print(f"  Studying under: {master_name}")
        
    # Display Dragons
    for entity in registry.view(DragonComponent, NameComponent):
        dragon = registry.get_component(entity, DragonComponent)
        print(f"\nGenerated Dragon: {dragon.name}")
        print(f"  {dragon.age} {dragon.size} {dragon.color} Dragon ({dragon.alignment})")
        print(f"  Breath: {dragon.breath}, AC: {dragon.ac}, HP: {dragon.hp}")
        print(f"  Saving Throw: Fighter {dragon.saving_throw}, Morale: {dragon.morale}")
        print(f"  Status: {dragon.status}")
        print(f"  Favorite Food: {dragon.food}")
        print(f"  Lair: {dragon.lair}")

    # Display Taverns
    for entity in registry.view(TavernComponent, NameComponent):
        tav = registry.get_component(entity, TavernComponent)
        print(f"\nGenerated Tavern: {tav.name}")
        print(f"  Decor: {', '.join(tav.decorations)}")
        print(f"  Patrons: Mostly {tav.patrons_most}, Notable: {tav.specific_customer}")
        print(f"  Entertainment: {tav.entertainers}")
        print(f"  Activities: {', '.join(tav.activities)}")
        print(f"  Best Room: {tav.best_room}")
        print(f"  Outside: {', '.join(tav.amenities)}")
        
        s = tav.sign
        print(f"  Sign: {s['shape']} ({s['material']}), {s['position']} via {s['mounting']}")
        print(f"        Content: {s['illustration']}, Sub-panel: {s['subpanel']}, Feature: {s['special']}")

        print("  Staff:")
        for npc_entity in registry.view(TavernNPCComponent):
            npc = registry.get_component(npc_entity, TavernNPCComponent)
            if npc.tavern_id == entity.id:
                name = registry.get_component(npc_entity, NameComponent).name
                print(f"    - {name} ({npc.role}): {', '.join(npc.traits)}")

        for menu_entity in registry.view(MenuComponent):
            menu = registry.get_component(menu_entity, MenuComponent)
            if menu.tavern_id == entity.id:
                print(f"  Menu ({menu.menu_type}):")
                for cat, val in menu.items.items():
                    if isinstance(val, list):
                        print(f"    - {cat}: {', '.join(val)}")
                    else:
                        print(f"    - {cat}: {val}")

    # Display Houses
    for entity in registry.view(HouseComponent, NameComponent):
        house = registry.get_component(entity, HouseComponent)
        print(f"\nGenerated House: {house.house_type}")
        print(f"  Description: {house.description}")
        print(f"  Levels: {house.levels}")
        if isinstance(house.rooms, dict):
            print("  Layout:")
            for floor, rooms in house.rooms.items():
                print(f"    - {floor}: {', '.join(rooms)}")
        else:
            print(f"  Rooms: {', '.join(house.rooms)}")
        print(f"  Loot Found (1d6): {house.loot}")

    # Display Guilds
    for entity in registry.view(GuildComponent, NameComponent):
        guild = registry.get_component(entity, GuildComponent)
        print(f"\nGenerated Guild: {guild.name}")
        print(f"  Field: {guild.field} ({guild.sub_field})")
        print(f"  Expertise: {guild.expertise}")
        print(f"  Power Metrics:")
        for k, v in guild.power.items():
            print(f"    - {k}: {v}")
        print(f"  Members:")
        for k, v in guild.members.items():
            print(f"    - {k}: {v}")
        if guild.event:
            print(f"  Current Event: {guild.event}")

    # Display General Items
    print("\n--- General Items ---")
    for entity in registry.view(ItemComponent, NameComponent):
        item = registry.get_component(entity, ItemComponent)
        print(f"  [Item] {item.name}")

    # Display Mythology
    print("\n--- Deities & Religions ---")
    for entity in registry.view(PantheonComponent, NameComponent):
        p = registry.get_component(entity, PantheonComponent)
        print(f"  [{p.culture_name}] {p.pattern}")
        lead_id = p.lead_deity_id.id if hasattr(p.lead_deity_id, "id") else p.lead_deity_id
        lead = get_c(lead_id, DeityComponent)
        if lead:
            print(f"    Lead Deity: {lead.name} ({', '.join(lead.areas)})")
            print(f"      Myth: {lead.description}")
        print(f"    Other Native Gods:")
        for d_ref in p.deities:
            d_id = d_ref.id if hasattr(d_ref, "id") else d_ref
            if d_id == lead_id: continue
            d = get_c(d_id, DeityComponent)
            if d:
                print(f"      - {d.name}: {', '.join(d.areas)}")

    # Display Abbeys
    print("\n--- Abbeys ---")
    for entity in registry.view(AbbeyComponent, NameComponent):
        a = registry.get_component(entity, AbbeyComponent)
        deity_str = ""
        if a.deity_id:
            d = get_c(a.deity_id, DeityComponent)
            if d:
                deity_str = f" [Dedicated to {d.name}]"
        
        print(f"  [Abbey] {a.name}{deity_str}")
        print(f"    Size: {a.size} ({a.pop} {a.residents_type})")
        print(f"    Leader: {a.leader_title} (Cleric Level {a.leader_level})")
        print(f"    Locations: {', '.join(a.locations[:8])}...")
        print(f"    Activities: {', '.join(a.activities)}")
        if a.fame:
            print(f"    Fame: {a.fame}")
        if a.history:
            print(f"    History: {a.history}")
        if a.event:
            print(f"    Current Event: {a.event}")
        if a.relic_id:
            relic_comp = get_c(a.relic_id, RelicComponent)
            if relic_comp:
                print(f"    Relic: {relic_comp.name} (Spell: {relic_comp.spell_name})")

    # Display Hamlets
    print("\n--- Hamlets ---")
    for entity in registry.view(HamletComponent):
        c = registry.get_component(entity, HamletComponent)
        ident = registry.get_component(entity, NameComponent)
        print(f"  [{ident.name}] Main Building: {c.main_building}")
        print(f"    Disposition: {c.disposition}")
        if c.secret:
            print(f"    Secret: They are {c.secret}!")
        print(f"    Surrounding Houses ({len(c.house_ids)}):")
        for h_id in c.house_ids:
            h_comp = get_c(h_id, HouseComponent)
            if h_comp:
                print(f"      - {h_comp.house_type} House ({h_comp.levels})")

    # Display Villages
    for entity in registry.view(VillageComponent, NameComponent):
        v = registry.get_component(entity, VillageComponent)
        ident = registry.get_component(entity, NameComponent)
        print(f"\n  [{ident.name}] Size: {v.size} (Grade {v.grade}, Pop ~{v.population})")
        print(f"    Occupations: {', '.join(v.occupations)}")
        print(f"    Ruler: {v.ruler} ({v.ruler_disp})")
        print(f"    Villager Disposition: {v.villager_disp}")
        if v.secret:
            print(f"    Secret: They are {v.secret}!")
        if v.event:
            print(f"    Event: {v.event['nature']} ({v.event['timing']})")
        
        print(f"    Pride: {v.pride}")
        print(f"    Draft Animals: {v.draft_animal}")
        print(f"    Culture: Gravity={v.cultural_gravity}, Behavior={v.odd_behavior}")
        print(f"    Custom: {v.strange_dress}")
        
        print(f"    Notable NPCs ({len(v.npcs)}):")
        for npc in v.npcs:
            print(f"      - {npc}")
            
        print(f"    Defenses: {', '.join(v.defenses)} ({v.guards} guards)")
        
        print(f"    Points of Interest ({len(v.poi_ids) + len(v.special_pois)}):")
        for poi in v.special_pois:
            print(f"      - {poi}")
        for p_id in v.poi_ids:
            p_name_comp = get_c(p_id, NameComponent)
            p_ident_comp = get_c(p_id, IdentityComponent)
            if p_name_comp and p_ident_comp:
                print(f"      - [{p_ident_comp.entity_class}] {p_name_comp.name}")

    # Display Cities
    for entity in registry.view(CityComponent, NameComponent):
        v = registry.get_component(entity, CityComponent)
        ident = registry.get_component(entity, NameComponent)
        print(f"\n  [{ident.name}] Size: {v.size} (Grade {v.grade}, Pop ~{v.population})")
        print(f"    Occupations: {', '.join(v.occupations)}")
        print(f"    Characteristics: {', '.join(v.characteristics)}")
        print(f"    Appearance: {v.appearance}")
        print(f"    Ruler: {v.ruler} ({v.ruler_disp})")
        print(f"    Villager Disposition: {v.villager_disp}")
        if v.event:
            print(f"    Event: {v.event['nature']} ({v.event['timing']})")
            
        print(f"    Pride: {v.pride}")
        print(f"    Draft Animals: {v.draft_animal}")
        print(f"    Culture: Gravity={v.cultural_gravity}, Behavior={v.odd_behavior}")
        print(f"    Custom: {v.strange_dress}")
        print(f"    Latest News: {v.latest_news or 'None'}")
        print(f"    Faction War: {v.faction_war or 'None'}")
        print(f"    Cultural Change: {v.cultural_change or 'None'}")
        print(f"    Districts ({len(v.districts)}): {', '.join(v.districts)}")
        print(f"    Prison: {v.prison}")
        print(f"    Interesting Street: {v.interesting_street}")
        
        print(f"    Notable NPCs ({len(v.npcs)}):")
        for npc in v.npcs:
            print(f"      - {npc}")
            
        print(f"    Military: {v.guards} guards, {v.supplies} months supplies")
        if v.walled:
            print(f"    Defenses: Stone walls with {len(v.entrances)} entrances ({', '.join(v.entrances)})")
            print(f"      Entrances are guarded by 2 towers and {v.entrance_defenses}")
        
        print(f"    Buildings of Interest ({len(v.buildings)}):")
        for b in v.buildings:
            print(f"      - {b['name']} ({b['type']})")

        print(f"    Points of Interest (General counts):")
        for p_type, count in v.poi_counts.items():
            print(f"      - {p_type.capitalize()}: {count}")

        if v.special_pois:
            print(f"    Special Locations:")
            for sp in v.special_pois:
                print(f"      - {sp}")

    # Display Relics
    print("\n--- Standalone Relics ---")
    for entity in registry.view(RelicComponent, NameComponent):
        relic = registry.get_component(entity, RelicComponent)
        attached = False
        for a_entity in registry.view(AbbeyComponent):
            ab = registry.get_component(a_entity, AbbeyComponent)
            if ab.relic_id == entity.id:
                attached = True
                break
        if not attached:
            print(f"  [Relic] {relic.name}")
            if relic.spell_name:
                print(f"    Can cast {relic.spell_name} (Level {relic.spell_level})")

    # Display Castles
    print("\n--- Castles ---")
    for entity in registry.view(CastleComponent, NameComponent):
        castle = registry.get_component(entity, CastleComponent)
        print(f"  [Castle] {castle.name}")
        print(f"    Type: {castle.type_name}")
        print(f"    Unusual Feature: {castle.unusual}")
        print(f"    Condition: {castle.condition}, Disposition: {castle.disposition}")
        if castle.keep:
            k = castle.keep
            print(f"    Keep: {k['shape']}, {k['levels']} levels")
            print(f"      Treasure: {', '.join(k['treasure'])}")
        print(f"    Extra Defenses: {', '.join(castle.defenses)}")
        
        g = castle.garrison
        print(f"    Garrison ({g['Total Fighters']} fighters): {g['Lord']}")
            
        print(f"    Specialized Staff:")
        for job, desc in castle.people[:3]:
            print(f"      - {job}: {desc}")
            
    # Display Monarchs
    print("\n--- Monarchs & Nobility ---")
    for entity in registry.view(MonarchComponent, NameComponent):
        m = registry.get_component(entity, MonarchComponent)
        print(f"  [{m.base_title}] {m.name} ({m.monarch_type})")
        print(f"    Official Title: {m.official_term}")
        print(f"    Sovereign Mode of Address: {m.fantasy_address}")

    # Display Books
    print("\n--- Legendary Books & Tomes ---")
    for entity in registry.view(BookComponent, NameComponent):
        b = registry.get_component(entity, BookComponent)
        print(f"  [Book] {b.title}")

    # Display Hex Map
    from components import HexComponent, FactionComponent
    from generators import hex_logic
    # --- DUNGEON CROSS SECTION ---
    print("\n--- MEGADUNGEON CROSS SECTION ---")
    dungeon_entities = registry.view(DungeonComponent)
    # Sort by area_id
    dungeon_entities.sort(key=lambda e: registry.get_component(e, DungeonComponent).area_id)
    
    for d_ent in dungeon_entities:
        d_comp = registry.get_component(d_ent, DungeonComponent)
        d_name = registry.get_component(d_ent, NameComponent).name
        print(f"\n[Area {d_comp.area_id}] {d_name}")
        print(f"  Theme: {d_comp.theme} ({dungeon_logic.THEME_DETAILS.get(d_comp.theme, 'No special effects')})")
        
        # Sort levels by depth
        levels = [registry.get_entity_by_id(l_id) for l_id in d_comp.level_ids]
        levels.sort(key=lambda l: registry.get_component(l, DungeonLevelComponent).depth)
        
        for l_ent in levels:
            l_comp = registry.get_component(l_ent, DungeonLevelComponent)
            # Custom roman numerals
            roman = ["I", "II", "III", "IV", "V", "VI"][l_comp.depth - 1]
            
            print(f"  Level Depth {roman}:")
            print(f"    Factions: {', '.join([f['type'] + ' (L' + str(f['level']) + ')' for f in l_comp.factions])}")
            print(f"    Wandering table: {', '.join(l_comp.wandering_monsters)}")
            print(f"    Rooms: {len(l_comp.room_ids)}")
            if l_comp.links:
                for link in l_comp.links:
                    t_ent = registry.get_entity_by_id(link['to'])
                    t_comp = registry.get_component(t_ent, DungeonLevelComponent)
                    secret_str = " (SECRET)" if link['secret'] else ""
                    print(f"    -> Linked to Area {t_comp.area_id} Depth {['I','II','III','IV','V','VI'][t_comp.depth-1]}{secret_str}")

    print("\n--- HEX MAP (2-Mile Snowflake) ---")
    hex_entities = list(registry.view(HexComponent))
    # Sort hexes by q then r for a somewhat readable grid-ish output
    hex_entities.sort(key=lambda e: (registry.get_component(e, HexComponent).q, registry.get_component(e, HexComponent).r))
    
    for entity in hex_entities:
        h = registry.get_component(entity, HexComponent)
        symbol = hex_logic.BIOME_SYMBOLS.get(h.biome, "???")
        
        feature_str = "None"
        if h.feature_id:
            if isinstance(h.feature_id, str):
                feature_str = h.feature_id
            else:
                f_name = get_c(h.feature_id, NameComponent)
                f_ident = get_c(h.feature_id, IdentityComponent)
                
                if f_ident and f_ident.entity_class == "Landmark":
                    from components import LandmarkComponent
                    l = get_c(h.feature_id, LandmarkComponent)
                    if l:
                        feature_str = f"[{f_ident.entity_class}] {f_name.name} ({l.l_type} - {l.category}) | Content: {l.content}"
                        if l.detail:
                            feature_str += f" [{l.detail}]"
                        if l.treasure_chance > 0:
                            feature_str += f" | Treasure: {l.treasure_chance}%"
                elif f_ident and f_ident.entity_class == "Lair":
                    from components import LairComponent
                    l = get_c(h.feature_id, LairComponent)
                    if l:
                        feature_str = f"[{f_ident.entity_class}] {f_name.name} (Total: {l.total_count}, In: {l.inside_count}, Out: {l.outside_count}, 1d8-Pos: {l.location_relative})"
                else:
                    feature_str = f"[{f_ident.entity_class}] {f_name.name}" if f_name and f_ident else "Unknown Feature"
        
        faction_str = "Wilderness"
        if h.faction_id:
            fac = get_c(h.faction_id, FactionComponent)
            faction_str = fac.name if fac else "Unknown Faction"
            
        print(f"  Hex ({h.q},{h.r},{h.s}): {h.biome} [{symbol}] | Feature: {feature_str} | Domain: {faction_str}")

    # Display Factions & Diplomacy
    print("\n--- FACTIONS & REALMPOLITIK ---")
    for entity in registry.view(FactionComponent):
        f = registry.get_component(entity, FactionComponent)
        print(f"\n  [{f.name}] Territory: {len(f.hex_ids)} hexes")
        if f.active_event:
            print(f"    Current Event: {f.active_event['nature']} ({f.active_event['timing']})")
        
        if f.relationships:
            print("    Foreign Relations:")
            for target_id, rel in f.relationships.items():
                target_f = get_c(target_id, FactionComponent)
                t_name = target_f.name if target_f else "Unknown"
                print(f"      - {rel} with {t_name}")

    # Display Traps
    print("\n--- Traps ---")
    from generators.trap_generator import TrapComponent
    for entity in registry.view(TrapComponent, NameComponent):
        trap = registry.get_component(entity, TrapComponent)
        print(f"  {trap}")

    # Display Dressing
    print("\n--- Room Dressing (Containers & Furniture) ---")
    from generators.dressing_generator import ContainerComponent, FurnitureComponent
    for entity in registry.view(ContainerComponent):
        print(f"  {registry.get_component(entity, ContainerComponent)}")
    for entity in registry.view(FurnitureComponent):
        print(f"  {registry.get_component(entity, FurnitureComponent)}")

    print("\n--- Registry Global View ---")
    for entity in registry._entities:
        name_comp = registry.get_component(entity, NameComponent)
        ident_comp = registry.get_component(entity, IdentityComponent)
        if name_comp and ident_comp:
            dial = registry.get_component(entity, DialogueComponent)
            bark_str = f' | "{dial.bark}"' if dial else ""
            print(f"[{ident_comp.entity_class}] {name_comp.name}{bark_str}")

if __name__ == "__main__":
    main()
