import random
screen_size = (500,650)
background_color = (255,255,255)
objects_size = (100,100)
running = True
transparent = (0, 0, 0, 0)
PLAYER_WIDTH = 55
PLAYER_HEIGHT = 60
VEL = 200
y_location = 0
counter = 0
bad_points = 5
good_points = 0
list_info = ['Around 27,000 trees are cut down each day ', 'Humans use only 1% of all available water',
             ' 78% of marine mammals are at risk of choking on plastic', 'Americans throw away 25 trillion Styrofoam cups every year',
             'On average, one supermarket goes through 60 million paper bags each year!']

FONT_NAME = "Calibri"

START_MESSAGE = list_info[random.randint(0,3)]
START_FONT_SIZE = int(27)
START_COLOR = (0, 0, 0)
START_LOCATION = (0,15)

j = 0
unsustainable_list = ['fast_fashion','meat','plastic_straw','trash_bin']
sustainable_list = ['sustainable_fashion','vegan','reusable_cup','recycle_trash_bin']
right_object_x = 100
left_object_x = 300