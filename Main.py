# <----------------Librarys---------------->
from turtle import Screen
from Snake import Snake
from Food import Food
from Scorboard import Scorboard
from intro import start
from startname import Startname
import time

# <----------------Screen---------------->
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
play_again=True

# <---------------Main Class ---------------->
def game():
    screen.clear()
    screen.bgcolor("black")
    # <----------------Classes---------------->
    intros = start()
    startname = Startname()
    food = Food()
    scorboard = Scorboard()
    screen.tracer(0)
    snake = Snake()

    # <----------------Control---------------->
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    # <----------------Loop---------------->
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.xcor() > 275 or snake.head.xcor() < -275 or snake.head.ycor() > 275 or snake.head.ycor() < -275:
            game_is_on = False
            scorboard.gameover()
        for seg in snake.segements[1:]:
            if snake.head.distance(seg) < 5:
                game_is_on = False
                scorboard.gameover()
        if snake.head.distance(food.food) < 15:
            food.refresh()
            snake.exted_snake()
            scorboard.increse_score()

# <---------------Main loop ---------------->
while True:
    game()
    user_input = screen.textinput("Input", "Do You Want to play again (Y/N)").strip().lower()
    if user_input !="y":

        break

screen.exitonclick()
