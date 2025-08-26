import os
from .element import Element
import random

class Deck:
    """it represents a deck of cards. Must specify what cards to read (in assets/images folder).
    
    The objective of this class is to load images once so that process doesn't repeat multiple times on the program."""

    def __init__(self, deck_path: str):
        assert os.path.isdir(deck_path), "Path doesn't exists: "+ deck_path
        assert len(os.listdir(deck_path)) > 0, "Path doesn't contain files: " + deck_path
        self.path = deck_path
        self.name = deck_path.split('/')[-1].capitalize()

        images_path_list = [path for path in os.listdir(self.path) if path.split('.')[-1] in ('jpg', 'jpeg', 'png')]
        valid_syntax_images_path_list = [path for path in images_path_list if path.split(' ')[0].isdecimal()]
        assert len(images_path_list) > 0, "Path doesn't contain img files (expected png or jpg files): " + deck_path
        assert len(valid_syntax_images_path_list) > 0, "Path doesn't contain img files with correct syntax (expected files with names as '## card name.png'): " + deck_path
        
        self.card_paths = valid_syntax_images_path_list
        metadata = {}
        for path in self.card_paths:
            metadata[int(path.split(' ')[0])] = Element(self.path+'/'+path, self)
        
        self.elements = metadata
        self.ids = list(self.elements.keys())
        self.sort()
        self.id_selector = 0
    
    def __getitem__(self, id: int):
        return self.elements[id]
    
    def __len__(self):
        return len(self.card_paths)
    
    def __repr__(self):
        return f"<Deck '{self.name}' with {len(self)} cards. Path: '{self.path}'>"

    def sort(self):
        self.ids.sort()
        self.id_selector = 0
        return
    
    def get_next_ids(self, amount = 1):
        assert self.id_selector+amount <= len(self), "Deck ran out of elements. Try to use shuffle or sort to restart selection"
        if amount == 1: result = self.ids[self.id_selector]
        else: result = self.ids[self.id_selector:self.id_selector+amount]
        self.id_selector += amount
        return result
    
    def shuffle(self):
        random.shuffle(self.ids)
        self.id_selector = 0
        return