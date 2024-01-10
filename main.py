from classes.avatar import *
from classes.amulet import *
from classes.apple import *
from classes.coin import *
from classes.location import *
from classes.map import *
from classes.shovel import *
from classes.traveller import *
from classes.wizard import *
from classes.dragon import *
from classes.egg import *
from classes.rocky_shore import *



dragon_text = """                                               _   __,----'~~~~~~~~~`-----.__
                                        .  .    `//====-              ____,-'~`
                        -.            \_|// .   /||\\  `~~~~`---.___./
                  ______-==.       _-~o  `\/    |||  \\           _,'`
            __,--'   ,=='||\=_    ;_,_,/ _-'|-   |`\   \\        ,'
         _-'      ,='    | \\`.    '',/~7  /-   /  ||   `\.     /
       .'       ,'       |  \\  \_  "  /  /-   /   ||      \   /
      / _____  /         |     \\.`-_/  /|- _/   ,||       \ /
     ,-'     `-|--'~~`--_ \     `==-/  `| \'--===-'       _/`
               '         `-|      /|    )-'\~'      _,--"'
                           '-~^\_/ |    |   `\_   ,^             /|
                                /  \     \__   \/~               `\__
                            _,-' _/'\ ,-'~____-'`-/                 ``===|
                           ((->/'    \|||' `.     `\.  ,                _||
             ./                       \_     `\      `~---|__i__i__\--~'_/
            <_n_                     __-^-_    `)  \-.______________,-~'
             `B'\)                  ///,-'~`__--^-  |-------~~~~^'
             /^\                           ///,--~`-\
            `   `                                       """

game_name = """ ______ __ __   ___        ___ ____     __ __ __  ____ ____  ______   ___ ___        _      ____ ____  ___   _____
|      |  |  | /  _]      /  _]    \   /  ]  |  |/    |    \|      | /  _]   \      | |    /    |    \|   \ / ___/
|      |  |  |/  [_      /  [_|  _  | /  /|  |  |  o  |  _  |      |/  [_|    \     | |   |  o  |  _  |    (   \_ 
|_|  |_|  _  |    _]    |    _]  |  |/  / |  _  |     |  |  |_|  |_|    _]  D  |    | |___|     |  |  |  D  \__  |
  |  | |  |  |   [_     |   [_|  |  /   \_|  |  |  _  |  |  | |  | |   [_|     |    |     |  _  |  |  |     /  \ |
  |  | |  |  |     |    |     |  |  \     |  |  |  |  |  |  | |  | |     |     |    |     |  |  |  |  |     \    |
  |__| |__|__|_____|    |_____|__|__|\____|__|__|__|__|__|__| |__| |_____|_____|    |_____|__|__|__|__|_____|\___|"""


