from blobber import *

name = input("What is the name of your blobber? ")
color = input("What color is your blobber? ")
radius = int(input("What is the radius of you blobber? "))
height = int(input("What is the height of you blobber? "))
ogCylVol = 3.14 * (radius ^ 2) * height
currentVol = ogCylVol
happi = currentVol / ogCylVol * 100
killRate = (ogCylVol / 1000) * 2
myBlobber = Blobber(name, color, radius, height, happi)
death = False
print(happi)

finish = False

while finish != True:
    myBlobber.happi = currentVol / ogCylVol * 100
    print()
    print("Main Menu")
    print("\t(1) Display Name")
    print("\t(2) Change Name")
    print("\t(3) Display Color")
    print("\t(4) Change Color")
    print("\t(5) Feed Blobber")
    print("\t(6) Blobber Speak")
    print("\t(7) Exit")
    print("My vital level is " + str(round(float(myBlobber.happi), 4)) + "%")

    response = int(input(" "))
    
    if happi <= 90 or happi >= 110:
        death = True

    if response == 1:
        myBlobber.displayName()
        currentVol = currentVol - killRate

    if response == 2:
        myBlobber.changeName()
        currentVol = currentVol - killRate

    if response == 3:
        myBlobber.displayColor()
        currentVol = currentVol - killRate

    if response == 4:
        myBlobber.changeColor()
        currentVol = currentVol - killRate

    if response == 5:
        myBlobber.feedMe(float(myBlobber.happi))
        currentVol = currentVol - killRate

    if response == 6:
        myBlobber.blobberSpeak(str(myBlobber.happi))
        currentVol = currentVol - killRate

    if response == 7:
        finish = True

    if death == True:
        print("That boi dead.")
        finish = True
    