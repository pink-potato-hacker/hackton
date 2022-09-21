import Consts
import Screen
import pygame
import Player
import Objects


def main():
    pygame.init()
    objects_y = 0
    Consts.running = True
    clock = pygame.time.Clock()
    x_location_tuple = Objects.random_x_location()
    object1_x = x_location_tuple[0]
    object2_x = x_location_tuple[1]
    while Consts.running:
        Screen.win(Consts.good_points)
        Screen.lose(Consts.bad_points)
        Screen.draw_to_screen()
        Objects.object1 = Consts.sustainable_list[Objects.num]
        Objects.object2 = Consts.unsustainable_list[Objects.num]
        object1_cords_tuple = (object1_x, objects_y)
        object2_cords_tuple = (object2_x, objects_y)
        Objects.place_objects(object1_cords_tuple,object2_cords_tuple, Objects.object1, Objects.object2)
        objects_y += 10
        pygame.display.update()
        # Player.meeting_check(objects_y,Objects.object1)
        Player.meeting_check(objects_y,Objects.object2)
        if objects_y == 650:
            Objects.num += 1
            objects_y = 0
            if Objects.num == 4:
                Objects.num = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    count = 0
                    while count <= 300:
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