import pygame
import math
pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

scale = 10
scale_value = 1

camera_center_x = 0
camera_center_y = 0
process_running = True

objects = []

normal_picture_size = 500



def coordinates_changer(x,y):
    # в координаты поля
    global camera_center_y, camera_center_x
    if x >= screen_width//2:
        new_x = camera_center_x+((x-screen_width//2)/scale)
    else:
        new_x = camera_center_x - ((screen_width//2 - x)/scale)
    if y >= screen_height // 2:
        new_y = camera_center_y+((y-screen_height//2)/scale)
    else:
        new_y = camera_center_y - ((screen_height//2 - y)/scale)
    return(new_x,new_y)

def coordinates_chaneg_in_pygame(x,y):
    global camera_center_y, camera_center_x
    distance_x = camera_center_x - x
    distance_y = camera_center_y - y
    # zero_point_x = camera_center_x-screen_width//2
    # zero_point_y = camera_center_y-screen_height//2
    new_x = (screen_width//2 - distance_x)
    new_y = (screen_height//2 - distance_y)
    return(new_x,new_y)
class Object():
    def __init__(self, x,y):
        self.x,self.y = coordinates_changer(x,y)
        # self.x_for_draw,self.y_for_draw = x,y
        self.image= pygame.image.load("planet.png")
        self.image = pygame.transform.scale(self.image,(normal_picture_size/scale,normal_picture_size/scale))

def scaling():
    global scale, objects, camera_y_changed,camera_x_changed
    for object in objects:
        object.image = pygame.image.load("planet.png")
        object.image = pygame.transform.scale(object.image, (normal_picture_size *(scale/100), normal_picture_size *(scale/100)))

def events_check():
    global process_running, scale, scale_value, objects,camera_center_x,camera_center_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                process_running = False
            elif event.key == pygame.K_1:
                if scale >= scale_value and scale_value < 1:
                    scale_value = scale_value * 10
                scale +=scale_value
                if scale > 1.1:
                    scale = round(scale)

                # scale = round(scale, 2)
                scaling()
            elif event.key == pygame.K_2:
                if scale <= scale_value:
                    scale_value = scale_value / 10
                scale -=scale_value
                if scale > 1.1:
                    scale = round(scale)

                # scale = round(scale,2)
                scaling()
    keys = pygame.mouse.get_pressed()
    keys2= pygame.key.get_pressed()
    pos = coordinates_changer(*pygame.mouse.get_pos())
    if keys[0]:
        camera_center_x+= (pos[0] - camera_center_x)/scale
        camera_center_y+= (pos[1] - camera_center_y)/scale
    if keys2[pygame.K_1]:
        if scale >= scale_value and scale_value < 1:
            scale_value = scale_value* 10
        scale += scale_value
        if scale >1.1:
            scale = round(scale)
        scaling()
    if keys2[pygame.K_2]:
        if scale <= scale_value:
            scale_value = scale_value /10
        scale -= scale_value
        if scale > 1.1:
            scale = round(scale)
        # scale = round(scale, 2)
        scaling()
def test_camera_draw():
    font = pygame.font.SysFont("Times New Roman", int(scale))

    for x in range(0,screen_width):
        if int(scale)>0 and coordinates_changer(x,0)[0] % int(scale) ==0:
            pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, screen_height), 1)
            surface = font.render(str(coordinates_changer(x, 0)[0] / scale), False, (255, 255, 255))
            screen.blit(surface, (x, 0))
    for y in range(0,screen_height):
        if int(scale)>0 and coordinates_changer(0,y)[1] % int(scale) ==0:
            pygame.draw.line(screen,(0,255,0),(0,y),(screen_width,y),1)
            surface = font.render(str(coordinates_changer(0,y)[1] / scale), False, (255, 255, 255))
            screen.blit(surface, (0,y))
def create_func():
    func_coords=[]
    x = -screen_width//2
    way = 1
    frequency=10
    high_coof = 50
    while coordinates_changer(x,0)[0] < coordinates_changer(screen_width,0)[0]:
        # sinusoida
        y = math.cos(frequency*math.radians(x))*high_coof
        #parabola
        # y = x**2
        y = y*-1
        # x2 = x
        # if 0<=coordinates_chaneg_in_pygame(0,y)[1] < screen_height:
        new_cords=coordinates_chaneg_in_pygame(x*scale,y)
        func_coords.append(new_cords)
        x+=way
    return func_coords
def draw_func():
    func_coords = create_func()
    # k = 1/scale
    for i in range(1,len(func_coords)):
        # pygame.draw.circle(screen,(255,0,0),(i[0],i[1]),scale//50)
        pygame.draw.line(screen,(255,0,0),(func_coords[i-1][0],func_coords[i-1][1]),(func_coords[i][0], func_coords[i][1]),2)
def drawing():
    screen.fill((0, 0, 0))
    test_camera_draw()
    draw_func()
    pygame.display.update()
def mainloop():
    # func_coords = create_func()
    while process_running:
        events_check()
        pygame.time.delay(20)
        print(scale_value,scale)
        drawing()


if __name__ == '__main__':
    mainloop()