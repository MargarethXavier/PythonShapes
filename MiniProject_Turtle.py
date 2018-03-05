import turtle

def draw_flowers(shape,color,speed):
    flower.shape(shape)
    flower.color(color)
    flower.speed(speed)    
    flower.forward(80)
    flower.right(60)
    flower.forward(80)
    flower.right(120)
    flower.forward(80)
    flower.right(60)
    flower.forward(80)
    flower.right(110)
        
window = turtle.Screen()
window.bgcolor("white")

flower = turtle.Turtle()
flower.left(120)
for i in range(36):
    draw_flowers("circle","purple",80)
flower.setpos(0,-300)
    
window.exitonclick()
