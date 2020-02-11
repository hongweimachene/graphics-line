from display import *
from draw import *
import random

s = new_screen()
c = [ 0, 255, 0 ]

# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, YRES / 2, s, c)
# draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)
#
# #octants 8 and 4
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES-1, 0, s, c);
# draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
# draw_line(XRES-1, 0, 0, YRES/2, s, c);
#
# #octants 2 and 6
# c[RED] = 255;
# c[GREEN] = 0;
# c[BLUE] = 0;
# draw_line(0, 0, XRES/2, YRES-1, s, c);
# draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);
#
# #octants 7 and 3
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES/2, 0, s, c);
# draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);
#
# #horizontal and vertical
# c[BLUE] = 0;
# c[GREEN] = 255;
# draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
# draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);


for i in range(10000):
    c[RED] = random.randint(0,255)
    c[BLUE] = random.randint(0,255)
    c[GREEN] = random.randint(0,255)
    draw_line(random.randint(0,XRES-1),random.randint(0,YRES-1),random.randint(10,XRES-9),random.randint(10,YRES-9), s, c)
for i in range(15000):
    c[RED] = 0
    c[BLUE] = 0
    c[GREEN] = 0
    draw_line(random.randint(10,XRES-9),random.randint(10,YRES-9),random.randint(50,XRES-49),random.randint(50,YRES-49), s, c)
for i in range(8000):
    c[RED] = random.randint(0,255)
    c[BLUE] = random.randint(0,255)
    c[GREEN] = random.randint(0,255)
    draw_line(random.randint(50,XRES-49),random.randint(50,YRES-49),random.randint(100,XRES-99),random.randint(100,YRES-99), s, c)
for i in range(8000):
    c[RED] = 0
    c[BLUE] = 0
    c[GREEN] = 0
    draw_line(random.randint(100,XRES-99),random.randint(100,YRES-99),random.randint(150,XRES-149),random.randint(150,YRES-149), s, c)
for i in range(4000):
    c[RED] = random.randint(0,255)
    c[BLUE] = random.randint(0,255)
    c[GREEN] = random.randint(0,255)
    draw_line(random.randint(150,XRES-149),random.randint(150,YRES-149),random.randint(200,XRES-199),random.randint(200,YRES-199), s, c)
for i in range(2500):
    c[RED] = 0
    c[BLUE] = 0
    c[GREEN] = 0
    draw_line(random.randint(200,XRES-199),random.randint(200,YRES-199),random.randint(250,XRES-249),random.randint(250,YRES-249), s, c)
for i in range(2500):
    c[RED] = random.randint(0,255)
    c[BLUE] = random.randint(0,255)
    c[GREEN] = random.randint(0,255)
    draw_line(random.randint(225,XRES-224),random.randint(225,YRES-224),random.randint(250,XRES-249),random.randint(250,YRES-249), s, c)
for i in range(2500):
    c[RED] = 0
    c[BLUE] = 0
    c[GREEN] = 0
    draw_line(random.randint(240,XRES-239),random.randint(240,YRES-239),random.randint(250,XRES-249),random.randint(250,YRES-249), s, c)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
print("\n\nImage file is called pic.png\nMight take a while to run file\n\n")
