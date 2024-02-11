import pygame
import random

# Pygame başlatılıyor
pygame.init()

# Ekran ayarları
genislik, yukseklik = 800, 600
ekran = pygame.display.set_mode((genislik, yukseklik))

# Renkler
mavi = (0, 0, 255)
beyaz = (255, 255, 255)

# FPS (Saniyedeki Kare Sayısı) ayarı
fps = 30
saat = pygame.time.Clock()

# Oyuncu ayarları
oyuncu_img = pygame.image.load('player.png')  # Yol doğru olduğundan emin olun
oyuncu_x, oyuncu_y = genislik / 2, yukseklik - 100

# Olta ayarları
olta_hareket = False
olta_firlatildi = False
olta_hizi = 10
olta_x, olta_y = oyuncu_x + 22, oyuncu_y - 10

# Balık ayarları
baliklar = []
for i in range(5):
    balik_x = random.randint(0, genislik-10)
    balik_y = random.randint(50, yukseklik-100)
    baliklar.append([balik_x, balik_y])

# Skor
skor = 0
font = pygame.font.SysFont(None, 36)

# Oyun döngüsü
calisiyor = True
while calisiyor:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyor = False
        elif olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_SPACE and not olta_firlatildi:
                olta_firlatildi = True
                olta_hareket = True
                olta_x, olta_y = oyuncu_x + 22, oyuncu_y - 10

    tuslar = pygame.key.get_pressed()
    
    # Oyuncu hareketi
    if tuslar[pygame.K_LEFT] and oyuncu_x > 0:
        oyuncu_x -= 5
        if not olta_firlatildi:
            olta_x = oyuncu_x + 22
    if tuslar[pygame.K_RIGHT] and oyuncu_x < genislik - 50:
        oyuncu_x += 5
        if not olta_firlatildi:
            olta_x = oyuncu_x + 22

    # Olta hareketi
    if olta_firlatildi and olta_hareket:
        olta_y -= olta_hizi
        if olta_y < 0:
            olta_firlatildi = False
            olta_hareket = False
            olta_y = oyuncu_y - 10  # Oltayı oyuncunun yüksekliğine geri getir

    # Balık yakalama kontrolü
    for balik in baliklar[:]:
        if olta_firlatildi and olta_x in range(balik[0], balik[0]+10) and olta_y in range(balik[1], balik[1]+10):
            baliklar.remove(balik)
            olta_firlatildi = False
            olta_hareket = False
            skor += 1
            # Yeni balık ekleyin
            yeni_balik_x = random.randint(0, genislik-10)
            yeni_balik_y = random.randint(50, yukseklik-100)
            baliklar.append([yeni_balik_x, yeni_balik_y])

    ekran.fill(mavi)
    ekran.blit(oyuncu_img, (oyuncu_x, oyuncu_y))
    if olta_hareket or not olta_firlatildi:
        pygame.draw.rect(ekran, beyaz, pygame.Rect(olta_x, olta_y, 5, 10))
    for balik in baliklar:
        pygame.draw.rect(ekran, beyaz, pygame.Rect(balik[0], balik[1], 10, 5))
    skor_goster = font.render("Skor: " + str(skor), True, beyaz)
    ekran.blit(skor_goster, (10, 10))

    pygame.display.flip()
    saat.tick(fps)

pygame.quit()
