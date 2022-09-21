import pygame
import Consts
import Screen

object1 = pygame.Rect(240, 0, 4,4)
object1 = pygame.Rect(260, 0, 4,4)
def moving_object(object1, object2):
    object1.y += 10
    object2.y += 10
    pygame.display.update()

def place_objects(cords_tuple, png_couple):
    unsustainable_object = png_couple[0]
    unsustainable_img = pygame.image.load("png files/"+unsustainable_object+".png")
    unsustainable_img = pygame.transform.scale(unsustainable_img, Consts.objects_size)
    Screen.screen.blit(unsustainable_img, cords_tuple)

    sustainable_object = png_couple[1]
    sustainable_img = pygame.image.load("png files/" + sustainable_object + ".png")
    sustainable_img = pygame.transform.scale(sustainable_img, Consts.objects_size)
    Screen.screen.blit(sustainable_img, cords_tuple)
