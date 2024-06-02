import time
from snakeclass import Snake
from turtle import Screen,Turtle
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

timmy = Snake()
food = Food()
game_score = Scoreboard()

screen.listen()
screen.onkey(fun=timmy.up, key="Up")
screen.onkey(fun=timmy.down, key="Down")
screen.onkey(fun=timmy.right, key="Right")
screen.onkey(fun=timmy.left, key="Left")

game_active = True
while game_active:
    screen.update()
    time.sleep(0.1)
    timmy.move()

    #detect collision with food
    if timmy.head.distance(food) < 15:
        food.relocate()
        timmy.extend()
        game_score.increment_score()

    if timmy.head.xcor() > 280 or timmy.head.xcor() < -280 or timmy.head.ycor() > 280 or timmy.head.ycor() < -280:
        game_score.reset_game()
        timmy.reset()

    for tortoise in timmy.turtle_list[:1:-1]:
        if timmy.head.distance(tortoise) < 10:
            game_score.reset_game()
            timmy.reset()


screen.exitonclick()
