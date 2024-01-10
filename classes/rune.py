class Rune:
    """
        The Rune class is used to store various values of a rune so that the player can interact with it.
        ...

        Attributes
        ----------
        name : str
            the name of the rune
        description : str
            description of the rune
        discoverable : bool
            whether the rune is viewable on the ground of the location
    """
    def __init__(self, name: str, description: str, discoverable: bool):
        self.name = name
        self.description = description
        self.discoverable = discoverable
