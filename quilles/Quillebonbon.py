from setup import *
def bonbon(taille,x,y,angle=0):

    setup(x,y,angle)

    t=taille
    width(3*t)

    tracer(0)
    
    up()
    forward(t*100)
    left(90)
    forward(t*-20)

    down()

    for i in range(4):

        ed,rf=pos()
    
        dot(120*t,'green')
        right(30)
        up()
        forward(t*60)
        down()
        left(90)
        circle(t*60)

        fillcolor('black')
        begin_fill()
        left(90)
        circle(t*100,62)
        right(90)
        circle(t*-60,40)
        right(45)
        circle(t*-100,72)
        right(45)
        circle(t*-60,40)
        end_fill()

        up()
        left(180)
        circle(t*-60,5)
        down()
        
        pencolor('blue')
        fillcolor('red')
        begin_fill()
        circle(t*-5,80)
        circle(t*-70,20)
        circle(t*70,20)
        circle(t*7,70)
        right(150)
        circle(t*-30,50)
        left(80)
        circle(t*-30,50)
        right(70)
        forward(t*10)
        left(90)
        circle(t*-35,65)
        right(70)
        forward(t*10)
        left(90)
        circle(t*-35,45)
        right(70)
        forward(t*20)
        circle(t*30,40)
        circle(t*-30,30)
        right(107)
        circle(t*60,63)
        end_fill()

        up()
        circle(t*60,125)
        left(185)
        down()

        begin_fill()
        circle(t*5,80)
        circle(t*70,20)
        circle(t*-70,20)
        circle(t*-7,70)
        left(150)
        circle(t*30,50)
        right(80)
        circle(t*30,50)
        left(70)
        forward(t*10)
        right(90)
        circle(t*35,65)
        left(70)
        forward(t*10)
        right(90)
        circle(t*35,45)
        left(70)
        forward(t*20)
        circle(t*-30,40)
        circle(t*30,30)
        left(107)
        circle(t*-60,63)
        end_fill()

        up()
        goto(ed,rf)
        circle(t*150,90)
        down()

    

    update()
    
bonbon(0.5,0,0)

input('')
