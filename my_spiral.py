import turtle
import math

def draw_spiral(t, n):
    """Draws an Archimedian spiral starting at the origin.
    Args:
      n: how many line segments to draw
      length: how long each segment is
      https://ru.wikipedia.org/wiki/%D0%90%D1%80%D1%85%D0%B8%D0%BC%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0_%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BB%D1%8C
      r = k*beta
      dl = k*dbeta*sqrt(1+beta**2)    
    """
    length = 0
    beta = 0  # initial roll angle
    dbeta = 2 # step of roll angle in degree
    k = 0.05
    
    for i in range(n):
        t.fd(length)  
        t.lt(dbeta)
        
        w = math.sqrt(1 + (math.radians(beta))**2)
        
        dlength = k * math.radians(dbeta) * w 
        beta += dbeta
        length += dlength      #length_arc = integral(dlength) = sum (dlength)


# create the world and bob
bob = turtle.Turtle()
draw_spiral(bob, n=600)

turtle.mainloop()
