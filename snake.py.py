#import modules
import turtle 
import random
import time
delay = 0.1
score = 0
high_score = 0
#create windows
wn = turtle.Screen()
wn.title("SNAKE GAME BY HAZEM YAKOUT")
wn.bgcolor("#000087")#blue color
wn.setup(width=600, height= 600)
wn.cv._rootwindow.resizable(False, False)
wn.tracer(0)
#head of snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"
#create food
food = turtle.Turtle()
colors = random.choice(["red", "green", "black"])
shapes = random.choice(["square", "circle", "triangle"])
food.shape(shapes)
food.color(colors)
food.speed(0)
food.penup()
food.goto(0, 100)
#create pen
pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.speed(0)
pen.goto(0, 250)
pen.hideturtle()
pen.write("Score: 0  High Score: 0 ", align= "center", font=("Arial", 24, "bold"))
#functions of directions
def goup():
    if head.direction != "down":
        head.direction = "up"
def godown():
    if head.direction != "up":
        head.direction = "down"
def goleft():
    if head.direction != "right":
        head.direction = "left"
def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+10)
    if head.direction == "down":
           y = head.ycor()
           head.sety(y-10)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+10)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-10)
#key binding
wn.listen()
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")
segments = []

#main gameplay
while True:
    wn.update()
    if (head.xcor()>295 or head.xcor()< -295 or head.ycor()>295 or head.ycor()<-295):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        colors = random.choice(["red", "green", "black"])
        shapes = random.choice(["square", "circle", "triangle"])
        food.shape(shapes)
        food.color(colors)
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score} ", align= "center", font=("Arial", 24, "bold"))
    if head.distance(food) < 10:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        #adding segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.speed(0)
        new_segment.penup()
        segments.append(new_segment)   
        delay -= 0.001 # increase difficulty of game
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score} ", align= "center", font=("Arial", 24, "bold"))  
    for index in range(len(segments) - 1, 0, -1):
       x = segments[index -1].xcor()
       y = segments[index -1].ycor()
       segments[index].goto(x, y)
    if len(segments)> 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    #checking for collision with body
    for segment in segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(["red", "green", "black"])
            shapes = random.choice(["square", "circle", "triangle"])
            food.shape(shapes)
            food.color(colors)
            for segment in segments:
               segment.hideturtle()
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score} ", align= "center", font=("Arial", 24, "bold"))
    time.sleep(delay)