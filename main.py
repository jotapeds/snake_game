## Snake game
from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)


# setting up segments

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# setting up keybindings

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')





game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    


    # detecting collisions
    # turtle distance method

    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #detect collisions with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        scoreboard.reset()
    
    # detect collision with tail.
    #if head collides with itself:
    # trigger game_over
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()









screen.exitonclick()

