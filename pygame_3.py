import pygame

# Pygame modülünü başlat
pygame.init()

# Pencere boyutunu ayarla
window_size = (800, 600)
window = pygame.display.set_mode(window_size)

# Spiderman resmini yükle
spiderman_image = pygame.image.load("spiderman.png")

# Spiderman'in koordinatlarını ayarla
spiderman_rect = spiderman_image.get_rect()
spiderman_rect.topleft = (50, 50)

# Oyun döngüsünü çalıştırma durumunu ayarla
running = True

# Ana döngü
while running:
    # Olayları işle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Spiderman resmini pencereye çiz
    window.blit(spiderman_image, spiderman_rect)
    
    # Ekranı güncelle
    pygame.display.update()

# Pygame'i sonlandır
pygame.quit()
