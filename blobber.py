class Blobber:
    def __init__(self, name, color, radius, height):
        self.name = name
        self.color = color
        self.radius = radius
        self.height = height

    def displayName(self):
        print(self.name)

    def changeName(self):
        self.name = input("What is the new name of your blobber? ")

    def displayColor(self):
        print(self.color)

    def changeColor(self):
        self.color = input("What is the new color of your blobber? ")


        
