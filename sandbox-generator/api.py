import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ecs import Registry
from generators.hex_generator import HexGenerator
from components import HexComponent, IdentityComponent, NameComponent

app = FastAPI()

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global registry in-memory for the session
registry = Registry()
hex_gen = HexGenerator(registry)

def serialize_value(val):
    if isinstance(val, uuid.UUID):
        return str(val)
    if isinstance(val, list):
        return [serialize_value(i) for i in val]
    if isinstance(val, dict):
        return {k: serialize_value(v) for k, v in val.items()}
    return val

def serialize_registry(reg: Registry):
    entities_data = []
    for entity in reg._entities:
        ent_data = {
            "id": str(entity.id),
            "components": {}
        }
        for comp_type, entity_map in reg._components.items():
            if entity in entity_map:
                comp = entity_map[entity]
                comp_name = comp_type.__name__
                # Extract all attributes from the component
                attrs = {k: serialize_value(v) for k, v in comp.__dict__.items() if not k.startswith("_")}
                ent_data["components"][comp_name] = attrs
        entities_data.append(ent_data)
    return entities_data

@app.get("/api/generate")
def generate_world():
    global registry, hex_gen
    registry = Registry()
    hex_gen = HexGenerator(registry)
    hex_gen.generate_map()
    return {"status": "success", "message": "World generated"}

@app.get("/api/world")
def get_world():
    return serialize_registry(registry)

@app.get("/api/hexes")
def get_hexgrid():
    hexes = []
    for entity in registry.view(HexComponent):
        h_comp = registry.get_component(entity, HexComponent)
        ident = registry.get_component(entity, IdentityComponent)
        name = registry.get_component(entity, NameComponent)
        
        hex_data = {
            "id": str(entity.id),
            "q": h_comp.q,
            "r": h_comp.r,
            "s": h_comp.s,
            "biome": h_comp.biome,
            "feature_id": str(h_comp.feature_id) if h_comp.feature_id else None,
            "faction_id": str(h_comp.faction_id) if h_comp.faction_id else None,
            "name": name.name if name else "Unknown Hex"
        }
        hexes.append(hex_data)
    return hexes

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
