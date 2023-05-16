import turtle
from features import *

turtle.speed(100)
features.drawHead()
features.drawEyes()
features.drawSmile()
turtle.done()

choice = 0
finish = False
while finish != True:    
    choice = int(input("Change me!\n\t1.Make me sad\n\t4.Exit "))

    
    if choice == 1:
        features.drawHead()
        features.drawEyes()
        features.drawSad()
        turtle.done()

    if choice == 4:
        finish = True