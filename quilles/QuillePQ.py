from setup import *

def PQ (taille,x,y,angle=0):

    t=taille

    setup(x,y,angle)

    up()
    backward(t*300)
    left(90)
    forward(-30*t)
    down()
    
    tracer(0)

    left(225)
    width(2*t)


    pencolor('black')
    fillcolor('#FBCEF2')
    begin_fill()
    circle(1000*t,15)
    left(5)
    circle(1000*t,15)
    circle(50*t,50)
    circle(25*t,20)
    left(30)
    circle(25*t,20)
    circle(50*t,50)
    right(25)
    circle(1000*t,15)
    left(5)
    circle(1000*t,15)
    circle(50*t,50)
    circle(25*t,20)
    left(30)
    circle(25*t,20)
    circle(50*t,50)

    end_fill()
    up()
    right(25)
    forward(150*t)
    left(90)
    forward(50*t)
    right(90)
    down()
    
    i=0.7
    width(2*t)
    pencolor('black')
    fillcolor('#A17B66')
    begin_fill()
    circle(500*i*t,15)
    left(5)
    circle(500*i*t,15)
    circle(25*i*t,50)
    circle(12.5*i*t,20)
    left(30)
    circle(12.5*i*t,20)
    circle(25*i*t,50)
    right(25)
    circle(500*i*t,15)
    left(5)
    circle(500*i*t,15)
    circle(25*i*t,50)
    circle(12.5*i*t,20)
    left(30)
    circle(12.5*i*t,20)
    circle(25*i*t,50)
    end_fill()
   
    up()
    backward(198*t)
    left(90)
    forward(40*t)
    right(7)
    down()

    width(2*t)
    pencolor('black')
    fillcolor('#FBCEF2')
    begin_fill()
    forward(500*t)
    left(15)
    circle(-25*t,20)
    circle(-50*t,50)
    circle(-75*t,20)
    left(5)
    circle(-700*t,20)
    left(5)
    circle(-700*t,20)
    circle(-75*t,20)
    circle(-50*t,50)
    circle(-25*t,20)

    left(17)
    forward(505*t)

    right(153)
    circle(25*t,20)
    circle(50*t,50)
    right(25)
    circle(1000*t,15)
    left(5)
    circle(1000*t,15)
    circle(50*t,40)


    end_fill()

    width(2*t)
    pencolor('black')
    fillcolor('#FBCEF2')
    begin_fill()
    right(80)
    circle(-90*t,18)
    right(10)
    circle(-40*t,50)
    circle(-30*t,50)
    circle(-20*t,10)
    circle(-1000*t,1)
    end_fill()

    fillcolor('#FBCEF2')
    begin_fill()
    circle(-1000*t,14)
    left(90)
    forward(505*t)
    left(90)
    circle(500*t,30)
    circle(20*t,90)
    right(33)
    forward(480*t)
    left(185)
    circle(-40*t,50)
    circle(-30*t,50)
    circle(-20*t,10)
    end_fill()
    right(75)
    forward(70*t)
    update()

PQ(0.5,0,0)
    
