from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    if x0 > x1:
        tx, ty = x0, y0
        x0, y0 = x1, y1
        x1, y1 = tx, ty
    if y0 == y1:
        x,y = x0,y0
        while x <= x1:
            plot(screen,color,x,y)
            x = x + 1
        return
    if x0 == x1:
        if y0 > y1:
            tx, ty = x0, y0
            x0, y0 = x1, y1
            x1, y1 = tx, ty
        x,y = x0,y0
        while y <= y1:
            plot(screen,color,x,y)
            y = y + 1
        return
    m = (y1-y0)/(x1-x0)
    if (m <= 1 and m > 0):
        octant1(x0,y0,x1,y1,screen,color)
    if (m > 1):
        octant2(x0,y0,x1,y1,screen,color)
    if (m < -1):
        octant7(x0,y0,x1,y1,screen,color)
    if (m >= -1 and m <= 0):
        octant8(x0,y0,x1,y1,screen,color)

def octant1(x0,y0,x1,y1,screen,color):
    x = x0
    y = y0
    a = y1-y0
    b = -1 * (x1-x0)
    d = (2 * a) + b
    while x <= x1:
        plot(screen,color,x,y)
        if d >= 0:
            y = y + 1
            d = d + (2 * b)
        x = x + 1
        d = d + (2 * a)

def octant2(x0,y0,x1,y1,screen,color):
    x = x0
    y = y0
    a = y1-y0
    b = -1 * (x1-x0)
    d = a + (2 * b)
    while y <= y1:
        plot(screen,color,x,y)
        if d <= 0:
            x = x + 1
            d = d + (2 * a)
        y = y + 1
        d = d + (2 * b)

def octant7(x0,y0,x1,y1,screen,color):
    x = x0
    y = y0
    a = y1-y0
    b = -1 * (x1-x0)
    d = a - (2 * b)
    while y >= y1:
        plot(screen,color,x,y)
        if d >= 0:
            x = x + 1
            d = d + (2 * a)
        y = y - 1
        d = d - (2 * b)

def octant8(x0,y0,x1,y1,screen,color):
    x = x0
    y = y0
    a = y1-y0
    b = -1 * (x1-x0)
    d = (2 * a) - b
    while x <= x1:
        plot(screen,color,x,y)
        if d <= 0:
            y = y - 1
            d = d - (2 * b)
        x = x + 1
        d = d + (2 * a)
