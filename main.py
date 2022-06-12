import pygame
pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

scale = 10
scale_value = 1

# camera_x_normal, camera_y_normal = 0,0
# camera_x_changed, camera_y_changed = -screen_width//2,screen_height//2
# camera_x_changed_original, camera_y_changed_original =camera_x_changed, camera_y_changed
camera_center_x = 0
camera_center_y = 0
process_running = True

objects = []

normal_picture_size = 500

def coordinates_changer(x,y):
    # return (camera_center_x,camera_center_y)
    # global camera_center_y, camera_center_x
    return(camera_center_x-(screen_width//2-x),camera_center_y-(screen_height//2-y))
def coordinates_changer2(x,y):
    return(camera_center_x+x,camera_center_y+y)

class Object():
    def __init__(self, x,y):
        self.x,self.y = coordinates_changer(x,y)
        self.x_for_draw,self.y_for_draw = x,y
        self.image= pygame.image.load("planet.png")
        self.image = pygame.transform.scale(self.image,(normal_picture_size/scale,normal_picture_size/scale))

def scaling():
    global scale, objects, camera_y_changed,camera_x_changed
    for object in objects:
        object.image = pygame.image.load("planet.png")
        object.image = pygame.transform.scale(object.image, (normal_picture_size / scale, normal_picture_size / scale))

    # camera_x_changed = camera_x_changed_original/scale
    # camera_y_changed = camera_y_changed_original/scale

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button== 1:
                print(camera_center_x,camera_center_y)
                # pos = pygame.mouse.get_pos()
                # new_object = Object(pos[0],pos[1])
                # objects.append(new_object)
    keys = pygame.mouse.get_pressed()
    pos = coordinates_changer(*pygame.mouse.get_pos())
    if keys[0]:
        # camera_x_changed = camera_x_changed +(camera_x_changed- coordinates_changer(pos[0],0)[0])
        # camera_y_changed = camera_y_changed +(camera_y_changed-coordinates_changer(0,pos[1])[1])
        camera_center_x = camera_center_x+(camera_center_x-pos[0])
        camera_center_y = camera_center_y+(camera_center_y-pos[1])


def test_camera_draw():
    # pygame.draw.line(screen, (0,255,0), (0,screen_height//2),(screen_width,screen_height//2))
    # pygame.draw.line(screen, (0,255,0), (screen_width//2,0),(screen_width//2,screen_height))
    # plank = (screen_width // 2) / scale
    # # print(plank)
    # for i in range(1,int(scale)+1):
    #     pygame.draw.line(screen, (0, 255, 0), (((screen_width//2)-(screen_width//scale*i),0)[0], screen_height//2-5), (((screen_width//2)-(screen_width//scale*i),0)[0],  screen_height//2+5))
    # for i in range(1,int(scale)+1):
    #     pygame.draw.line(screen, (0, 255, 0), (((screen_width//2)+(screen_width//scale*i),0)[0], screen_height//2-5), (((screen_width//2)+(screen_width//scale*i),0)[0],  screen_height//2+5))
    for i in range(0,screen_width//2,scale):
        now_pos =coordinates_changer(i,0)
        print(scale)
        pygame.draw.line(screen,(0,255,0),(coordinates_changer2(i,0)[0],0),(coordinates_changer2(i,0)[0],screen_height))
    for i in range(0,screen_height//2,scale):
        now_pos =coordinates_changer(0,i)
        pygame.draw.line(screen,(0,255,0),(0,coordinates_changer2(0,i)[1]),(screen_width,coordinates_changer2(0,i)[1]))
    # for i in range(screen_width//2):
    #     now_pos = coordinates_changer(i, 0)
    #
def drawing(sprites):
    screen.fill((0, 0, 0))
    test_camera_draw()
    for sprite in sprites:
        # print(coordinates_changer(sprite.x, sprite.y))

        screen.blit(sprite.image, (sprite.x_for_draw, sprite.y_for_draw))

    pygame.display.update()
def mainloop():
    while process_running:
        events_check()
        pygame.time.delay(20)
        drawing(objects)


if __name__ == '__main__':
    mainloop()