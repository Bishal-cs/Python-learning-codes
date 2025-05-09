import pygame
import sys

# Game variables
gravity = 0.25
bird_movement = 0
bg_surface = pygame.Surface((288, 512))
bg_surface.fill((135, 206, 235))

# Bird properties
bird_surface = pygame.Surface((28, 28))
bird_surface.fill((255, 255, 255))
bird_rect = bird_surface.get_rect(center=(50, 256))

# Pipe properties
pipe_surface = pygame.Surface((40, 512))
pipe_surface.fill((0, 0, 0))
pipe_rect = pipe_surface.get_rect(center=(288, 256))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6

    # Move the bird
    bird_movement += gravity
    bird_rect.centery += bird_movement

    # Draw everything
    screen = pygame.display.set_mode((288, 512))
    screen.blit(bg_surface, (0, 0))
    screen.blit(bird_surface, bird_rect)
    screen.blit(pipe_surface, pipe_rect)
    pygame.display.flip()

