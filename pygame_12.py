import pygame
import random

pygame.init()

# Pencere Ayarları
Genislik, Yukseklik = 800, 600
pencere = pygame.display.set_mode((Genislik, Yukseklik))

# Renkler
Beyaz = (255, 255, 255)
Kirmizi = (255, 0, 0)
Mavi = (0, 0, 255)

# FPS Ayarı
FPS = 60
saat = pygame.time.Clock()

# Karakter ve Mermi Ayarları
canavar = pygame.Rect(Genislik // 2, Yukseklik - 60, 50, 50)
mermi_hizi = 7
mermiler = []

# Oyun Döngüsü
calisiyor = True
while calisiyor:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyor = False
        
        # Ateşleme Olayı
        elif olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_SPACE:
                # Mermiyi canavarın ortasından ateşle
                mermi = pygame.Rect(canavar.centerx - 5, canavar.top, 10, 20)
                mermiler.append(mermi)

    # Karakter Kontrolü
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT] and canavar.left > 0:
        canavar.x -= 5
    if tuslar[pygame.K_RIGHT] and canavar.right < Genislik:
        canavar.x += 5
    
    # Mermilerin Hareketi
    for mermi in mermiler[:]:
        mermi.y -= mermi_hizi
        if mermi.bottom < 0:
            mermiler.remove(mermi)
    
    # Çizimler
    pencere.fill(Beyaz)
    pygame.draw.rect(pencere, Kirmizi, canavar)
    for mermi in mermiler:
        pygame.draw.rect(pencere, Mavi, mermi)
    
    pygame.display.flip()
    saat.tick(FPS)

pygame.quit()