def game_play():
    #setup
    print(dragon_text)
    print(game_name + "\n")

    # Runes
    hagalaz = Rune("Hagalaz", "ᚺ", False)
    kenaz = Rune("Kenaz", "ᚲ", False)
    thurisaz = Rune("Thurisaz", "ᚦ", False)
    uruz = Rune("Uruz", "ᚢ", True)
    ansuz = Rune("Ansuz", "ᚫ", False)
    raidho = Rune("Raidho", "ᚱ", True)
    fehu = Rune("Fehu", "ᚠ", True)

    runes = {"hagalaz": hagalaz,
             "kenaz": kenaz,
             "thurisaz": thurisaz,
             "uruz": uruz,
             "ansuz": ansuz,
             "raidho": raidho,
             "fehu": fehu}

    # People
    wizard = Wizard()
    traveller = Traveller()
    dragon = Dragon()

    people = {"wizard": wizard,
              "man": wizard,
              "kettricken": traveller,
              "dragon": dragon}

    # Items
    shovel = Shovel()
    amulet = Amulet(wizard)
    apple = Apple(traveller)
    coin = Coin()
    egg = Egg()
    world_map = Map()
    wishing_well = Item("a wishing well", "Use a coin to make a wish..")
    portrait = Item("a portrait", "A portrait of an old man, he looks powerful and mysterious.")
    carvings = Item("some carvings", "They depict a great battle between some weird old guys in hats.")
    book = Item("an old book", "As you look through the book you find reference to some strange markings on stones... "
                               "It appears that that powerful beings used to use these stones to teleport to places around "
                               "the world.\n(Use 'teleport [rune name]' to target a different location)")

    items = {"shovel": shovel,
             "amulet": amulet,
             "apple": apple,
             "coin": coin,
             "egg": egg,
             "map": world_map,
             "portrait": portrait,
             "carvings": carvings,
             "book": book,
             "well": wishing_well}

    # Locations
    backyard = Location("your backyard", "There is a strange portal.", [apple], None)
    desert = Location("Desert Wastes", "These are barren lands, the sun beats down on your exposed flesh.",
                      [shovel], None, ansuz, kenaz)
    ice_cave = Location("Ice Cave", "It is very cold.", [carvings], None, uruz, hagalaz)
    dragon_lair = Location("Dragon's Lair", "There are riches stretching as far as the eye can see.\nHowever one item "
                                            "stands out as being the only thing not glittering with gold.", [egg], None,
                           raidho, thurisaz)
    forrest = Location("Shadow Grove", "Green trees tower over you, the sun filtering through the canopy. It is quite "
                                       "beautiful here.", [], traveller, thurisaz, uruz)
    wizard_tower = Location("Abandoned Wizard's Tower",
                            "The tower shakes in the wind, you'd better look around quickly,"
                            " it doesn't seem very safe here.",
                            [world_map, book, portrait, amulet], None, hagalaz, ansuz)
    rocky_shore = RockyShore([coin], None, fehu, raidho)
    village = Location("Old Town", "There is a wishing well in the centre of the town square. An old man leans against "
                                   "a ramshackle market stall.", [wishing_well], wizard, kenaz, fehu)
    space = Location("Rainbow Road in Space", "Huh?", [], dragon)

    location_list = [backyard, desert, ice_cave, dragon_lair, forrest, wizard_tower, rocky_shore, village]

    me = Avatar(input("Enter a name for your character: "), backyard)

    # Tutorial for the game
    print(
        "You wake up to a strange light glowing outside your window.\nYou cautiously get out of bed and open the back "
        "door of your cottage only to see what looks to be a portal.\nUse the 'look' command to look around you.")
    while True:
        tut_input = input().strip().lower()
        if tut_input == "":
            print("Enter a command")
            continue
        tut_target = tut_input.split()[-1]
        if "look" in tut_input:
            me.look()
            print("To pick up an object, type 'pick up [object name]'")
            print("To inspect an object, type 'inspect [object name]'")
            print("Remember to interact with all objects on your adventure, you never know what you might need.")
        elif "pick up" in tut_input:
            if tut_target in items:
                me.pickup(items[tut_target])
                print("You have collected everything here, why not see where the portal takes you.\nUse the 'teleport' "
                      "command to enter the portal.")
            else:
                print("That object does not exist, ensure you typed everything correctly")
        elif "inspect" in tut_input:
            if tut_target in items or tut_target in people:
                me.inspect(items[tut_target])
            else:
                print("That object does not exist, ensure you typed everything correctly")
        elif "view bag" in tut_input:
            me.view_bag()
        elif "teleport" in tut_input:
            if tut_target in runes:
                me.teleport(runes[tut_target], location_list)
            elif me.location == backyard:
                me.location = wizard_tower
                PlacesVisited.places[wizard_tower.name] = "[X]"
                me.look()
                break
        else:
            print("That command does not exist, ensure you typed everything correctly")
    # Game play through
    while me.alive and not me.game_won:
        directive = input().strip().lower()
        target = directive.split()[-1]

        if "pick up" in directive:
            if target in items:
                me.pickup(items[target])
            elif target == "rock":
                me.pickup_rock()
            else:
                print("That object does not exist, ensure you typed everything correctly")

        elif "look" in directive:
            me.look()

        elif "talk to" in directive:
            if target in people:
                me.talk_to(people[target])
            else:
                print("That object does not exist, ensure you typed everything correctly")

        elif "use" in directive or "give" in directive:
            if target in items:
                me.use(items[target])
            elif target in runes:
                print("That is a rune, it must be used with 'teleport [rune]'")
            else:
                print("That object does not exist, ensure you typed everything correctly")

        elif "teleport" in directive:
            if target in runes:
                me.teleport(runes[target], location_list)
            elif me.location.name == "a shipwreck":
                me.teleport(None, location_list)
            elif target == "all" and len(me.bag.runes) == 7:
                me.location = space
                me.look()
            else:
                print("That object does not exist, ensure you typed everything correctly")

        elif "inspect" in directive:
            if target in items:
                me.inspect(items[target])
            else:
                print("That object does not exist, ensure you typed everything correctly")

        elif "view bag" in directive:
            me.view_bag()

        else:
            print("That command does not exist, ensure you typed everything correctly")


game_play()
print("Game Over")
if input("Would you like to play again? Y/N\n").lower().strip() == "y":
    game_play()