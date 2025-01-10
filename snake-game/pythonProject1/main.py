import turtle
from idlelib.colorizer import color_config
from turtle import Turtle, Screen
import time

from scoreboard import ScoreBoard
from snake import Snake
from food import Food

from turtledemo.penrose import start

#START SCREEN
screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.colormode(255)

#START FOOD
food = Food()

#START SCOREBOARD
score_board = ScoreBoard()

#START SNAKE
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




game_speed = .1

gameOn = True

while gameOn:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    #DETECT COLLISION WITH FOOD
    if food.distance(snake.head) < 20:
        food.refresh()
        score_board.add_point()
        snake.create_snake()

    #DETECT COLLISON WITH WALL:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameOn = False
        score_board.game_over()

    #DETECT COLLISION WITH TAIL:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameOn = False
            score_board.game_over()



screen.exitonclick()





