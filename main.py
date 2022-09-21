import Consts
import Objects
import Screen
import pygame
import Player

object1_cords_tuple = Consts.right_object_start
object2_cords_tuple = Consts.left_object_start

def main():
    y_location = 0
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get(Screen.screen_func()):
            for png_couple in Consts.objects_list:
                objects = Objects.place_objects((100, y_location),(300, y_location),png_couple)
                object1 = objects[0]
                object2 = objects[1]
                y_location+= 10
                pygame.display.update()
                break
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Player.right_key()
                if event.key == pygame.K_LEFT:
                    Player.left_key()
    clock.tick(60)

if __name__ == '__main__':
    main()