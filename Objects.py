import pygame
import Consts
import Screen
num = 0
object1 = Consts.sustainable_list[num]
object2 = Consts.unsustainable_list[num]
def place_objects(object1_cords_tuple,object2_cords_tuple, object1, object2):
    object1_img = pygame.image.load("png_files/"+object1+".png")
    object1_img = pygame.transform.scale(object1_img, Consts.objects_size)
    Screen.screen.blit(object1_img, object1_cords_tuple)

    object2_img = pygame.image.load("png_files/" + object2 + ".png")
    object2_img = pygame.transform.scale(object2_img, Consts.objects_size)
    Screen.screen.blit(object2_img, object2_cords_tuple)
