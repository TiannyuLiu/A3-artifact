import turtle
import time
import random
import time
import pygame

def up():
     SBSP.setheading(90)
     SBSP.forward(20)

def down():
    SBSP.setheading(270)
    SBSP.forward(20)

def left():
    SBSP.setheading(180)
    SBSP.forward(20)

def right():
    SBSP.setheading(0)
    SBSP.forward(20)

turtle.bgcolor("lightcyan")
playground = turtle.Screen()
playground.register_shape('MK.gif')
playground.register_shape('SBSP.gif')
playground.onkey(up,'Up')
playground.onkey(down,'Down')
playground.onkey(left,'Left')
playground.onkey(right,'Right')

playground.listen()

writer = turtle.Turtle()
writer.color('brown')
writer.hideturtle()
writer.penup()
writer.home()
writer.write("Don't get catched by MR Krabs",align='center',font=("Comic Sans MS",50,'bold')) 
writer.goto(0,-49)
writer.write("READY?3,2,1,GO!",align='center',font=("Comic Sans MS",19,'bold'))
time.sleep(3)

writer.clear()

url='BGM.mp3'
pygame.mixer.init()
t=pygame.mixer.music.load(url)
pygame.mixer.music.play()

MK= turtle.Turtle()
MK.shape('MK.gif')
MK.penup()
MK.goto(random.randint(-200,200),random.randint(-200,200))



SBSP=turtle.Turtle()
SBSP.shape('SBSP.gif')
SBSP.speed(0)
SBSP.penup()
SBSP.goto(random.randint(-200,200),random.randint(-200,200))
SBSP.color('brown')



start = time.time()
while True:
    MK.setheading(MK.towards(SBSP))
    MK.forward(7)
    if MK.distance(SBSP)<10:
        end = time.time()
        playground.clear()
        SBSP.goto(0,0)
        SBSP.write("Get Back To Work!",align='center',font=("Comic Sans MS",40,'bold'))
        SBSP.goto(0,-50)
        SBSP.write("YOU SURVIVED {:.1f} SECONDS".format(end - start),align='center',font=("Comic Sans MS",20,'bold'))
        MK.pu()
        MK.goto(-50,-70)
        MK.stamp()
        SBSP.pu()
        SBSP.goto(50,-70)
        SBSP.stamp()
        pygame.mixer.music.stop()
        break
