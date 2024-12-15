from PALASTINE import flag
from turtle import Turtle,Screen
import time

window=Screen()
window.screensize(700,700)
window.bgcolor("black")
#window.tracer(0)
palastine_MAP=flag(window=window,x=-50,y=0,a=3)
p2=flag(window,-350,250,0.75)
window.update()
sam=Turtle()
sam.penup()
sam.goto(50,250)
sam.pendown()
sam.color('white')
sam.write("FREE PALASTINE ",align="center",font=("Arial",24,"normal"))
sam.penup()
sam.goto(-260,-300)
sam.pendown()
sam.write("ENG. MOHAMED SHABAN ",align="center",font=("Arial",12,"normal"))

window.exitonclick()