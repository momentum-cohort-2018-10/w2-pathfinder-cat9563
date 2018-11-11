import PIL
import random
from PIL import ImageColor
from PIL import Image



with open("elevation_small.txt", 'r') as f:
   all_elvations = [line.strip('\n').split() for line in f]


elevation_list = [[int(elevation ) for elevation in row] for row in all_elvations]

big_max = max([max(elevation) for elevation in elevation_list])
little_min = min([min(elevation) for elevation in elevation_list])

def find_max(list):
    list = elevation_list
    big_max = max([max(elevation) for elevation in elevation_list])
    return(big_max)

def find_min(list):
    list = elevation_list
    little_min = min([min(elevation) for elevation in elevation_list])
    return(little_min)

conv_to_rgb_values = [[int((elevation - little_min)/(big_max - little_min) * 255) for elevation in row] for row in elevation_list]


# def convert_to_rgb(list1,list2):
#     list1 = find_max
#     list2 = find_min
#     conv_to_rgb_values = [[int((elevation - find_min)/(find_max - find_min) * 255) 
#                             for elevation in row] for row in elevation_list]
#     return(conv_to_rgb_values)

def display_map(list):
    list = conv_to_rgb_values
    im = Image.new("RGB", (600, 600))
    for y, row in enumerate(conv_to_rgb_values):
        for x, value, in enumerate(row):
            im.putpixel((x, y), (value, value, value))
    im.save('hmm.png')
    im.show('hmm.png')

print(display_map(list))


# elvation/max elevation * 255 turn that into an integer

# print(big_max)
# print(little_min)
#print(elevation_list)