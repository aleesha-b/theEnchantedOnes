# User Documentation
## The Enchanted Lands
*Journey through the Enchanted Lands as you venture on a quest to uncover the whereabouts of the lost dragons.
Collect Runes that allow you to teleport around the world as you complete quests to get to your final destination.*
## Rules
Use commands to perform actions
- `look` - look around your current location
- `inspect <item>` - look at an item
- `use <item>` -use an item
- `pick up <item>` - pick up an item
- `talk to <person>` - talk to person
- `teleport <rune>` - teleport to the corresponding location on the map
- `view bag` - view the items in your bag

## Game Play
As you traverse the world you will pick up items that can be used to complete mini quests that give Runes (some runes
are simply laying on the ground waiting for you to pick up). Runes can then be used to teleport around the world. Each 
rune corresponds to a specific location on the map.

![Enchanted Lands Map](images/enchanted_lands.jpg)

## Software Needed
- Python
- PIL (Python Imaging Library)

# Developer Documentation
## Files
- theEnchantedOnes
  - classes 
      - amulet.py
      - apple.py
      - avatar.py
      - coin.py
      - dragon.py
      - egg.py
      - inventory.py
      - item.py
      - location.py
      - map.py
      - rocky_shores.py
      - rune.py
      - shovel.py
      - traveller.py
      - wizard.py
  - images
    - enchanted_lands.jpg
  - main.py
  - setup.py
  - startup_screen.py
  - ReadMe.md

## User requirements and specifications
The application must feature; 
- a minimum of 10 different locations
- a method of teleporting between locations
- runes corresponding to each location
- ten items, five of which are non-static
- the ability to pick up/inspect/use items
- three characters
- the ability to interact with characters
- a map which can be viewed
- a readable list of places visted/not visited
- an inventory listing all items currently in a player's possession
- missions that are completed by collecting items
- a final goal/mission


## Class diagram
```mermaid
classDiagram
    class Avatar{
        name: str
        location: Location
        bag: Inventory
        alive: bool
        look()
        pickup(item)
        pickup_rune()
        talk_to(person)
        use(item)
        teleport(rune, location_list)
        inspect(item)
        view_bag()
    }
    class Location{
        name: str
        description: str
        rune_key: Rune
        rune_found_here: Rune
        objects: list
        person: Person
        look()
    }
    class Item{
        name: str
        in_location: bool
        dynamic = False
        description: str
        use()
    }
    class Inventory{
        items: list
        runes: list
    }
    class Dragon{
        name: str
        description: str
        talk(avatar)
    }
    class Traveller{
        name: str
        task_finished: bool
        description: str
        talk(avatar)
        give_apple()
    }
    class Wizard{
        name: str
        description: str
        transform()
        talk(avatar)
    }
    class Amulet{
        used_on: Person
        dynamic = True
        use(location, bag)
    }
    class Apple{
        used_on: Person
        dynamic = True
        use(location, bag)
    }
    class Coin{
        dynamic = True
        use(location, bag)
    }
    class Egg{
        dynamic = True
        use(location, bag)
    }
    class Map{
        contains_rune = True
        dynamic = True
        use(location, bag)
    }
    class Shovel{
        dynamic = True
        use(location, bag)
    }
    class Rune{
        name: sttr
        description: str
        discoverable: bool
    }
    class RockyShore{
        shipwreck_rune: Rune
        shipwreck_objects: []
        look()
    }
    Location <|-- RockyShore
    Item <|-- Amulet
    Item <|-- Apple
    Item <|-- Coin
    Item <|-- Egg
    Item <|-- Map
    Item <|-- Shovel

    Avatar "1" <-- "1"Item
    Avatar "1" *-- "1" Location
    Avatar "1" <-- "1" Wizard
    Avatar "1" <-- "1" Dragon
    Avatar "1" <-- "1" Traveller
    Avatar "1" *-- "1" Inventory
    Avatar "1" <-- "1" Rune
    Wizard "1" <-- "1" Item
    Traveller "1" <-- "1" Item
    Inventory "1" o-- "0..*" Item
    Inventory "1" o-- "0..*" Rune
    Location "1" o-- "1" Rune
    Location "1" o-- "0..*" Item
```