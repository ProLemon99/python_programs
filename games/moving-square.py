import pygame

pygame.init()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
canvas = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
window = pygame.display.set_mode(((SCREEN_WIDTH,SCREEN_HEIGHT)))
running = True
clock = pygame.time.Clock()

TARGET_FPS = 60

# To make the pygame resizeable in your own code editor use pygame.RESIZEABLE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Moving Square")

run = True

x = 10
y = 10

SPEED = 1

clock = pygame.time.Clock()

FPS = 240

while run:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              run = False
            if event.key == pygame.K_LEFT:
                x -= SPEED
            elif event.key == pygame.K_RIGHT:
                x += SPEED
            elif event.key == pygame.K_UP:
                y -= SPEED
            elif event.key == pygame.K_DOWN:
                y += SPEED
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    x -= SPEED
  if keys[pygame.K_RIGHT]:
    x += SPEED
  if keys[pygame.K_UP]:
    y -= SPEED
  if keys[pygame.K_DOWN]:
    y += SPEED
  screen.fill((255, 255, 255))

  pygame.draw.rect(screen, (0, 0, 0), (x, y, 50, 50))

  clock.tick(FPS)
  
  pygame.display.flip()
pygame.quit()