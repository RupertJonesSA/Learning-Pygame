import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Azim's Game")

x_cordinate = 500.0
y_cordinate = 300.0

running = True
while running:
    for event in pygame.event.get():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        # parameters take in the screen, color, and size of drawing
        pygame.draw.rect(screen, (r, g, b), (x_cordinate, y_cordinate, 50, 50))
        if event.type == pygame.QUIT:
            pygame.quit()

    button = pygame.key.get_pressed()
    print(x_cordinate, y_cordinate)

    if button[pygame.K_LEFT]:
        x_cordinate -= 1
    if button[pygame.K_RIGHT]:
        x_cordinate += 1
    if button[pygame.K_UP]:
        y_cordinate -= 1
    if button[pygame.K_DOWN]:
        y_cordinate += 1

    if x_cordinate < 0:
        x_cordinate = 0
    if y_cordinate < 0:
        y_cordinate = 0
    if y_cordinate > 600:
        y_cordinate = 600
    if x_cordinate > 800:
        x_cordinate = 800

    # Sets FPS
    pygame.time.Clock().tick(144)
    pygame.display.flip()
