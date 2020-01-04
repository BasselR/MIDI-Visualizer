import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

x, y = 50, 50
vx = 3

clock = pygame.time.Clock()
FPS = 60
playtime = 0

screenRect = screen.get_rect()

screen.blit(background, (0, 0))

mainloop = True

class Ball(object):
    """this is not a native pygame sprite but instead a pygame surface"""
    def __init__(self, radius = 5, color=(255,0,255), x=320, y=240):
        """create a (black) surface and paint a blue ball on it"""
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        # create a rectangular surface for the ball 50x50
        self.surface = pygame.Surface((2*self.radius,2*self.radius))    
        # pygame.draw.circle(Surface, color, pos, radius, width=0) # from pygame documentation
        pygame.draw.circle(self.surface, color, (radius, radius), radius) # draw blue filled circle on ball surface
        self.surface = self.surface.convert() # for faster blitting. 
        # to avoid the black background, make black the transparent color:
        # self.surface.set_colorkey((0,0,0))
        # self.surface = self.surface.convert_alpha() # faster blitting with transparent color
        
    def blit(self, background):
        """blit the Ball on the background"""
        background.blit(self.surface, (self.x, self.y))

myBall = Ball()

while mainloop:

    milliseconds = clock.tick(FPS)
    playtime += milliseconds / 1000.0

    #x += vx
    myBall.x += 2
    screen.blit(background, (0, 0))
    myBall.blit(background)
    #pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)

    if(x + 30 > screenRect.width or x - 30 < 0):
        vx *= -1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

    pygame.display.update()