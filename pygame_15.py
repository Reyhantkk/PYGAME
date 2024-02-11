import pygame
import sys

# Pygame'i başlat
pygame.init()

# Ekran boyutları
genislik, yukseklik = 800, 400
ekran = pygame.display.set_mode((genislik, yukseklik))

# Renkler
beyaz = (255, 255, 255)
siyah = (0, 0, 0)

# Oyun elemanları
top_hizi = [5, 5]
top = pygame.Rect(genislik / 2 - 15, yukseklik / 2 - 15, 30, 30)
oyuncu1 = pygame.Rect(genislik - 20, yukseklik / 2 - 70, 10, 140)
oyuncu2 = pygame.Rect(10, yukseklik / 2 - 70, 10, 140)

# FPS ayarı
fps = 60
saat = pygame.time.Clock()

# Oyun döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Oyuncu kontrolleri
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_UP] and oyuncu1.top > 0:
        oyuncu1.y -= 10
    if tuslar[pygame.K_DOWN] and oyuncu1.bottom < yukseklik:
        oyuncu1.y += 10
    if tuslar[pygame.K_w] and oyuncu2.top > 0:
        oyuncu2.y -= 10
    if tuslar[pygame.K_s] and oyuncu2.bottom < yukseklik:
        oyuncu2.y += 10

    # Top hareketi
    top.x += top_hizi[0]
    top.y += top_hizi[1]

    # Top sınırlara çarpma kontrolü
    if top.top <= 0 or top.bottom >= yukseklik:
        top_hizi[1] = -top_hizi[1]
    if top.left <= 0 or top.right >= genislik:
        top_hizi[0] = -top_hizi[0]

    # Top oyunculara çarpma kontrolü
    if top.colliderect(oyuncu1) or top.colliderect(oyuncu2):
        top_hizi[0] = -top_hizi[0]

    # Ekranı temizle
    ekran.fill(siyah)

    # Oyun elemanlarını çiz
    pygame.draw.ellipse(ekran, beyaz, top)
    pygame.draw.rect(ekran, beyaz, oyuncu1)
    pygame.draw.rect(ekran, beyaz, oyuncu2)

    # Orta çizgiyi çiz
    pygame.draw.aaline(ekran, beyaz, (genislik / 2, 0), (genislik / 2, yukseklik))

    pygame.display.flip()
    saat.tick(fps)
