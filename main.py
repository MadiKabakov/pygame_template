import pygame
import sys
from settings import screen_width, screen_height

# Initialize Pygame
pygame.init()
# Create a screen with a specific size
screen = pygame.display.set_mode((screen_width, screen_height))
# Set the window title
pygame.display.set_caption("Pygame simple template")


def run_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    while True:
        run_game()
