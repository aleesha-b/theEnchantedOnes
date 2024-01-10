from classes.item import Item


class Shovel(Item):
    """
        The Shovel class is used to store the values of a dynamic item, as well as actions to be performed when the item
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

        Methods
        ----------
        use(self, location, bag)
            performs an action if the location is correct
    """
    def __init__(self):
        super().__init__("a shovel", "Used for digging.")
        self.dynamic = True

    def use(self, location, bag):
        if location.name == "Desert Wastes":
            print("You dig in the sand...")
            print("You keep digging...")
            print("You enter a mad haze where digging is all that exists.")
            print(".・゜゜・．.・゜゜・．.・゜゜・．.・゜゜・．.・゜゜・．.・゜゜・．.・゜゜・．.・゜゜・．")
            print("You wake up from a daze, sunburnt and thirsty with a strange stone in your hand. Your shovel has "
                  "mysteriously disappeared.")
            print(f"{location.rune_found_here.name} added to bag. (Use 'view bag' to view your runes).")
            bag.runes.append(location.rune_found_here)
            bag.items.remove(self)
        else:
            print("This item can't be used here.")
