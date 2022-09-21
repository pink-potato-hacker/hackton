import Consts
import Objects
import Screen
import pygame
import Player

object1_cords_tuple = Consts.right_object_start
object2_cords_tuple = Consts.left_object_start

running = True
while running:
    for event in pygame.event.get(Screen.screen_func()):
        for png_couple in Consts.objects_list:
            Objects.place_objects(object1_cords_tuple,object2_cords_tuple,png_couple)
            objects = Objects.place_objects(object1_cords_tuple,object2_cords_tuple,png_couple)
            object1 = objects[0]
            object2 = objects[1]
            Objects.moving_object(object1,object2)
            pygame.display.flip()
            pygame.display.update()
            break
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Player.right_key()
            if event.key == pygame.K_LEFT:
                Player.left_key()

