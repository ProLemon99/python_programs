import pygame as pg
from random import randrange

pg.display.set_caption("Snake")
window = 1000
tileSize = 50
range = (tileSize//2, window-tileSize//2, tileSize)
getRandomposition = lambda: [randrange(*range),randrange(*range)]
snake = pg.rect.Rect([0,0, tileSize-2,tileSize-2])
snake.center = getRandomposition()
snake_dir = (0,0)
time = 0
timeStep = 100
food = snake.copy()
food.center = getRandomposition()
length = 1
speedInc = 0
segments = [snake.copy()]
dirs = {pg.K_UP:1, pg.K_DOWN:1, pg.K_LEFT:1, pg.K_RIGHT:1 }
screen = pg.display.set_mode([window]*2)
clock = pg.time.Clock()

while True:
    speedInc = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
              run = False
            if event.key == pg.K_UP:
                snake_dir = (0, - tileSize) 
                dirs = {pg.K_UP:1, pg.K_DOWN:0, pg.K_LEFT:0, pg.K_RIGHT:0 }
            elif event.key == pg.K_DOWN:
                snake_dir = (0, tileSize) 
                dirs = {pg.K_UP:0, pg.K_DOWN:1, pg.K_LEFT:0, pg.K_RIGHT:0 }
            elif event.key == pg.K_LEFT:
                snake_dir = (-tileSize, 0) 
                dirs = {pg.K_UP:0, pg.K_DOWN:0, pg.K_LEFT:1, pg.K_RIGHT:0 }
            elif event.key == pg.K_RIGHT:
                snake_dir = (tileSize, 0) 
                dirs = {pg.K_UP:0, pg.K_DOWN:0, pg.K_LEFT:0, pg.K_RIGHT:1 }
    screen.fill("black")

    # Check if the snake bumps into itself
    selfBump = pg.Rect.collidelist(snake, segments[:-1]) != -1

    # Check if the snake hit the border
    if snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window or selfBump:
        snake.center, food.center = getRandomposition(), getRandomposition()
        length, snake_dir = 1, (0,0)
        segments = [snake.copy()]

    # Check collision
    if snake.center == food.center:
        food.center = getRandomposition()
        length = length + 1
        speedInc = speedInc + 0.5

    # Draw the apples
    pg.draw.rect(screen, 'red', food)

    # Draw the snake
    [pg.draw.rect(screen, 'green', segment)for segment in segments]
    
    # Move the snake
    timeNow = pg.time.get_ticks()
    if timeNow - time > timeStep:
        time = timeNow
    snake.move_ip(snake_dir)
    segments.append(snake.copy())
    segments = segments[-length:]
    pg.display.flip()
    clock.tick(10 + speedInc)