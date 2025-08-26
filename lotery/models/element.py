from PIL import Image

class Element:
    def __init__(self, file_path: str, parent_deck):
        self.deck = parent_deck
        file_name = file_path.split('/')[-1]
        self.ext = file_name.split('.')[-1]
        self.name = ' '.join(file_name.split(' ')[1:]).split('.')[0].capitalize()
        self.path = file_path
        self.image = Image.open(self.path)

    def __repr__(self):
        return f"<Element named '{self.path}' from deck '{self.deck.name}'>"