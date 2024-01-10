from classes.inventory import Inventory
from classes.location import Location
from classes.places_visited import *


class Avatar:
    """
        The Avatar class is used to store various values of the avatar, as well as function for interacting with the
        world.
        ...

        Attributes
        ----------
        name : str
            the name of the avatar
        location : Location
            the current location of the avatar
        bag : Inventory
            the items currently held by the avatar
        alive : bool
            whether the avatar is alive

        Methods
        ----------
        look(self)
            prints information about the current location of the avatar
        pickup(self, item)
            adds an item to the avatar's bag
        pickup_rock(self)
            adds a rune to the avatar's bag if the rune found in the current location is discoverable
        talk_to(self, person)
            method for the avatar to interact with people in the current location
        teleport(self, rune, location_list)
            teleports to a location corresponding to the rune used
        inspect(self, item)
            print the description of the item
        view_bag(self)
            prints the contents of the avatar's bag
    """
    def __init__(self, name: str, location: Location):
        self.name = name
        self.location = location
        self.bag = Inventory()
        self.alive = True
        self.game_won = False

    def look(self):
        print(f"You are in: {self.location.name}. {self.location.description}.")
        self.location.look()
        if self.location.rune_found_here is not None and self.location.rune_found_here.discoverable:
            print("There is also a strange rock on the ground.")

    def pickup(self, item):
        if item.dynamic and item.in_location and item in self.location.objects:
            self.bag.items.append(item)
            print(f"{item.name} has been added to your bag. (Use 'view bag' to view your items).")
            item.in_location = False
        elif item in self.bag.items:
            print("You already picked that up.")
        elif item.dynamic:
            print("The item does not exist")
        else:
            print("You can't pick that up. Try using 'inspect [item]' instead.")

    def pickup_rock(self):
        if self.location.rune_found_here.discoverable:
            self.bag.runes.append(self.location.rune_found_here)
            self.location.rune_found_here.discoverable = False
            print(f"{self.location.rune_found_here.name} has been added to your bag. "
                  f"(Use 'view bag' to view your runes).")
        else:
            print("That item does not exist.")

    def talk_to(self, person):
        if self.location.person is not None and self.location.person == person:
            person.talk(self)
        else:
            print("There is no one to talk to.")

    def use(self, item):
        if self.bag.in_backpack(item) != -1:
            if item.name == "an egg" and item.use(self.location, self.bag):
                self.game_won = True
            else:
                item.use(self.location, self.bag)
        else:
            print("You do not have", item.name)

    def teleport(self, rune, location_list):
        if not self.location.name == "Shipwreck":
            if rune in self.bag.runes:
                for location in location_list:
                    if location.rune_key == rune:
                        self.location = location
                        PlacesVisited.places[self.location.name] = "[X]"
                        print("‧͙⁺˚*･༓☾　　☽༓･*˚⁺‧͙‧⁺˚*･༓☾　　☽༓･*˚⁺‧‧͙⁺˚*･༓☾　　☽༓･*˚⁺‧‧͙⁺˚*･༓☾　　☽༓･*˚⁺‧‧͙⁺˚*･༓☾　　☽༓･*˚⁺‧͙")
                        self.look()
            else:
                print("You do not have that rune.")
        else:
            print("You can't teleport from here. Go back to shore? (Y/N)")
            if input().upper() == "Y":
                self.location.reset_location()
                print(f"You are in {self.location.name}. {self.location.description}.")
                self.location.name = "Rocky Shore"

    def inspect(self, item):
        if item in self.location.objects or item in self.bag.items or item in self.bag.runes:
            print(item.description)
        else:
            print("That item does not exist here.")

    def view_bag(self):
        items = ""
        for item in self.bag.items:
            if items == "":
                items = item.name
            else:
                items = items + f", {item.name}"
        print(f"Items in bag: {items}")
        runes = ""
        for rune in self.bag.runes:
            runes = runes + f"\n {rune.description} {rune.name}"
        print(f"Runes in bag: {runes}")
        if items == "" and runes == "":
            print("You have nothing in your bag.")
        print("You can 'use' items in your bag to perform actions in certain locations. ")
