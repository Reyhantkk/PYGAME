import pygame

pygame.init()

height = 600
width = 800
window = pygame.display.set_mode((width, height))

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
pygame.draw.line(window, blue, (0, 0), (width, height))
pygame.draw.line(window, blue, (0, height), (width, 0))
pygame.draw.rect(window, red, (width/2, height/2, 100, 100))
pygame.draw.circle(window, green, (width/2, height/2), 50)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

