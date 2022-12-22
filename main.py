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
        self.frames = 0
        self.frames_for_wait = 10
        self.history_mode = False
        if self.history_mode:
            self.points_history = [self.points]
            self.now_way = 0
        self.points = [(-14.0, -1.0), (-13.0, -1.0), (-13.0, -2.0), (-14.0, -2.0), (-4.0, -1.0), (-4.0, -2.0),
                       (-4.0, -3.0),
                       (-3.0, 0.0), (-3.0, -4.0), (-1.0, -5.0), (-2.0, -5.0), (-2.0, 1.0), (-1.0, 1.0), (0.0, -2.0),
                       (1.0, 0.0),
                       (1.0, -4.0), (2.0, -1.0), (2.0, -2.0), (2.0, -3.0), (3.0, -2.0), (6.0, -1.0), (7.0, -1.0),
                       (7.0, 0.0),
                       (6.0, 0.0), (6.0, 1.0), (7.0, 1.0), (8.0, -2.0), (8.0, 2.0), (10.0, 2.0), (10.0, 3.0),
                       (10.0, -2.0),
                       (10.0, -3.0), (20.0, 0.0), (20.0, 1.0), (21.0, 1.0), (21.0, 0.0)]
        self.font = pygame.font.SysFont("Times New Roman", 19)

        self.space = Scaling_space_widget(0, 0, 300, 300, "x^2")
        self.space2 = Scaling_space_widget(400, 100, 300, 300, "sinx")
        self.space3 = Scaling_space_widget(800, 200, 300, 300, False, 1.3)
        # for lissajous
        self.a = 3
        self.b = 2
        self.am_a = 100
        self.am_b = 100
        self.phase_shift = 2
        self.t = 0
        self.frames_for_t = 1
        self.frames_counter = 0
        self.lissajous_cords = [
            self.space3.create_lissajous(self.a, self.b, self.am_a, self.am_b, self.phase_shift, self.t)]

    def mainloop(self):
        while self.process_running:
            self.events_check()
            self.drawing()
            if self.frames_counter >= self.frames_for_wait:
                self.frames_counter = 0
                self.t += 1
                self.lissajous_cords.append(
                    self.space.create_lissajous(self.a, self.b, self.am_a, self.am_b, self.phase_shift, self.t))
            self.frames_counter += 1

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
        self.space2.events_check(events, keys, keys2, mouse_pos)
        self.space3.events_check(events, keys, keys2, mouse_pos)

    def drawing(self):
        self.screen.fill((0, 0, 0))
        self.space.grid_draw(self.screen)
        self.space2.grid_draw(self.screen)
        self.space.draw_func(self.screen)
        self.space2.draw_func(self.screen)
        self.space3.grid_draw(self.screen)
        self.space3.draw_lissajous(self.screen, self.lissajous_cords)
        pygame.display.update()


if __name__ == '__main__':
    from scaling_space_widget import Scaling_space_widget

    app = App()

    app.mainloop()
