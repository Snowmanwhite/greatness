import turtle;

# Create turtle object
t = turtle.Turtle()

# Define function to draw circle
def draw_circle():
    for i in range(4):
        t.forward(80)
        t.right(90)

# Define function to animate circle
def animate_circle():
    for i in range(36):
        t.right(10)
        draw_circle()

# Call animate_square function to start animation
animate_circle()

# Exit on click
turtle.exitonclick()
