import turtle
import math

def draw_lissajous_curve():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    
    a = 5
    b = 4
    delta = math.pi / 2
    colors = ["red", "yellow", "blue", "green", "cyan", "magenta", "white"]

    for i in range(1000):
        t.color(colors[i % len(colors)])
        x = 200 * math.sin(a * math.radians(i) + delta)
        y = 200 * math.sin(b * math.radians(i))
        t.goto(x, y)
        
    screen.mainloop()

draw_lissajous_curve()

