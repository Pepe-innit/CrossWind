
class Inventory:
    def __init__(self):
        self.items = {}

#--- Methods ---

    def add_item(self, name, ammount=1):
        if name in self.items:
            self.items[name] += ammount
        else:
            self.items[name] = ammount

    def remove_item(self, name, ammount=1):
        if name in self.items:
            self.items[name] -= ammount
            if self.items[name] <= 0:
                del self.items[name]

    def get_items(self):
        return self.items