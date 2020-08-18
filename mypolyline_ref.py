#from __future__ import print_function, division
#выводит кракозябры в докстринге
import turtle
import math

def polyline(t, n, length, angle):
    """Рисует  n линейных сегментов
    t: Turtle объект
    n: число сегментов
    length: длина каждого сегмента
    angle: угол между сегментами (внешний для многоугольника)
    """
    #angle = 360.0/n  # поворот в градусах(внешний угол многоугольника)
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    #print(t, "parametr 'n':=", n, "'length:=", angle, 'Send to: ', arc)  
    print(polyline, 'got: ')
    print('        ', t)
    print('         parametr "length segment":=', length)
    print('         parametr "outer angle of segments:="', angle)    

def polygon(t, n, length):
    """Рисует правильный n сторонний многоугольник
    t: Turtle объект
    n: число сторон
    length: длина стороны
    """
    angle = 360.0/n  # внешний угол многоугольника
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """Рисует дугу по радиусу и углу
    t: Turtle объект
    r: радиус дуги
    angle: угол между началом и концом дуги в градусах
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 3) + 1     
    # упрощение задачи, заданием n
    step_length = arc_length / n
    step_angle = float(angle) / n
    # making a slight left turn before starting reduces, интересно как
    # the error caused by the linear approximation of the arc
    #t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    #t.rt(step_angle/2)
    print(arc, 'got: ')
    print('        ', t)
    print('         parametr "radius":=', r)
    print('         parametr "angle:="', angle)
    
def circle(t, r):
    """Рисует круг по радиусу
    t: Turtle объект
    r: радиус
    """
    print(circle, 'got: ')
    print('        ', t)
    print('         parametr "radius":=', r)
    arc(t, r, 360)
    

if __name__ == '__main__':
    bob = turtle.Turtle()
    bob.delay = 0.01
    
    # варианты для запуска  
    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    circle(bob, radius)
    #polyline(bob, 5, 20 , 120)
    #arc(bob, radius, 360)
    # wait for the user to close the window
    turtle.mainloop()
