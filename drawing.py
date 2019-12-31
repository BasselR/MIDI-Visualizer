import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

x, y = 50, 50
vx = 10

clock = pygame.time.Clock()
FPS = 60
playtime = 0

screenRect = screen.get_rect()

screen.blit(background, (0, 0))

mainloop = True

while mainloop:

    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0

    x += vx
    screen.blit(background, (0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)

    if(x > screenRect.width or x < 0):
        vx *= -1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

    pygame.display.flip()