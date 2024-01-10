from classes.rune import Rune


class Location:
    """
        The Location class is used to store various values of a location so that the player can interact with
        them.
        ...

        Attributes
        ----------
        name : str
            the name of the location
        description : str
            description of the location
        objects : list
            a list of objects in the location
        person: Person
            the person present in the location
        rune_found_here : Rune
            the rune found at the location
        rune_key : Rune
            the rune used to travel to this location

        Methods
        ----------
        look(self)
            prints the items found in this location
            """
    def __init__(self, name: str, description: str, objects: list, person: object, rune_found_here: Rune = None,
                 rune_key: Rune = None):
        self.name = name
        self.description = description
        self.rune_key = rune_key
        self.rune_found_here = rune_found_here
        self.objects = objects
        self.person = person

    def look(self):
        if self.person is not None:
            print(f"{self.person.name} is standing near by, try talking to them. "
                  f"(Use 'talk to {self.person.name}')")
        items = ""
        for item in self.objects:
            if item.in_location and items == "":
                items = item.name
            elif item.in_location:
                items = items + f", {item.name}"
        if not items == "":
            print(f"You look around and see: {items}")