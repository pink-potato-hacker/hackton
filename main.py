import Consts
import Screen
import pygame
import Player
import Objects

def main():
    objects_y = 0
    num = 0
    running = True
    clock = pygame.time.Clock()
    while running:
        Screen.win(Consts.good_points)
        Screen.lose(Consts.bad_points)
        Screen.draw_to_screen()
        object1 = Consts.sustainable_list[num]
        object2 = Consts.unsustainable_list[num]
        object1_cords_tuple = (Consts.right_object_x, objects_y)
        object2_cords_tuple = (Consts.left_object_x, objects_y)
        Objects.place_objects(object1_cords_tuple, object2_cords_tuple, object1, object2)
        objects_y += 10
        pygame.display.update()
        if objects_y == 650:
            num += 1
            objects_y = 0
            if num == 4:
                running = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    count = 0
                    while count<= 1000  :
                        Screen.load_instraction()
                        count += 1
                if event.key == pygame.K_RIGHT:
                    Player.right_key()
                elif event.key == pygame.K_LEFT:
                    Player.left_key()
                Consts.counter += 1
            if event.type == pygame.QUIT:
                running = False
    clock.tick(60)
    pygame.quit()



if __name__ == '__main__':
    main()