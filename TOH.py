# %%
import pygame as pg
import sys
import os

# =================================================================
# CONFIGURATION
# =================================================================
# Number of discs (n). You can change this value to adjust difficulty.
ndisc = 5

# NOTE: This algorithm solves the Tower of Hanoi using the 
# "Optimal Strategy," requiring the minimum number of moves: (2^n) - 1.
# =================================================================

pg.init()
screen = pg.display.set_mode((1000, 800))

# Using system fonts to ensure it runs on any computer
font = pg.font.SysFont('Arial', 50)
pg.display.set_caption('Tower of Hanoi - Optimal Solution Visualization')
clock = pg.time.Clock()

data = []
position = [ndisc, 0, 0]
polx = [200, 275, 350, 425, 500, 575, 650, 725, 800]
bottom = 600
width = 30
posdisc = []
c = 0

# Recursive function to calculate the Tower of Hanoi solution
def tower_of_hanoi_logic(a, b, c, n):
    if n > 0:
        tower_of_hanoi_logic(a, c, b, n - 1)
        data.append([a, c, n])
        tower_of_hanoi_logic(b, a, c, n - 1)

# Pre-calculate optimal moves
tower_of_hanoi_logic(0, 4, 8, ndisc)

# Initial setup of discs on the first peg
for i in range(ndisc):
    posdisc.append([i + 1, 0, ndisc - i - 1])

# Fetch the first movement data
working = data.pop(0)
posdisc.pop(0)
x = working[0]
xstop = working[1]
disc = working[2]
y = position[int(x/4)]
ystop = position[int(xstop/4)]
ymax = 8

position[int(x/4)] -= 1
position[int(xstop/4)] += 1

sign = 1 if x < xstop else -1

# Main Loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            os._exit(0)

    screen.fill((255, 255, 255))
    screen.blit(font.render("Move Count :", True, 'black'), (290, 700))
    
    # Draw static discs
    for dd in list(posdisc):
        pg.draw.rect(screen, 'Black', (polx[dd[1]] - dd[0] * width, bottom - dd[2] * 50, dd[0] * width * 2, 50))
    
    # Draw moving disc
    pg.draw.rect(screen, 'Black', (polx[x] - disc * width, bottom - y * 50, disc * width * 2, 50))

    # Render Move Counter
    co = font.render(str(c - 1), True, 'white')
    cou = font.render(str(c), True, 'black')
    screen.blit(co, (600, 700))
    screen.blit(cou, (600, 700))

    # Movement Logic
    if y < ymax and x != xstop:
        y += 1
    elif x != xstop:
        x += sign
    elif y > ystop:
        y -= 1
        if y == ystop:
            c += 1
    else:
        # Prepare next move
        posdisc.append([disc, x, y])
        if data:
            working = data.pop(0)
            x, xstop, disc = working[0], working[1], working[2]
            y = position[int(x/4)]
            ystop = position[int(xstop/4)]
            position[int(x/4)] -= 1
            position[int(xstop/4)] += 1
            
            try:
                posdisc.pop(posdisc.index([disc, x, y - 1]))
            except ValueError:
                pass
                
            sign = 1 if x < xstop else -1

    clock.tick(60)
    pg.display.update()


