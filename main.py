import pygame


class App:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.process_running = True
        self.game_running = False
        self.font = pygame.font.SysFont("Times New Roman", 19)
        self.space = Scaling_space_widget(100, 200, 300, 300, )

    def mainloop(self):

        while self.process_running:
            self.events_check()
            self.drawing()

    def events_check(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.process_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.process_running = False
        keys = pygame.mouse.get_pressed()
        keys2 = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        self.space.events_check(events, keys, keys2, mouse_pos)

    def drawing(self):
        self.screen.fill((0, 0, 0))
        self.space.grid_draw(self.screen)
        self.space.draw_func(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    from scaling_space_widget import Scaling_space_widget

    app = App()
    app.mainloop()
