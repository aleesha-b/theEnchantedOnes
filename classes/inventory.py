class Inventory:
    """
        The Inventory class is used to store the contents of the player's bag.
        ...

        Attributes
        ----------
        items : list
            a list of items in the bag
        runes : list
            a list of runes in the bag
    """
    def __init__(self):
        self.items = []
        self.runes = []

    def in_backpack(self, item):
        item_names = []
        for item in self.items:
            item_names.append(item.name)
        item_names.sort()
        low = 0
        high = len(item_names) - 1
        while low <= high:

            mid = low + (high - low) // 2

            if item_names[mid] == item.name:
                return mid

            elif item_names[mid] < item.name:
                low = mid + 1

            else:
                high = mid - 1

        return -1

