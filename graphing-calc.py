from math import *
import pygame

# initialize
pygame.init()
font = pygame.font.Font(None, 20)

# settings
WIDTH, HEIGHT = 500, 500
RATE = 1000
SIZE = 20

# color settings
BGCOL = (0, 0, 0)
GRIDCOL = (63, 63, 63)
AXESCOL = (255, 255, 255)
FCOL = (255, 0, 0)

# function to graph
def f(x):
    return tan(x)

# coordinate transforms
def ctrans(x, y):
    sx = WIDTH // 2 + x * (WIDTH / SIZE)
    sy = HEIGHT // 2 - y * (WIDTH / SIZE)
    return int(sx), int(sy)

# factorial
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# point list
fp = []

# calculate points in math coordinates
cx = -SIZE / 2
while cx <= SIZE / 2:
    try:
        y = f(cx)
        if -SIZE / 2 <= y <= SIZE / 2:
            fp.append((cx, y))
    except:
        pass
    cx += 1 / RATE
cx = -SIZE / 2

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("graphing calc")

# bg color
screen.fill(BGCOL)

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # grid
    for i in range(10):
        pygame.draw.line(screen, GRIDCOL, (WIDTH // 10 * i, 0), (WIDTH // 10 * i, HEIGHT), 2)
    for i in range(10):
        pygame.draw.line(screen, GRIDCOL, (0, HEIGHT // 10 * i), (WIDTH, HEIGHT // 10 * i), 2)

    # axes
    pygame.draw.line(screen, AXESCOL, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
    pygame.draw.line(screen, AXESCOL, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 2)
    
    # numbers
    pts = font.render(str(SIZE / 2), False, AXESCOL)
    nts = font.render(str(-SIZE / 2), False, AXESCOL)
    screen.blit(nts, (4, (HEIGHT // 2) + 4))
    screen.blit(pts, (WIDTH - pts.get_width() - 4, (HEIGHT // 2) + 4))
    screen.blit(pts, ((WIDTH // 2) + 6, 4))
    screen.blit(nts, ((WIDTH // 2) + 6, HEIGHT - nts.get_height() - 4))

    # draw points
    for x, y in fp:
        sx, sy = ctrans(x, y)
        pygame.draw.circle(screen, FCOL, (sx, sy), 2)

    # update display
    pygame.display.flip()

pygame.quit()