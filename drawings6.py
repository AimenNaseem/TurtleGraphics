import turtle

def draw_color_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    
    for i in range(200):
        t.color((i % 200) / 200, (i % 100) / 100, (i % 50) / 50)
        t.forward(i)
        t.right(59)
    
    screen.mainloop()

draw_color_spiral()
