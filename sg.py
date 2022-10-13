import turtle
import random
import time
s = 0
d = 0.1
# for creating screen
win = turtle.Screen()
win.title("Snake Game")
win.tracer(1)
win.setup(height=700, width=700)
turtle.bgcolor("black")

# for creating border of game/game area
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("chartreuse")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# for making the snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

#for making the food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(30, 30)

of = []

#for displaying score
score = turtle.Turtle()
score.color("cyan")
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0,300)
score.write("Score : ",align="center",font=("Courier",24,"bold"))

def sgu():
    if snake.direction != "down":
        snake.direction = "up"

def sgd():
    if snake.direction != "up":
        snake.direction = "down"

def sgl():
    if snake.direction != "right":
        snake.direction = "left"

def sgr():
    if snake.direction != "left":
        snake.direction = "right"
def sm():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)
win.listen()
win.onkeypress(sgu,"Up")
win.onkeypress(sgd,"Down")
win.onkeypress(sgr,"Right")
win.onkeypress(sgl,"Left")

while True:
    win.update()
    if snake.distance(food) < 20:
        x= random.randint(-290,270)
        y = random.randint(-240,240)
        food.goto(x,y)
        score.clear()
        s+=1
        score.write("Score : {}".format(s),align="center",font=("Courier",24,"bold"))
        d-=0.001

        newfood = turtle.Turtle()
        newfood.speed(0)
        newfood.shape("square")
        newfood.color("red")
        newfood.penup()
        of.append(newfood)
    for index in range(len(of)-1,0,-1):
        a = of[index-1].xcor()
        b = of[index-1].ycor()
        of[index].goto(a,b)
    if len(of)>0:
        a = snake.xcor()
        b = snake.ycor()
        of[0].goto(a,b)
    sm()


    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        win.clear()
        win.bgcolor('black')
        score.goto(0,0)
        score.write("Game over \n Your Score is : {}".format(s), align="center", font=("Courier", 32, "bold"))
    for f in of:
        if f.distance(snake) < 20:
            time.sleep(1)
            win.clear()
            win.bgcolor('black')
            score.goto(0, 0)
            score.write("Game over \n Your Score is : {}".format(s), align="center", font=("Courier", 32, "bold"))
    time.sleep(d)
win.mainloop()
