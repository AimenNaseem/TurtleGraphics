
import turtle

def draw_hexagons():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    colors = ["red", "yellow", "blue", "green", "cyan", "magenta", "white"]
    
    for i in range(50):
        t.color(colors[i % len(colors)])
        for _ in range(6):
            t.forward(i * 6)
            t.right(60)
        t.right(8)
    
    screen.mainloop()

draw_hexagons()
