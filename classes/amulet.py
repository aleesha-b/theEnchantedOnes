from classes.item import Item
from classes.wizard import Wizard


class Amulet(Item):
    """
        The Amulet class is used to store the values of a dynamic item, as well as actions to be performed when the item
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
    def __init__(self, used_on: Wizard):
        super().__init__("an amulet", "An amulet belonging to a mysterious wizard.")
        self.used_on = used_on
        self.dynamic = True

    def use(self, location, bag):
        if location.name == "Old Town":
            self.used_on.transform()
            location.description = "There is a wishing well in the centre of the town square. An wizard leans " \
                                   "against a ramshackle market stall."
            bag.items.remove(self)
        else:
            print("This item can't be used here.")
