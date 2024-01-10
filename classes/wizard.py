class Wizard:
    """
        The Wizard class is used to store the properties of an old man/wizard, as well as perform an action when the
        old man/wizard is talked to.
        ...

        Attributes
        ----------
        name : str
            the name of the old man/wizard
        description : str
            description of the old man/wizard

        Methods
        ----------
        talk(self, avatar)
            prints the dialogue for talking to the old man/wizard
        transform(self)
            changes the old man into a wizard, prints some dialogue
    """
    def __init__(self):
        self.name = "Old Man"
        self.description = "Looks a little worse for wear."

    def transform(self):
        self.name = "Wizard"
        print("Why thankyou for saving me from that horrible existence!\nThe Great Spell had left me in tatters, "
              "but now I have my memories back, thanks to you young traveller.")
        if input("Talk to the wizard? Y/N\n").upper() == "Y":
            print("So you've heard about the mysterious disappearance of the dragons eh?\nWell it just so happens that "
                  "I was one of the seven Great Ones responsible for sending them off to their new home.\n"
                  "You see a thousand years ago there was a Great War between our dragon friends and the almighty "
                  "Lost One, a wizard who had found the source of the dragon's strength and learnt how to use it for "
                  "evil.\nWith the power of the Great Ones combined with the strength of the dragons we managed "
                  "to defeat the Lost One.\nAfter the final battle was over the dragons and ourselves convened and "
                  "decided that in order for such a thing to never happen again our dragon friends would have to be "
                  "sent to another world, along with their life-source.\nThe seven Great Ones each gathered our runes "
                  "and cast a spell the likes of which had never been seen to transport the powerful giants to their "
                  "new home.\nUnfortunately the sheer magnitude of transporting such powerful creatures caused the "
                  "runes to scatter to the corners of the world and made me lose my memory in the process.\nI sure "
                  "wish I could find those runes to go visit our scaly friends...")

    def talk(self, avatar):
        if self.name == "Old Man":
            print("*Hic* 1000 years it's been... *Hic* Why... *Hic* Where did they all go... *Hic* Who am I?")
            print("The old man looks vaguely like the Wizard from the portrait. Perhaps I should give him this amulet")
        elif self.name == "Wizard" and len(avatar.bag.runes) == 7:
            print("You've done it! You've found all seven runes! How did you manage to achieve such a feat?\nNever "
                  "mind, now is not the time for explaining.\nQuick, use the runes on the portal! Do not worry young "
                  "traveller I will ensure that we are safe on our journey.\n(Use 'teleport all').")
        else:
            print("Come back when you have all seven runes.")
