
import turtle

def draw_hypnotic_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    
    colors = ["red", "yellow", "blue", "green", "cyan", "magenta", "white"]
    
    for i in range(360):
        t.color(colors[i % len(colors)])
        t.forward(i * 2)
        t.right(59)
    
    screen.mainloop()

draw_hypnotic_spiral()
