import turtle
import math

def diagonal_line(t, size, angle):
    diagonal = int(math.isqrt((4 * size)**2 + size**2))    
    t.lt(angle)  
    t.fd(diagonal)  
    t.rt(angle)
       
def draw_a(t, size):
    diagonal_line(t, size, angle)
    
    t.pu()
    t.fd(size)
    t.rt(90)
    t.fd(size * 4)
    t.lt(90)
    t.pd()
    
    diagonal_line(t, size, 180 - angle)
    t.pu()
    t.bk(size/2)
    t.rt(90)
    t.fd(size * 2)
    t.lt(90)
    t.pd()
    t.fd(size)
    


if __name__ == '__main__':

    # create and position the turtle
    size = 50
    angle = math.degrees(math.atan(4))  #сell_height = 4 * w, cell_width = 2 * w
    bob = turtle.Turtle()

    draw_a(bob, size)

    turtle.mainloop()