class Computer:

    # Variables
    description: str
    processorType: str
    hardDriveCapacity: int
    memory: int
    operatingSystem: str
    yearMade: int
    price: int

    # Constructor
    def __init__(self, des:str, pro:set, hdc:int, mem:int, os:str, year:int, pri:int):
        self.description = des
        self.processorType = pro
        self.hardDriveCapacity = hdc
        self.memory = mem
        self.operatingSystem = os
        self.yearMade = year
        self.price = pri

    # Returns price of this computer object
    def getPrice(self):
        return self.price
    
    # Sets price of this computer object
    def setPrice(self, new:int):
        self.price = new
    
    # Returns the operating system of this computer object
    def getOS(self):
        return self.operatingSystem
    
    # Updates the operating system of the computer
    def setOS(self, new:str):
        self.operatingSystem = new
    
    
    # string method - return all information about this computer object
    def __str__(self):
        toString:str = ""
        toString = "Description: " + str(self.description)
        toString = toString + "\nProcessor Type: " + str(self.processorType)
        toString = toString + "\nHard Drive Capacity: " + str(self.hardDriveCapacity)
        toString = toString + "\nMemory: " + str(self.memory)
        toString = toString + "\nOperating System: " + str(self.operatingSystem)
        toString = toString + "\nYear Made: " + str(self.yearMade)
        toString = toString + "\nPrice: " + str(self.price)
        return toString

    # updates computer to operating system imputed by the user, discounts the computer if > 4 years old
    def refurbish(self, newOS:str):
        if self.yearMade < 2000:    # too old to sell, donation only
            self.price = 0
        elif self.yearMade < 2012:  # heavily-discounted price on machines 10+ years old
            self.price = 250
        elif self.yearMade < 2018:  # discounted price on machines 4-to-10 year old machines
            self.price = 550
        else:                   # recent computers
            self.price = 1000

        if newOS is not None:   # update operating system
            self.operatingSystem = newOS
    




    