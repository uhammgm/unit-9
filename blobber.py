

class Blobber:

    
    
    def __init__(self, name, color, radius, height, happi):
        self.name = name
        self.color = color
        self.radius = radius
        self.height = height
        self.happi = happi

    def displayName(self):
        print(self.name)

    def changeName(self):
        self.name = input("What is the new name of your blobber? ")

    def displayColor(self):
        print(self.color)

    def changeColor(self):
        self.color = input("What is the new color of your blobber? ")

    def blobberSpeak(self, happi):
        print("Hi my name is " + self.name + ", I am " + self.color + "." + "\nMy happiness level is " + str(round(float(happi), 4)) + "%.")

    def feedMe(self, happi):
        food = input("How much food do you want to feed me? ")
        happi = float(happi) + float(food)

    
        
