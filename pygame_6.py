import pygame

pygame.init()

genişlik = 800
yükseklik = 600
pencere = pygame.display.set_mode((genişlik, yükseklik))

hız = 20
spiderman = pygame.image.load("spiderman.png")
spiderman_koordinat = spiderman.get_rect()
spiderman_koordinat.center = (genişlik // 2, yükseklik // 2)

clock = pygame.time.Clock()

durum = True
while durum:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            durum = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spiderman_koordinat.x -= hız
    if keys[pygame.K_RIGHT]:
        spiderman_koordinat.x += hız
    if keys[pygame.K_UP]:
        spiderman_koordinat.y -= hız
    if keys[pygame.K_DOWN]:
        spiderman_koordinat.y += hız

    pencere.fill((0, 0, 0))  # Arka planı temizle (siyah yap)
    pencere.blit(spiderman, spiderman_koordinat)
    pygame.display.update()
    clock.tick(60)  # FPS'i 60 olarak sınırla

pygame.quit()
