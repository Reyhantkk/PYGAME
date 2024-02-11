import pygame
import random

# Pygame başlatılıyor
pygame.init()

# Pencere ayarları
Genislik = 800
Yukseklik = 600
pencere = pygame.display.set_mode((Genislik, Yukseklik))

# Renkler
Beyaz = (255, 255, 255)
Kirmizi = (255, 0, 0)

# FPS ayarı
saat = pygame.time.Clock()
FPS = 30

# Karakter ve yem tanımlamaları
canavar = pygame.Rect(Genislik // 2, Yukseklik // 2, 50, 50)
yem = pygame.Rect(random.randint(0, Genislik-20), random.randint(0, Yukseklik-20), 20, 20)

# Skor
skor = 0
font = pygame.font.SysFont(None, 36)

# Oyun döngüsü
calisiyor = True
while calisiyor:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyor = False

    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT]:
        canavar.x -= 5
    if tuslar[pygame.K_RIGHT]:
        canavar.x += 5
    if tuslar[pygame.K_UP]:
        canavar.y -= 5
    if tuslar[pygame.K_DOWN]:
        canavar.y += 5

    # Canavarın ekran dışına çıkmasını önleme
    if canavar.left < 0:
        canavar.left = 0
    elif canavar.right > Genislik:
        canavar.right = Genislik
    if canavar.top < 0:
        canavar.top = 0
    elif canavar.bottom > Yukseklik:
        canavar.bottom = Yukseklik

    # Yem yeme kontrolü
    if canavar.colliderect(yem):
        skor += 1
        yem.x = random.randint(0, Genislik-20)
        yem.y = random.randint(0, Yukseklik-20)

    # Ekranı temizleme ve yeniden çizme
    pencere.fill(Beyaz)
    pygame.draw.rect(pencere, Kirmizi, canavar)
    pygame.draw.ellipse(pencere, (0, 255, 0), yem)

    # Skorun gösterilmesi
    skor_goster = font.render("Skor: " + str(skor), True, (0, 0, 0))
    pencere.blit(skor_goster, (10, 10))

    pygame.display.flip()
    saat.tick(FPS)

# Oyun döngüsü
calisiyor = True
while calisiyor:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyor = False

    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT]:
        canavar.x -= 5
    if tuslar[pygame.K_RIGHT]:
        canavar.x += 5
    if tuslar[pygame.K_UP]:
        canavar.y -= 5
    if tuslar[pygame.K_DOWN]:
        canavar.y += 5

    # Yem yeme kontrolü
    canavar_resim = pygame.Surface((50, 50))  # Example surface for "canavar_resim"
    canavar_resim.fill((255, 0, 0))  # Example fill color for "canavar_resim"

    yem_resim = pygame.Surface((20, 20))  # Example surface for "yem_resim"
    yem_resim.fill((0, 255, 0))  # Example fill color for "yem_resim"

    if canavar.colliderect(yem):
        skor += 1
        yem.topleft = (random.randint(0, Genislik - yem.width), random.randint(0, Yukseklik - yem.height))

    # Ekranı temizleme ve yeniden çizme
    pencere.fill((255, 255, 255))  # Beyaz arka plan, resim yoksa
    # Arka plan resmi varsa: pencere.blit(arka_plan_resim, (0, 0))
    pencere.blit(canavar_resim, canavar)
    pencere.blit(yem_resim, yem)

    # Skorun gösterilmesi
    skor_goster = font.render("Skor: " + str(skor), True, (0, 0, 0))
    pencere.blit(skor_goster, (10, 10))

    pygame.display.flip()
    saat.tick(FPS)

pygame.quit()