from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("bg.gif")
screen.title("S N A K E")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detect for food collision 15px buffer
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
       # game_is_on = False
        #scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
           # game_is_on = False
           # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
