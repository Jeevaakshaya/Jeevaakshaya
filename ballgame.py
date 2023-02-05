# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import turtle
import winsound


score_a=0
score_b=0

win =turtle.getscreen()
win.setup(800,600) #
win.bgcolor("blue")
win.title("ball game")
win.tracer(0)

#left paddle
left_paddle=turtle.turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=1,stretch_lens=5)
left_paddle.penup()
left_paddle.got(-380,0)

#right paddle
right_paddle=turtle.turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=1,stretch_lens=5)
right_paddle.penup()
right_paddle.got(380,0)

#ball
ball =turtle.turtle()
ball.shape("circle")
ball.speed(0)
ball.color("white")
ball.goto(0,0)
ball.shapesize(stretch_wid=5,strength_len=1)
ball.penup()
ball.dx=0.25
ball.dy-0.25


pen=turtle.turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("player A:0 player B:0",align="center",font=("Ariel",24,"normal"))


def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)
def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)
def right_paddle_down():
    right_paddle.sety(right_paddle.ycor()-20)

win.listen()
win.onkeypress(left_paddle_up,'w')
win.onkeypress(left_paddle_down,'s')
win.onkeypress(right_paddle_up,'up')
win.onkeypress(right_paddle_down,'down')


while True:
    win.update()
    
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1
        
    if ball.ycor()<-290:
         ball.sety(-290)
         ball.dy *=-1 
         
    if ball.xcor()>390:
         ball.setx(390)
         ball.dx *=-1   
         
         score_a +=1
         pen.clear()
         pen.write("player A:{} player B:{} ".format(score_a,score-b),align="center",font=("Ariel",24,"normal")
    
    if ball.xcor()<-390:
         ball.setx(-390)
         ball.dx *=-1   
         
         score_b +=1
         pen.clear()
         pen.write("player A:{} player B:{} ".format(score_a,score-b),align="center",font=("Ariel",24,"normal")
    if ball.xcor()>370 and right_paddle.ycor()-50<ball.ycor()<right_paddle.ycor()+50:
        ball.setx(360)
        ball.dx *= -1
        
    if ball.xcor()<-370 and left_paddle.ycor()-50<ball.ycor()<left_paddle.ycor()+50:
        ball.setx(-370)
        ball.dx *= -1    
                                
while True:
    win.update()                
         



