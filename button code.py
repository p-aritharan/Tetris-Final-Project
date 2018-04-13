# took this code from https://stackoverflow.com/questions/44468625/how-to-make-a-button-in-pygame-display-and-update-images
# using this code we can then add the following
#1. startgame button which is activated with mouseclick
#2. click to rotate block and scroll down to have block fall or other way around
import sys
import pygame

# Three images.
IMG1 = pygame.Surface((100, 100))
IMG1.fill((240, 240, 240))
pygame.draw.circle(IMG1, (0, 0, 0), (50, 50), 10)
IMG2 = pygame.Surface((100, 100))
IMG2.fill((240, 240, 240))
pygame.draw.circle(IMG2, (0, 0, 0), (25, 25), 10)
pygame.draw.circle(IMG2, (0, 0, 0), (75, 75), 10)
IMG3 = pygame.Surface((100, 100))
IMG3.fill((240, 240, 240))
pygame.draw.circle(IMG3, (0, 0, 0), (20, 20), 10)
pygame.draw.circle(IMG3, (0, 0, 0), (50, 50), 10)
pygame.draw.circle(IMG3, (0, 0, 0), (80, 80), 10)
# Put the images into a list or tuple.
IMAGES = [IMG1, IMG2, IMG3]

def main():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    bg_color = pygame.Color(30, 40, 60)
    # Use this rect for the collision detection and blitting.
    img_rect = IMG1.get_rect(topleft=(200, 200))
    img_index = 0
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if img_rect.collidepoint(event.pos):
                    img_index += 1
                    # Modulo to cycle between 0, 1, 2.
                    img_index %= len(IMAGES)

        screen.fill(bg_color)
        # Use the index to get the current image and blit
        # it at the img_rect (topleft) position.
        screen.blit(IMAGES[img_index], img_rect)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
    sys.exit()