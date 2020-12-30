from setup import *
def pates(taille,x,y,angle=0):

    setup(x,y,angle)

    t=taille

    tracer(0)

    width(4*t)
    pencolor('black')

    #Fermeture du paquet
    fillcolor('#e2261a')
    begin_fill()
    up()
    forward(t*15)
    left(90)
    forward(t*125)
    down()

    forward(t*20)
    right(20)
    forward(t*20)
    left(20)
    circle(t*12,100)
    g,h=pos()
    left(50)
    forward(t*25)
    circle(t*6,180)
    up()
    goto(g,h)
    down()
    left(40)
    circle(t*-15,70)
    left(152)
    circle(t*700,10)
    circle(t*-200,17)
    circle(t*10,70)
    forward(t*30)
    y,u=pos()
    circle(t*8,120)
    up()
    forward(t*30)
    down()
    forward(t*50)
    up()
    forward(t*30)
    down()
    forward(t*35)

    up()
    goto(y,u)
    down()
    right(140)
    circle(t*15,40)
    circle(t*100,18)
    left(90)
    circle(t*-75,45)
    circle(t*30,50)
    right(15)
    circle(t*350,15)
    circle(t*-30,30)
    left(50)
    forward(t*28)
    end_fill()

    #Paquet 
    fillcolor('#e5cd9c')
    begin_fill()
    right(125)
    circle(t*-1600,8.7)
    right(20)
    circle(t*-60,70)
    left(3)
    forward(t*70)
    circle(t*-90,32)
    right(45)
    circle(t*-1600,8.4)
    right(78)
    circle(t*-75,45)
    circle(t*30,50)
    right(15)
    circle(t*350,15)
    circle(t*-30,30)
    left(50)
    forward(t*28)
    end_fill()

    up()
    right(127)
    circle(t*-1600,8.7)
    down()
    fillcolor('#e2261a')
    begin_fill()
    right(20)
    circle(t*-60,70)
    left(3)
    forward(t*70)
    circle(t*-90,30)
    left(126)
    forward(t*28)
    circle(t*10,80)
    right(15)
    circle(t*50,40)
    circle(t*-100,30)
    circle(t*200,19)
    circle(t*10,80)
    right(20)
    circle(t*70,34)
    end_fill()

    up()
    left(140)
    circle(t*-60,50)
    down()

    right(60)
    fillcolor('#126849')
    begin_fill()
    circle(t*70,93)
    end_fill()

    up()
    left(140)
    forward(t*8)
    left(30)

    fillcolor('white')
    begin_fill()
    circle(t*-70,75)
    end_fill()

    up()
    left(215)
    forward(t*20)
    right(20)
    fillcolor('red')
    begin_fill()
    circle(t*70,50)
    end_fill()

    up()
    right(113)
    forward(t*65)

    forward(t*165.5)
    right(80)
    forward(t*34)
    begin_fill()
    forward(t*20)
    right(97)
    forward(t*169)
    fillcolor('#126849')
    circle(t*-10,180)
    forward(t*165.5)
    end_fill()
    left(180)
    fillcolor('white')
    begin_fill()
    forward(t*165.5)
    right(90)
    circle(t*100,10)
    right(60)
    circle(t*10,50)
    f,g=pos()
    right(93)
    forward(t*165.5)
    right(90)
    forward(t*18)
    end_fill()

    up()
    goto(f,g)
    left(160)
    fillcolor('red')
    begin_fill()
    circle(t*10,100)
    right(168)
    forward(t*168.5)
    right(80)
    forward(t*20)
    end_fill()
    
    up()
    backward(t*75)
    right(90)
    forward(t*9)
    left(68)
    down()

    
    fillcolor('#126849')
    begin_fill()
    circle(t*400,23)
    circle(t*-5,110)
    circle(t*1600,2.1)
    circle(t*-5,73)
    circle(t*-300,28)
    circle(t*-5,80)
    circle(t*100,30)
    end_fill()

    pencolor('white')
    up()
    left(166)
    forward(t*60)
    down()
    write('PÂTES', font=("Arial",int(35*t), "normal"))
    
    
    update()


pates(0.5,0,0)