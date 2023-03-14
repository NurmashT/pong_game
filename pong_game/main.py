from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score_board import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()

    # Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting when the ball goes out of the screen
    if ball.xcor() > 400:
        ball.reset()
        score_board.right_points_increase()
        sleep(1)

    if ball.xcor() < -400:
        ball.reset()
        score_board.left_points_increase()
        sleep(1)


screen.exitonclick()