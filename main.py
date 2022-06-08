import pygame
pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
def events_check():
    global process_running
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                process_running = False
        if event.type == pygame.QUIT:
            process_running = False
def drawing(sprites):
    screen.fill((0, 0, 0))
    for sprite in sprites:
        screen.blit(sprite, (sprite.pos_x, sprite.pos_y))
    pygame.display.update()
def mainloop():
    objects = []
    while process_running:
        events_check()
        pygame.time.delay(20)
        drawing(objects)

if __name__ == '__main__':
    process_running = True
    mainloop()