from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    pass


def octant1(x0,y0,x1,y1,screen,color):
    if x0 > x1:
        tx, ty = x0, y0
        x0, y0 = x1, y1
        x1, y1 = tx, ty
    x = x0
    y = x1
    a = y1-y0
    b = -1 * (x1-x0)
    d = (2 * a) + b
    while x <= x1:
        plot(screen,color,x,y)
        if d > 0:
            y = y + 1
            d = d + (2 * b)
    x = x + 1
    d = d + (2 * a)

def octant2(x0,y0,x1,y1,screen,color):
    if x0 > x1:
        tx, ty = x0, y0
        x0, y0 = x1, y1
        x1, y1 = tx, ty
    x = x0
    y = x1
    a = y1-y0
    b = -1 * (x1-x0)
    d = a + (2 * b)
    while y <= y1:
        plot(screen,color,x,y)
        if d > 0:
            x = x + 1
            d = d + (2 * a)
    y = y + 1
    d = d + (2 * b)

def octant7(x0,y0,x1,y1,screen,color):
    if x0 > x1:
        tx, ty = x0, y0
        x0, y0 = x1, y1
        x1, y1 = tx, ty
    x = x0
    y = x1
    a = y1-y0
    b = -1 * (x1-x0)
    d = (-1 * a) + (2 * b)
    while y >= y1:
        plot(screen,color,x,y)
        if d > 0:
            x = x + 1
            d = d + (2 * a)
    y = y - 1
    d = d - (2 * b)

def octant8(x0,y0,x1,y1,screen,color):
    if x0 > x1:
        tx, ty = x0, y0
        x0, y0 = x1, y1
        x1, y1 = tx, ty
    x = x0
    y = x1
    a = y1-y0
    b = -1 * (x1-x0)
    d = (2 * a) - b
    while x <= x1:
        plot(screen,color,x,y)
        if d > 0:
            y = y - 1
            d = d - (2 * b)
    x = x + 1
    d = d + (2 * a)
