import pygame

pygame.init()

# Pencere oluşturuluyor
pencere = pygame.display.set_mode((800, 600))

genislik = 800
yukseklik = 600
pencere = pygame.display.set_mode((genislik, yukseklik))

durum=True
while durum:
    for event in pygame.event.get():
        print(event)
        # Pencere kapatma işlemi
        if event.type==pygame.QUIT:
            durum=False
  
pygame.quit()

