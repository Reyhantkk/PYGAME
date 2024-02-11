from tkinter import font
import pygame
import random

# Pygame başlatılıyor
pygame.init()

# Ekran ayarları
genislik, yukseklik = 800, 600
ekran = pygame.display.set_mode((genislik, yukseklik))

# Renkler
beyaz = (255, 255, 255)
siyah = (0, 0, 0)
kirmizi = (255, 0, 0)

# FPS (Saniyedeki Kare Sayısı) ayarı
fps = 60
saat = pygame.time.Clock()

# Oyuncu gemisi
oyuncu_img = pygame.image.load('player.png')  # Oyuncu gemisinin görselini yükleyin
oyuncu_x = genislik / 2
oyuncu_y = yukseklik - 100
oyuncu_hizi = 5

# Düşman gemileri
dusman_img = pygame.image.load('enemy.png')  # Düşman gemisinin görselini yükleyin
dusmanlar = []
for i in range(6):
    x = random.randint(50, genislik - 50)
    y = random.randint(50, 150)
    dusmanlar.append([x, y])

# Mermi
mermi_img = pygame.image.load('bullet.png')  # Mermi görselini yükleyin
mermiler = []

# Oyun döngüsü
calisiyor = True
while calisiyor:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            calisiyor = False

    # Oyuncu hareketi
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT] and oyuncu_x > 0:
        oyuncu_x -= oyuncu_hizi
    if tuslar[pygame.K_RIGHT] and oyuncu_x < genislik - 50:
        oyuncu_x += oyuncu_hizi
    
    # Mermi ateşleme
    if tuslar[pygame.K_SPACE]:
        mermiler.append([oyuncu_x + 25, oyuncu_y - 20])

    # Ekranı temizle
    ekran.fill(siyah)

    # Oyuncu gemisini çiz
    ekran.blit(oyuncu_img, (oyuncu_x, oyuncu_y))

    # Düşman gemilerini çiz
    skor = 0  # Define the variable "skor"
    for dusman in dusmanlar:
        ekran.blit(dusman_img, (dusman[0], dusman[1]))

    # Mermileri çiz
    for mermi in mermiler:
        ekran.blit(mermi_img, (mermi[0], mermi[1]))
        mermi[1] -= 10  # Mermiyi yukarı hareket ettir
        if mermi[1] < 0:
            mermiler.remove(mermi)
            
    pygame.display.update()
    saat.tick(fps)

 

pygame.quit()
