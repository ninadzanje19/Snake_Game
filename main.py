import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen_obj = Screen()
screen_obj.setup(width=600, height=600)
screen_obj.bgcolor("black")
screen_obj.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen_obj.listen()
screen_obj.onkey(snake.up, "Up")
screen_obj.onkey(snake.down, "Down")
screen_obj.onkey(snake.left, "Left")
screen_obj.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen_obj.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen_obj.exitonclick()
