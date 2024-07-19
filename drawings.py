import turtle

def draw_heart():
    window = turtle.Screen()
    window.bgcolor("black")  
    
    pen = turtle.Turtle()
    pen.color("#990000")  
    pen.pensize(3)
    pen.speed(3)

    pen.begin_fill()

    pen.penup()
    pen.goto(0, -250)
    pen.pendown()

    pen.left(140)
    pen.forward(287)
    pen.circle(-150, 200)

    pen.left(118)
    pen.circle(-150, 200)
    pen.forward(287)

    pen.end_fill()

    pen.penup()
    pen.goto(0, -20)
    pen.color("white")
    pen.write("I love you", align="center", font=("Arial", 36, "italic"))
    
    pen.hideturtle()

    window.mainloop()

draw_heart()
