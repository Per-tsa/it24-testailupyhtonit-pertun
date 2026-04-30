# simple pong 

import turtle
import time
import winsound
import os
import random

ik = turtle.Screen()
ik.title("Pong by pertsa")
ik.bgcolor("black")
ik.setup(width=800, height=600)
ik.tracer(6)

# Pisteytys
piste_vas = 0
piste_oik = 0

# Palkki vas
pal_vas = turtle.Turtle()
pal_vas.speed(0)
pal_vas.shape("square")
pal_vas.color("white")
pal_vas.shapesize(stretch_wid=5, stretch_len=1)
pal_vas.penup()
pal_vas.goto(-350, 0)

# Palkki oik
pal_oik = turtle.Turtle()
pal_oik.speed(0)
pal_oik.shape("square")
pal_oik.color("white")
pal_oik.shapesize(stretch_wid=5, stretch_len=1)
pal_oik.penup()
pal_oik.goto(350, 0)

# Pallo
pallo = turtle.Turtle()
pallo.speed(0)
pallo.shape("square")
pallo.color("white")
pallo.penup()
pallo.goto(0, 0)
pallo.dx = 1
pallo.dy = -1

# Kynä
kynä = turtle.Turtle()
kynä.speed(0)
kynä.color("white")
kynä.penup()
kynä.hideturtle()
kynä.goto(0, 260)
kynä.write("Pelaaja A: 0   Pelaaja B: 0", align="center", font=("Courier", 24, "normal"))


# funktiot / liikkeet
    #Vasen

def pal_vas_up():
    y = pal_vas.ycor()
    y += 20
    pal_vas.sety(y)

def pal_vas_dwn():
    y = pal_vas.ycor()
    y -= 20
    pal_vas.sety(y)

    #Oikea

def pal_oik_up():
    y = pal_oik.ycor()
    y += 20
    pal_oik.sety(y)

def pal_oik_dwn():
    y = pal_oik.ycor()
    y -= 20
    pal_oik.sety(y)

# äänet
def random_ääni_boing(kansio, boing):
    vastaavat = [
        os.path.join(kansio, f)
        for f in os.listdir(kansio)
        if boing.lower() in f.lower() and f.lower().endswith('.wav')
    ]
    return random.choice(vastaavat) if vastaavat else None

def random_ääni_bounce(kansio, bounce):
    vastaavat2 = [
        os.path.join(kansio, f)
        for f in os.listdir(kansio)
        if bounce.lower() in f.lower() and f.lower().endswith('.wav')
    ]
    return random.choice(vastaavat2) if vastaavat2 else None

# Näppäin inputs
ik.listen()
ik.onkeypress(pal_vas_up, "w")
ik.onkeypress(pal_vas_dwn, "s")
ik.onkeypress(pal_oik_up, "Up")
ik.onkeypress(pal_oik_dwn, "Down")


# Main loop
while True:
    ik.update()
    time.sleep(1 / 200)

    # pallon liike
    pallo.setx(pallo.xcor() + pallo.dx)
    pallo.sety(pallo.ycor() + pallo.dy)

    # rajapyykki
    if pallo.ycor() > 290:
        pallo.sety(290)
        pallo.dy *= -1
        sound_file = random_ääni_boing(r"C:\Users\p70911\pyhton treeni\pong\sounds", "boing")
        if sound_file:
            winsound.PlaySound(sound_file, winsound.SND_ASYNC)
        
    if pallo.ycor() < -290:
        pallo.sety(-290)
        pallo.dy *= -1
        sound_file = random_ääni_boing(r"C:\Users\p70911\pyhton treeni\pong\sounds", "boing")
        if sound_file:
            winsound.PlaySound(sound_file, winsound.SND_ASYNC)

    if pallo.xcor() > 390:
        pallo.goto(0, 0)
        pallo.dx *= -1
        piste_vas += 1
        kynä.clear()
        kynä.write("Pelaaja A: {}   Pelaaja B: {}".format(piste_vas, piste_oik), align="center", font=("Courier", 24, "normal"))
        
    if pallo.xcor() < -390:
        pallo.goto(0, 0)
        pallo.dx *= -1
        piste_oik += 1
        kynä.clear()
        kynä.write("Pelaaja A: {}   Pelaaja B: {}".format(piste_vas, piste_oik), align="center", font=("Courier", 24, "normal"))
        
    # palkin ja pallon kohtaaminen
    if (pallo.xcor() > 340 and pallo.xcor() < 350) and (pallo.ycor () < pal_oik.ycor() + 40 and pallo.ycor() >pal_oik.ycor() -40):
        pallo.setx(340)
        pallo.dx *= -1
        sound_file = random_ääni_bounce(r"C:\Users\p70911\pyhton treeni\pong\sounds", "bounce")
        if sound_file:
            winsound.PlaySound(sound_file, winsound.SND_ASYNC)

    
    if (pallo.xcor() < -340 and pallo.xcor() > -350) and (pallo.ycor () < pal_vas.ycor() + 40 and pallo.ycor() >pal_vas.ycor() -40):
        pallo.setx(-340)
        pallo.dx *= -1
        sound_file = random_ääni_bounce(r"C:\Users\p70911\pyhton treeni\pong\sounds", "bounce")
        if sound_file:
            winsound.PlaySound(sound_file, winsound.SND_ASYNC)