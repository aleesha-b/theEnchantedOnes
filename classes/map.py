from classes.item import Item
from classes.places_visited import *
from PIL import Image


class Map(Item):
    """
        The Map class is used to store the values of a dynamic item, as well as actions to be performed when the item
          is used so that the player can interact with it.
        ...

        Attributes
        ----------
        name : str
            the name of the item
        description : str
            description of the item
        in_location : bool
            whether the item is  in its original location
        dynamic : bool
            whether an item can be used/picked up
        contains_rune : bool
            whether the map has a rune in it

        Methods
        ----------
        use(self, location, bag)
            opens an image file containing a representation of the map
    """
    def __init__(self):
        super().__init__("a map", "A map of the strange lands you find yourself in.")
        self.dynamic = True
        self.contains_rune = True

    def print_places(self):
        text = "Places visited:\n"
        for item in PlacesVisited.places:
            text = text + f"{PlacesVisited.places[item]} {item}\n"
        print(text)

    def use(self, location, bag):
        self.print_places()
        if self.contains_rune:
            print("As you unroll the map a strange stone with some intricate marking falls out.")
            print(f"{location.rune_found_here.name} added to bag.")
            bag.runes.append(location.rune_found_here)
            self.contains_rune = False
        img = Image.open('images/enchanted_lands.jpg')
        img.show("Map.png")

