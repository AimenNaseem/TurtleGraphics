
import turtle
import math

def draw_spirograph():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)

    colors = ["red", "yellow", "blue", "green", "cyan", "magenta", "white"]

    for i in range(360):
        t.color(colors[i % len(colors)])
        t.forward(math.sin(math.radians(i)) * 100)
        t.right(45)
        t.forward(100)
        t.right(135)
        t.forward(math.sin(math.radians(i)) * 100)
        t.right(45)
        t.forward(100)
        t.right(135)
        t.right(10)
        
    screen.mainloop()

draw_spirograph()
