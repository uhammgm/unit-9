import turtle
from features import *

turtle.speed(100)
drawer = features()
drawer.drawHead()
drawer.drawEyes()
drawer.drawSmile()
turtle.hideturtle()

mouthStat = 1
headStat = 1
eyesStat = 1
FroSmi = "1.Make me sad"
EyeBlue = "2.Make my eyes blue"
HapMad = "3.Make me mad"

choice = 0
finish = False
while finish != True:    
    print("Change me!" + "\n\t" + FroSmi + "\n\t" + EyeBlue + "\n\t" + HapMad + "\n\t4.Exit ")
    choice = int(input("Choice: "))
    
    if choice == 1:
        if HapMad == "3.Make me happy":
            drawer.drawHead()
        elif HapMad == "3.Make me mad":
            drawer.drawHeadMad()
        if eyesStat == 1:
            drawer.drawEyes()
        elif eyesStat == 2:
            drawer.drawEyesBlue()
        if FroSmi == "1.Make me sad":
            drawer.drawSad()
            FroSmi = "1.Make me smile"
            mouthStat = 1
        elif FroSmi == "1.Make me smile":
            drawer.drawSmile()
            FroSmi = "1.Make me sad"
            mouthStat = 2
        
        

    if choice == 2:
        eyesStat = 2
        if headStat == 1:
            drawer.drawHead()
        elif headStat == 2:
            drawer.drawHeadMad()
        if mouthStat == 1:
            drawer.drawSmile()
        elif mouthStat == 2:
            drawer.drawSad()
        if EyeBlue == "2.Make my eyes black":
            drawer.drawEyes()
            EyeBlue = "2.Make my eyes blue"
        elif EyeBlue == "2.Make my eyes blue":
            drawer.drawEyesBlue()
            EyeBlue = "2.Make my eyes black"
        
        

    if choice == 3:
        drawer.drawHeadMad()
        if eyesStat == 1:
            drawer.drawEyes()
        elif eyesStat == 2:
            drawer.drawEyesBlue()
        if mouthStat == 1:
            drawer.drawSmile()
        elif mouthStat == 2:
            drawer.drawSad()
        if HapMad == "3.Make me mad":
            drawer.drawHeadMad()
            HapMad = "3.Make me happy"
        elif HapMad == "3.Make me mad":
            drawer.drawHead()
            HapMad == "3.Make me mad"


    if choice == 4:
        finish = True