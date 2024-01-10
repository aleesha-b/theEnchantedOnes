class Traveller:
    """
        The Traveller class is used to store the properties of a traveller, as well as perform an action when the
        traveller is talked to.
        ...

        Attributes
        ----------
        name : str
            the name of the traveller
        description : str
            description of the traveller
        task_finished : bool
            whether the avatar has completed the task of the traveller

        Methods
        ----------
        talk(self, avatar)
            prints the dialogue for talking to the traveller
        give_apple(self)
            completes the task
    """
    def __init__(self):
        self.name = "Kettricken"
        self.task_finished = False
        self.description = "A traveller, she looks hungry. Try talking to her."

    def talk(self, avatar):
        if self.task_finished:
            print("The traveller looks at you and smiles")
        else:
            print("Hi friend, it sure is a fine day for a stroll through the forrest.\nSay you don't happen to have "
                  "any food on you, do you?")

    def give_apple(self):
        print("Why thankyou, friend! Here take this strange rock I found as thanks for your kind gesture.")
        self.task_finished = True
