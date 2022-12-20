import pygame
import math
from PIL import Image


class Scaling_space_widget():
    def __init__(self, x, y, width, height, scale=10, scale_value=0.1, camera_speed=1, border_for_camera_moving_x=20,
                 border_for_camera_moving_y=20):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.scale = scale
        self.scale_value = scale_value

        self.font = pygame.font.SysFont("Times New Roman", 19)

        self.camera_center_x = 0
        self.camera_center_y = 0
        self.camera_speed = camera_speed
        self.border_for_camera_moving_x = border_for_camera_moving_x
        self.border_for_camera_moving_y = border_for_camera_moving_y
        self.func_coords = self.create_func()

        self.my_image = Image.open("valakas.jpg")
        self.image_pixels = self.my_image.load()
        self.my_pixels_array = []
        for y in range(self.my_image.size[1]):

            a = []
            for x in range(self.my_image.size[0]):
                a.append(self.image_pixels[x, y])
            self.my_pixels_array.append(a)

    def coordinates_changer(self, x, y):
        # в координаты поля
        x = x - self.x
        y = y - self.y
        new_x = self.camera_center_x + ((x - self.width // 2) / self.scale)
        new_y = self.camera_center_y - ((y - self.height // 2) / self.scale)
        return (new_x, new_y)

    def coordinates_changer_in_pygame(self, x, y):
        distance_x = x - self.camera_center_x
        distance_y = y - self.camera_center_y
        distance_x *= self.scale
        distance_y *= self.scale
        new_x = (self.width // 2 + distance_x)
        new_y = (self.height // 2 - distance_y)
        new_x += self.x
        new_y += self.y
        return (new_x, new_y)

    def grid_draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)
        self.font = pygame.font.SysFont("Times New Roman", int(self.scale) * 2)
        x = self.camera_center_x - (self.camera_center_x % 5)
        y = self.camera_center_y - (self.camera_center_y % 5)
        field_color = (0, 150, 0)

        zero_x = round(self.coordinates_changer_in_pygame(0, 0)[0], 1)
        zero_y = round(self.coordinates_changer_in_pygame(0, 0)[1], 1)

        counter = x
        while counter >= self.coordinates_changer(self.x, 0)[0]:
            pos = self.coordinates_changer_in_pygame(counter, 0)[0]
            pygame.draw.line(screen, field_color, (pos, self.y), (pos, self.y + self.height), 2)
            surface = self.font.render(str(counter), False, (255, 255, 255))
            screen.blit(surface, (pos, self.y))
            counter -= 5
        counter = x

        while counter <= self.coordinates_changer(self.x + self.width, 0)[0]:
            pos = self.coordinates_changer_in_pygame(counter, 0)[0]
            pygame.draw.line(screen, field_color, (pos, self.y), (pos, self.y + self.height), 2)
            surface = self.font.render(str(counter), False, (255, 255, 255))
            screen.blit(surface, (pos, self.y))
            counter += 5
        counter = y
        #
        while counter <= self.coordinates_changer(0, self.y)[1]:
            pos = self.coordinates_changer_in_pygame(0, counter)[1]
            pygame.draw.line(screen, field_color, (self.x, pos), (self.x + self.width, pos), 2)
            surface = self.font.render(str(counter), False, (255, 255, 255))
            screen.blit(surface, (self.x, pos))
            counter += 5

        counter = y
        # #
        while counter >= self.coordinates_changer(0, self.y + self.height)[1]:
            pos = self.coordinates_changer_in_pygame(0, counter)[1]
            pygame.draw.line(screen, field_color, (self.x, pos), (self.x + self.width, pos), 2)
            surface = self.font.render(str(counter), False, (255, 255, 255))
            screen.blit(surface, (self.x, pos))
            counter -= 5

        if self.y < zero_y <= self.y + self.height:
            pygame.draw.line(screen, (0, 0, 255), (self.x, zero_y), (self.x + self.width, zero_y), 5)
        if self.x < zero_x <= self.x + self.width:
            pygame.draw.line(screen, (0, 0, 255), (zero_x, self.y), (zero_x, self.y + self.height), 5)

    def drawing(self, screen):
        self.grid_draw(screen)
        self.draw_func(screen)
        self.draw_image(screen)

    def is_mouse_on_widget(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            return True
        else:
            return False

    def events_check(self, events, mouse_pressed, keyboard_pressed, mouse_pos):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.scale += self.scale_value
                    self.scale = round(self.scale, 2)

                elif event.key == pygame.K_2:
                    if self.scale - self.scale_value >= self.scale_value:
                        self.scale -= self.scale_value
                        self.scale = round(self.scale, 2)

        if keyboard_pressed[pygame.K_1]:
            self.scale += self.scale_value
            self.scale = round(self.scale, 2)
            self.func_coords = self.create_func()

        if keyboard_pressed[pygame.K_2]:
            if self.scale - self.scale_value >= self.scale_value:
                self.scale -= self.scale_value
                self.scale = round(self.scale, 2)
                self.func_coords = self.create_func()

        # pos = self.coordinates_changer(*mouse_pos)
        # if keys[0]:
        #     camera_center_x -= (camera_center_x - pos[0]) / 2
        #     camera_center_y -= (camera_center_y - pos[1]) / 2
        pos = mouse_pos
        if self.is_mouse_on_widget(pos):
            if self.width < pos[0] >= self.x + self.width - self.border_for_camera_moving_x:
                self.camera_center_x += self.camera_speed
                self.func_coords = self.create_func()

            elif self.x < pos[0] <= self.x + self.border_for_camera_moving_x:
                self.camera_center_x -= self.camera_speed
                self.func_coords = self.create_func()

            if self.y + self.height - self.border_for_camera_moving_y < pos[1] <= self.y + self.height:
                self.camera_center_y -= self.camera_speed
                self.func_coords = self.create_func()

            elif self.y < pos[1] <= self.y + self.border_for_camera_moving_y:
                self.camera_center_y += self.camera_speed
                self.func_coords = self.create_func()

    def create_func(self):
        func_coords = []
        x = self.x
        way = 1
        # for sinusoida

        frequency = 10
        high_coof = 10

        # for line func

        k = 1
        b = 0
        while self.coordinates_changer(x, 0)[0] <= self.coordinates_changer(self.x + self.width, 0)[0]:
            x2 = self.coordinates_changer(x, 0)[0]
            # sinusoida
            y = math.cos(frequency * math.radians(x2)) * high_coof

            # parabola
            # y = x2**2

            # line func
            # y = k*x2+b

            # hyperbola
            # if x2 !=0:
            #     y = 1/x2

            # something
            # if x2 != 0 and -100 < x2 < 1000:
            #     # y = 5*x2-x2**2+1/x2
            #     y = math.sin((1 / x2)) ** x2
            #
            func_coords.append((x2, y))
            x += way
        return func_coords

    def draw_func(self, screen):
        for i in range(1, len(self.func_coords)):
            scaled_cords = self.coordinates_changer_in_pygame(self.func_coords[i - 1][0], self.func_coords[i - 1][1])
            scaled_cords2 = self.coordinates_changer_in_pygame(self.func_coords[i][0], self.func_coords[i][1])
            if type(scaled_cords[0]) == float and type(scaled_cords[1]) == float and type(
                    scaled_cords2[0]) == float and type(scaled_cords2[1]) == float:
                pygame.draw.line(screen, (255, 0, 0), (scaled_cords[0], scaled_cords[1]),
                                 (scaled_cords2[0], scaled_cords2[1]), 5)

    def draw_image(self, screen):
        # a =  my_image.size(0)
        begin_point_x = self.coordinates_changer_in_pygame(-self.my_image.size[0] // 2, 0)[0]
        begin_point_y = self.coordinates_changer_in_pygame(0, self.my_image.size[1] // 2)[1]
        res = self.coordinates_changer_in_pygame(1, 1)
        res2 = self.coordinates_changer_in_pygame(0, 0)
        len_x = res[0] - res2[0]
        len_y = res2[1] - res[1]
        for y in range(len(self.my_pixels_array)):
            for x in range(len(self.my_pixels_array[0])):
                # a=coordinates_chaneg_in_pygame(begin_point_x + x, 0)[0]
                # b=coordinates_chaneg_in_pygame(0, begin_point_y + y)[1]
                pygame.draw.rect(screen, (self.my_pixels_array[y][x]), (begin_point_x + x * len_x,
                                                                        begin_point_y + y * len_y,
                                                                        len_x, len_y))
