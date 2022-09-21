import random

import pygame
import Consts
import Screen
num = 0
object1 = Consts.sustainable_list[num]
object2 = Consts.unsustainable_list[num]

def random_x_location():
    random_num = random.randint(0,1)
    x_locations = [Consts.right_object_x,Consts.left_object_x]
    object1_x = x_locations[random_num]
    x_locations.remove(object1_x)
    object2_x = x_locations[0]
    return object1_x,object2_x


def place_objects(object1_cords_tuple,object2_cords_tuple, object1, object2):
    object1_img = pygame.image.load("png_files/"+object1+".png")
    object1_img = pygame.transform.scale(object1_img, Consts.objects_size)
    Screen.screen.blit(object1_img, object1_cords_tuple)

    object2_img = pygame.image.load("png_files/" + object2 + ".png")
    object2_img = pygame.transform.scale(object2_img, Consts.objects_size)
    Screen.screen.blit(object2_img, object2_cords_tuple)