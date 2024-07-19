import turtle

def draw_concentric_circles():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    colors = ["red", "yellow", "blue", "green", "cyan", "magenta", "white"]
    
    for i in range(20):
        t.color(colors[i % len(colors)])
        t.circle(i * 10)
        t.up()
        t.goto(0, -(i * 10))
        t.down()
    
    screen.mainloop()

draw_concentric_circles()
