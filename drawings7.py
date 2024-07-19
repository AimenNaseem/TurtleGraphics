import turtle

def draw_geometric_flower():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    colors = ["red", "yellow", "blue", "green", "cyan", "magenta", "white"]
    
    for i in range(36):
        t.color(colors[i % len(colors)])
        for _ in range(6):
            t.forward(100)
            t.right(60)
        t.right(10)
    
    screen.mainloop()

draw_geometric_flower()
