from classes.location import Location
from classes.places_visited import *


class RockyShore(Location):
    """
        The RockyShore class is used as an interactive multi-location version of the location class.
        ...

        Attributes
        ----------
        name : str
            the name of the location
        description : str
            description of the location
        objects : list
            a list of objects in the "rocky shore" location
        people: Person
            the person present in the location
        rune_found_here : Rune
            the rune found at the "rocky shore" location
        rune_key : Rune
            the rune used to travel to this location
        shipwreck_rune: Rune
            the rune found at the "shipwreck" location
        shipwreck_objects : list
            a list of objects in the "rocky shore" location

        Methods
        ----------
        look(self)
            prints the items found in this location
        reset_location(self)
            changes the location name and description back to its original state
        """

    def __init__(self, objects, people, rune_found_here, rune_key):
        super().__init__("Rocky Shore", "Gulls squawk as they fly overhead, searching for their next meal.",
                         [], people, None, rune_key)
        self.shipwreck_rune = rune_found_here
        self.shipwreck_objects = objects

    def look(self):
        if self.name == "Rocky Shore":
            print("You look around and see a shipwreck grounded on the rocks. Perhaps there is treasure inside. "
                  "Go look? (Y/N)")
            if input().lower().strip() == "y":
                self.name = "Shipwreck"
                PlacesVisited.places[self.name] = "[X]"
                self.description = "The inside of the shipwreck is quite small. You feel claustrophobic and a little " \
                                   "damp."
                print(f"You are in {self.name}. {self.description}")
                self.rune_found_here = self.shipwreck_rune
                self.objects = self.shipwreck_objects
            pass
        items = ""
        for item in self.objects:
            if item.in_location and items == "":
                items = item.name
            elif item.in_location:
                items = items + f", {item.name}"
        if not items == "":
            print(f"You look around and see {items}")

    def reset_location(self):
        self.name = "Rocky Shore"
        self.description = "Gulls squawk as they fly overhead, searching for their next meal."
