class Entity:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"Entity({self.id})"

class Registry:
    def __init__(self):
        self._entities = {} # id -> {ComponentClass: instance}
        self._next_id = 1

    def create_entity(self):
        ent = Entity(self._next_id)
        self._entities[ent.id] = {}
        self._next_id += 1
        return ent

    def get_entity_by_id(self, entity_id):
        if entity_id in self._entities:
            return entity_id # In this minimal version, the ID is sufficient as a handle
        return None

    def add_component(self, entity, component):
        ent_id = entity.id if isinstance(entity, Entity) else entity
        self._entities[ent_id][type(component)] = component

    def get_component(self, entity, component_type):
        ent_id = entity.id if isinstance(entity, Entity) else entity
        return self._entities.get(ent_id, {}).get(component_type)

    def has_component(self, entity, component_type):
        ent_id = entity.id if isinstance(entity, Entity) else entity
        return component_type in self._entities.get(ent_id, {})

    def view(self, *component_types):
        """Returns a list of entity IDs that have all the specified components."""
        results = []
        for ent_id, comps in self._entities.items():
            if all(ct in comps for ct in component_types):
                results.append(ent_id)
        return results

    def destroy_entity(self, entity):
        ent_id = entity.id if isinstance(entity, Entity) else entity
        if ent_id in self._entities:
            del self._entities[ent_id]
