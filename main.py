from blobber import *

name = input("What is the name of your blobber? ")
color = input("What color is your blobber? ")
radius = int(input("What is the radius of you blobber? "))
height = int(input("What is the height of you blobber? "))
ogCylVol = 3.14 * (radius ^ 2) * height
currentVol = ogCylVol

myBlobber = Blobber(name, color, radius, height)
print(ogCylVol)

finish = False

while finish != True:
    print()
    print("Main Menu")
    print("\t(1) Display Name")
    print("\t(2) Change Name")
    print("\t(3) Display Color")
    print("\t(4) Change Color")
    print("\t(5) Feed Blobber")
    print("\t(6) Blobber Speak")
    print("\t(7) Exit")

    response = input()
    if response == 1:
        Blobber.displayName()

    if response == 2:
        Blobber.changeName()

    if response == 3:
        Blobber.displayColor()

    if response == 4:
        Blobber.changeColor()

    if response == 7:
        finish = True

    