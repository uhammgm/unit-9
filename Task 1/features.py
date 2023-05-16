import turtle 
class features:
    
    def drawHead():
        turtle.penup()
        turtle.goto(200 , 0)
        turtle.setheading(90)
        turtle.pendown()
        turtle.color("yellow")
        turtle.begin_fill()
        turtle.circle(200)
        turtle.end_fill()
        turtle.color("black")
        turtle.width(2)
        turtle.circle(200)
    
    def drawEyes():
        turtle.penup()
        turtle.goto(100 , 75)
        turtle.color("black")
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-50 , 75)
        turtle.color("black")
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()

    def drawSmile():
        turtle.penup()
        turtle.goto(-145 , -65)
        turtle.pendown()
        turtle.setheading(310)
        turtle.width(5)
        turtle.circle(200,100)

    def drawSad():
        turtle.penup()
        turtle.goto(150 , -115)
        turtle.pendown()
        turtle.setheading(130)
        turtle.width(5)
        turtle.circle(200,100)
        
 
