import pygame
pygame.init()
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

scale = 5
scale_value = 0.1

camera_x_normal, camera_y_normal = 0,0
camera_x_changed, camera_y_changed = -screen_width//2,screen_height//2
camera_x_changed_original, camera_y_changed_original =camera_x_changed, camera_y_changed
process_running = True

objects = []

normal_picture_size = 500

def coordinates_changer(x,y):
    return (camera_x_changed+x,camera_y_changed-y)

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

    camera_x_changed = camera_x_changed_original/scale
    camera_y_changed = camera_y_changed_original/scale

def events_check():
    global process_running, scale, scale_value, objects
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                process_running = False
            elif event.key == pygame.K_1:
                scale +=scale_value
                scaling()
            elif event.key == pygame.K_2:
                scale -=scale_value
                scaling()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button== 1:
                pos = pygame.mouse.get_pos()
                new_object = Object(pos[0],pos[1])
                objects.append(new_object)



def test_camera_draw():
    pygame.draw.line(screen, (0,255,0), (0,screen_height//2),(screen_width,screen_height//2))
    pygame.draw.line(screen, (0,255,0), (screen_width//2,0),(screen_width//2,screen_height))
    plank = (screen_width // 2) / scale
    print(plank)
    for i in range(1,int(scale)+1):
        pygame.draw.line(screen, (0, 255, 0), (((screen_width//2)-(screen_width//scale*i),0)[0], screen_height//2-5), (((screen_width//2)-(screen_width//scale*i),0)[0],  screen_height//2+5))
    for i in range(1,int(scale)+1):
        pygame.draw.line(screen, (0, 255, 0), (((screen_width//2)+(screen_width//scale*i),0)[0], screen_height//2-5), (((screen_width//2)+(screen_width//scale*i),0)[0],  screen_height//2+5))

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