class Dragon:
    """
        The Dragon class is used to store the properties of a dragon, as well as perform an action when the dragon is
        talked to.
        ...

        Attributes
        ----------
        name : str
            the name of the dragon
        description : str
            description of the dragon

        Methods
        ----------
        talk(self, avatar)
            prints the dialogue for talking to the dragon
    """
    def __init__(self):
        self.name = "Dragon"
        self.description = "Big dragon. Hungry dragon."

    def talk(self, avatar):
        print("The dragon eats you.")
        print("You are dead.")
        avatar.alive = False
