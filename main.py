import pygame
import math
pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

scale = 1
scale_value = 1

camera_center_x = 0
camera_center_y = 0
process_running = True

objects = []

normal_picture_size = 500



def coordinates_changer(x,y):
    # в координаты поля
    global camera_center_y, camera_center_x
    # if x >= camera_center_y:
    new_x = camera_center_x+((x-screen_width//2)/scale)
    # else:
    #     new_x =camera_center_x-((screen_width//2 - x))
    # if y >= camera_center_y:
    new_y = camera_center_y-((y-screen_height//2)/scale)
    # # else:
    #     new_y =((screen_height//2 - y))- camera_center_y
    return(new_x,new_y)

def coordinates_chaneg_in_pygame(x,y):
    global camera_center_y, camera_center_x
    # x= x*scale
    # y = y*scale
    distance_x =x- camera_center_x
    distance_y =y- camera_center_y
    distance_x *=scale
    distance_y*=scale
    # zero_point_x = camera_center_x-screen_width//2
    # zero_point_y = camera_center_y-screen_height//2
    new_x = (screen_width//2 + distance_x)
    new_y = (screen_height//2 - distance_y)
    return(new_x,new_y)
class Object():
    def __init__(self, x,y):
        self.x,self.y = coordinates_changer(x,y)
        # self.x_for_draw,self.y_for_draw = x,y
        self.image= pygame.image.load("planet.png")
        self.image = pygame.transform.scale(self.image,(normal_picture_size/scale,normal_picture_size/scale))

def scaling():
    global scale, objects, func_coords
    for object in objects:
        object.image = pygame.image.load("planet.png")
        object.image = pygame.transform.scale(object.image, (normal_picture_size *(scale/100), normal_picture_size *(scale/100)))
    func_coords = create_func()
def events_check():
    global process_running, scale, scale_value, objects,camera_center_x,camera_center_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                process_running = False
            elif event.key == pygame.K_1:
                # if scale >= scale_value and scale_value < 1:
                #     scale_value = scale_value * 10
                scale +=scale_value
                # if scale > 1.1:
                #     scale = round(scale)
                scale=round(scale,2)

                # scale = round(scale, 2)
                scaling()
            elif event.key == pygame.K_2:
                # if scale <= scale_value:
                #     scale_value = scale_value / 10
                scale -=scale_value
                scale=round(scale,2)
                # if scale > 1.1:
                #     scale = round(scale)

                # scale = round(scale,2)
                scaling()
            elif event.key == pygame.K_q:
                camera_center_x=1000000
    keys = pygame.mouse.get_pressed()
    keys2= pygame.key.get_pressed()

    pos = coordinates_changer(*pygame.mouse.get_pos())
    # print(pos)
    # pos = pygame.mouse.get_pos()
    if keys[0]:

        camera_center_x-=(camera_center_x-pos[0])/2
        camera_center_y-=(camera_center_y-pos[1])/2
        # if pos[0]<screen_width//2:
        #     camera_center_x+=speed
        # else:
        #     camera_center_x-=speed

        scaling()

    if keys2[pygame.K_1]:
        # if scale >= scale_value and scale_value < 1:
        #     scale_value = scale_value* 10
        scale += scale_value
        scale = round(scale,2)

        # if scale >1.1:
        #     scale = round(scale)
        scaling()
    if keys2[pygame.K_2]:
        # if scale <= scale_value:
        #     scale_value = scale_value /10
        scale -= scale_value
        scale = round(scale,2)

        # if scale > 1.1:
        #     scale = round(scale)
        # scale = round(scale, 2)
        scaling()
def test_camera_draw():
    font = pygame.font.SysFont("Times New Roman", int(scale)*2)

    # for x in range(0,screen_width):
    #     if round(coordinates_changer(x,0)[0],2) % 5 ==0:
    #         pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, screen_height), 1)
    #         surface = font.render(str(round(coordinates_changer(x, 0)[0],2) ), False, (255, 255, 255))
    #         screen.blit(surface, (x, 0))
    # for y in range(0,screen_height):
    #     if round(coordinates_changer(0,y)[1],2) % 5 ==0:
    #         pygame.draw.line(screen,(0,255,0),(0,y),(screen_width,y),1)
    #         surface = font.render(str(round(-coordinates_changer(0,y)[1],2)), False, (255, 255, 255))
    #         screen.blit(surface, (0,y))
    x =camera_center_x-(camera_center_x%5)
    y =camera_center_y-(camera_center_y%5)
    counter=x
    while counter<=coordinates_changer(screen_width,0)[0]:
        pos = coordinates_chaneg_in_pygame(counter,0)[0]
        pygame.draw.line(screen,(0,255,0),(pos,0),(pos,screen_height),2)
        surface = font.render(str(counter), False, (255, 255, 255))
        screen.blit(surface, (pos,0))
        counter+= 5
    counter = x
    while counter >= coordinates_changer(0, 0)[0]:
        pos = coordinates_chaneg_in_pygame(counter, 0)[0]
        pygame.draw.line(screen, (0, 255, 0), (pos, 0), (pos, screen_height), 2)
        surface = font.render(str(counter), False, (255, 255, 255))
        screen.blit(surface, (pos, 0))
        counter -= 5
    counter = y
    while counter <= coordinates_changer(0, 0)[1]:
        pos = coordinates_chaneg_in_pygame(0,counter)[1]
        pygame.draw.line(screen, (0, 255, 0), (0,pos), (screen_width,pos), 2)
        surface = font.render(str(counter), False, (255, 255, 255))
        screen.blit(surface, (0,pos))
        counter += 5
    counter = y
    while counter >= coordinates_changer(0, screen_height)[1]:
        pos = coordinates_chaneg_in_pygame(0, counter)[1]
        pygame.draw.line(screen, (0, 255, 0), (0, pos), (screen_width, pos), 2)
        surface = font.render(str(counter), False, (255, 255, 255))
        screen.blit(surface, (0,pos))
        counter -= 5


def create_func():
    func_coords=[]
    x=0
    way = 1
    # for sinusoida

    frequency=10
    high_coof = 10

    # for line func

    k = 1
    b=0
    while coordinates_changer(x,0)[0] <= coordinates_changer(screen_width,0)[0]:
        x2 = coordinates_changer(x,0)[0]
        # sinusoida
        # y = math.cos(frequency*math.radians(x2))*high_coof

        #parabola
        # y = x2**2

        # line func
        # y = k*x2+b

        # hyperbola
        # if x2 !=0:
        #     y = 1/x2

        # something
        if x2 !=0:
            y = 5*x2-x2**2+1/x2
            func_coords.append((x2,y))
        x+=way
    return func_coords
def draw_func():
    global func_coords
    for i in range(1,len(func_coords)):
        scaled_cords= coordinates_chaneg_in_pygame(func_coords[i-1][0],func_coords[i-1][1])
        scaled_cords2= coordinates_chaneg_in_pygame(func_coords[i][0],func_coords[i][1])
        pygame.draw.line(screen,(255,0,0),(scaled_cords[0],scaled_cords[1]),(scaled_cords2[0],scaled_cords2[1]),5)
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
        # print(scale_value,scale)
        # pos = coordinates_changer(0,0)
        # print(pos)
        # print(coordinates_chaneg_in_pygame(pos[0],pos[1]))
        # print(camera_center_x)
        # print(scale)
        drawing()


if __name__ == '__main__':
    func_coords = create_func()
    mainloop()