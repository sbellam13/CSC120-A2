from computer import Computer
class ResaleShop:

    # inventory: a list where we'll store our inventory 
    inventory: list

    # Constructor
    def __init__(self):
        self.inventory = []

    # Takes in a Computer object and a new price, updates the price of the associated
    # computer if it is the inventory, prints error message otherwise. 
    def update_price(self, comp:Computer, newPrice:int):
        if comp in self.inventory:
            comp.setPrice(newPrice)
        else:
            print("Item not found. Cannot update price.")
    
    # Takes in a Computer object and adds it to the inventory. Returns the Computer object. 
    
    def buy(self, comp:Computer):
        self.inventory.append(comp)
        return self.inventory[len(self.inventory) - 1]

    #Takes in a Computer object, removes the associated computer if it is the inventory, 
    #prints error message otherwise
    def sell(self, comp:Computer):
        if comp in self.inventory:
            self.inventory.remove(comp)
        else:
            print("Item not found. Please select another item to sell.")

    # prints all the items in the inventory (if it isn't empty), prints error otherwise
    def print_inventory(self):
        if not self.inventory:  # If the inventory is empty
            print("No inventory to display.")
        else:
            print("There are " + str(len(self.inventory)) + " computer(s) in the store. ")
            for item in self.inventory:
                print(str(item))

def test():
    #First let's make a Shop object
    store:ResaleShop = ResaleShop()

    # Second, let's make a computer
    computer1:Computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,
    "macOS Big Sur", 2013, 1500)

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying\n" +  str(computer1))
    print("Adding to inventory...")
    store.buy(computer1)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS:str = "MacOS Monterey"
    print("Refurbishing\n" + str(computer1) + "\nupdating OS to" + str(new_OS))
    print("Updating inventory...")
    computer1.refurbish(new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling:\n" + str(computer1))
    store.sell(computer1)
    print("Done.\n")
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.print_inventory()
    print("Done.\n")

test()