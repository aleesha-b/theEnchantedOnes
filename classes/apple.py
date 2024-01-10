from classes.item import Item
from classes.traveller import Traveller


class Apple(Item):
    """
        The Apple class is used to store the values of a dynamic item, as well as actions to be performed when the item
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
        used_on : Person
            the person that the item can be used on/given to

        Methods
        ----------
        use(self, location, bag)
            performs an action if the location is correct
    """
    def __init__(self, used_on: Traveller):
        super().__init__("an apple", "An apple, slightly mouldy, possibly edible.")
        self.used_on = used_on
        self.dynamic = True

    def use(self, location, bag):
        if location.name == "Shadow Grove":
            self.used_on.give_apple()
            print(f"{location.rune_found_here.name} added to bag. (Use 'view bag' to view your runes).")
            bag.runes.append(location.rune_found_here)
            bag.items.remove(self)
        else:
            print("This item can't be used here.")
