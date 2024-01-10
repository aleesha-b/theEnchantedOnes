class Item:
    """
        The Item class is used to store various values of an item so that the player can interact with it.
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
            prints "This item cannot be used" as the item is not dynamic
    """
    def __init__(self, name: str, description: str):
        self.name = name
        self.in_location = True
        self.dynamic = False
        self.description = description

    def use(self, location, bag):
        print("This item cannot be used")
