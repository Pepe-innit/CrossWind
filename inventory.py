
class Inventory:
    def __init__(self):
        self.items = []
        self.max_items = 10
        self.max_weight = 25.0

#--- Methods ---
    def get_total_weight(self):
        return sum(fish.weight for fish in self.items)


    def add_item(self, item):
        if len(self.items) >= self.max_items:
            print("Inventory full! Cannot carry more fish.")
            return False
        
        if self.get_total_weight() + item.weight > self.max_weight:
            print("Too heavy! Cannot carry this fish.")
            return False
        
        self.items.append(item)
        return True

        
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_items(self):
        return self.items