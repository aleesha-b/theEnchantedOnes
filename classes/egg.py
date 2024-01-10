from classes.item import Item


class Egg(Item):
    """
        The Egg class is used to store the values of a dynamic item, as well as actions to be performed when the item
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
        super().__init__("an egg", "An egg as big as your head! You peer closer and see swirling galaxies contained "
                                   "within.")
        self.dynamic = True

    def use(self, location, bag):
        if location.name == "Rainbow Road in Space":
            print("Thank you for rescuing my last remaining spawn. I think I might just let you live.")
            bag.items.remove(self)
            return True
        else:
            print("This item can't be used here.")
            return False
