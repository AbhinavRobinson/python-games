import pygame

pygame.init()

dis = pygame.display.set_mode((900, 600))
pygame.display.set_caption("PYris")
clock = pygame.time.Clock()


def main():
    # GAME LOOP START
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    pygame.display.update()

    dis.fill(0)
    clock.tick(30)


main()
