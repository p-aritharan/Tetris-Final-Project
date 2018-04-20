import sys
import pygame

# def rot_center(image, angle):
#     """rotate an image while keeping its center and size"""
#     orig_rect = image.get_rect()
#     rot_image = pygame.transform.rotate(image, angle)
#     rot_rect = orig_rect.copy()
#     rot_rect.center = rot_image.get_rect().center
#     rot_image = rot_image.subsurface(rot_rect).copy()
#     return rot_image

IMG1 = pygame.image.load("Block1.gif")
# two rotations
IMG100 = IMG1
IMG200 = pygame.transform.rotate(IMG1, 90)
# Put the images into a list or tuple.
IMAGES = [IMG100, IMG200]

def main():
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    bg_color = pygame.Color(30, 40, 60)
    # Use this rect for the collision detection and blitting.
    img_rect = IMG1.get_rect(center=(200, 200))
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