from turtle import Screen
from paddle import *
from ball import *
import time 
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width= 800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # quita la animacion automatica del juego

r_paddle = Paddle((370,0))
l_paddle = Paddle((-370,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()

    #detect the punch with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_horizontal()
       

    #when r paddle misses 
    if ball.xcor() > 390:
        ball.reset()
        scoreboard.l_point()
    
    #when l paddle misses
    if ball.xcor() < -390:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()