import turtle

def draw_radiating_circles():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    colors = ["red", "yellow", "blue", "green", "cyan", "magenta", "white"]
    
    for i in range(36):
        t.color(colors[i % len(colors)])
        t.circle(100)
        t.right(10)
    
    screen.mainloop()

draw_radiating_circles()
