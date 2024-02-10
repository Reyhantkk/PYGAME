import pygame
import sys

# Pygame'i ve ses sistemini başlat
pygame.init()
pygame.mixer.init()

# Pencere ayarları
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Arka plan müziğini yükle ve oynat
pygame.mixer.music.load('arkaplan_muzigi.mp3')  # Doğru dosya yolunu belirtin
pygame.mixer.music.play(-1)  # Müziği sürekli tekrarla

# Ses efekti yükle
ses_efekti = pygame.mixer.Sound('ses_efekti.wav')  # Doğru dosya yolunu belirtin

# Oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # SPACE tuşuna basıldığında ses efektini oynat
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ses_efekti.play()

    # Arka planı güncelle (opsiyonel)
    screen.fill((0, 0, 0))  # Ekrana siyah bir arka plan çiz

    # Ekranı güncelle
    pygame.display.flip()

# Pygame'i temizle ve çık
pygame.quit()
sys.exit()
