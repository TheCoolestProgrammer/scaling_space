import pygame
pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

scale = 100
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
        new_x = camera_center_x+(x-screen_width//2)
    else:
        new_x = camera_center_x - (screen_width//2 - x)
    if y >= screen_height // 2:
        new_y = camera_center_y+(y-screen_height//2)
    else:
        new_y = camera_center_y - (screen_height//2 - y)
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
                scale +=scale_value
                scale = round(scale, 2)
                scaling()
            elif event.key == pygame.K_2:
                scale -=scale_value
                scale = round(scale,2)
                scaling()
    keys = pygame.mouse.get_pressed()
    pos = coordinates_changer(*pygame.mouse.get_pos())
    if keys[0]:
        camera_center_x+= (pos[0] - camera_center_x)//scale
        camera_center_y+= (pos[1] - camera_center_y)//scale
def test_camera_draw():
    # pygame.draw.line(screen, (0,255,0), (0,screen_height//2),(screen_width,screen_height//2))
    # pygame.draw.line(screen, (0,255,0), (screen_width//2,0),(screen_width//2,screen_height))
    # plank = (screen_width // 2) / scale
    # # print(plank)
    # for i in range(1,int(scale)+1):
    #     pygame.draw.line(screen, (0, 255, 0), (((screen_width//2)-(screen_width//scale*i),0)[0], screen_height//2-5), (((screen_width//2)-(screen_width//scale*i),0)[0],  screen_height//2+5))
    # for i in range(1,int(scale)+1):
    #     pygame.draw.line(screen, (0, 255, 0), (((screen_width//2)+(screen_width//scale*i),0)[0], screen_height//2-5), (((screen_width//2)+(screen_width//scale*i),0)[0],  screen_height//2+5))
    # for i in range(-screen_width//2,screen_width//2,scale):
    #     now_pos =coordinates_changer(i,0)
    #     # print(scale)
    #     pygame.draw.line(screen,(0,255,0),(coordinates_changer2(camera_center_x+i,0)[0],0),(coordinates_changer2(camera_center_x+i,0)[0],screen_height))
    # for i in range(0,screen_height//2,scale):
    #     now_pos =coordinates_changer(0,i)
    #     pygame.draw.line(screen,(0,255,0),(0,coordinates_changer2(0,camera_center_y+i)[1]),(screen_width,coordinates_changer2(0,camera_center_y+i)[1]))
    #
    # for i in range(screen_width//2):
    #     now_pos = coordinates_changer(i, 0)
    #
    font = pygame.font.SysFont("Times New Roman", scale//4)

    for x in range(0,screen_width):
        if coordinates_changer(x,0)[0] % scale ==0:
            pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, screen_height), 1)
            surface = font.render(str(coordinates_changer(x, 0)[0] / scale), False, (255, 255, 255))
            screen.blit(surface, (x, 0))
    for y in range(0,screen_height):
        if coordinates_changer(0,y)[1] % scale ==0:
            pygame.draw.line(screen,(0,255,0),(0,y),(screen_width,y),1)
            surface = font.render(str(coordinates_changer(0,y)[1] / scale), False, (255, 255, 255))
            screen.blit(surface, (0,y))
def draw_func():
    for x in range(screen_width):
        x2 =coordinates_changer(x,0)[0]
        y = x2*x2
        pygame.draw.circle(screen,(255,0,0),coordinates_chaneg_in_pygame(x2,y),5)
def drawing(sprites):
    screen.fill((0, 0, 0))
    test_camera_draw()
    draw_func()
    pygame.display.update()
def mainloop():
    while process_running:
        events_check()
        pygame.time.delay(20)
        drawing(objects)


if __name__ == '__main__':
    mainloop()