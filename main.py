from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

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


# detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

# detect collision with head
    if snake.head.xcor() > 340 or snake.head.xcor() < -350 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        score_board.game_over()
        game_is_on = False

# detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()