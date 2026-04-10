import random
from ecs import Registry
from components import BookComponent, IdentityComponent, NameComponent
from generators import book_logic

class BookGenerator:
    def __init__(self, context):
        self.registry = context.registry
        self.context = context

    def generate_book(self):
        title = book_logic.generate_book_title()
        physical = book_logic.generate_book_physical_details()
        
        # Create Entity
        book_entity = self.registry.create_entity()
        comp = BookComponent(title, physical, "Content Unknown", "Standard Writing")
        self.registry.add_component(book_entity, comp)
        self.registry.add_component(book_entity, NameComponent(title))
        self.registry.add_component(book_entity, IdentityComponent("Book"))
        
        return book_entity
