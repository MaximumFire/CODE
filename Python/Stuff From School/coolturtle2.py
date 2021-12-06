import turtle 
Mohanad = turtle.Turtle()

Mohanad.speed(1000000000000)

Mohanad.color("Black")

for i in range(1000):
    Mohanad.forward(180)
    Mohanad.left(70)
    Mohanad.forward(60)
    Mohanad.right(39)
    
    Mohanad.penup()
    Mohanad.setposition(0, 0)
    Mohanad.pendown()
    
    Mohanad.right(2)
    
turtle.done()
