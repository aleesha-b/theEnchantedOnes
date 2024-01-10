from classes.item import Item


class Coin(Item):
    """
        The Coin class is used to store the values of a dynamic item, as well as actions to be performed when the item
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
        super().__init__("a coin", "These ancient relics are used as donations to the gods.")

        self.dynamic = True

    def use(self, location, bag):
        if location.name == "Old Town":
            print("You throw your coin into the village wishing well...")
            print("‧͙⁺˚*･༓☾　　☽༓･*˚⁺‧͙‧⁺˚*･༓☾　　☽༓･*˚⁺‧‧͙⁺˚*･༓☾　　☽༓･*˚⁺‧‧͙⁺˚*･༓☾　　☽༓･*˚⁺‧‧͙⁺˚*･༓☾　　☽༓･*˚⁺‧͙")
            print("What's this? The wishing well has returned to you a strange stone.")
            print(f"{location.rune_found_here.name} added to bag. (Use 'view bag' to view your runes).")
            bag.runes.append(location.rune_found_here)
            bag.items.remove(self)
        else:
            print("This item can't be used here.")
