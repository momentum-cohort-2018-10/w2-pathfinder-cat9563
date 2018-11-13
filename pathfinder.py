import PIL
import random
from PIL import ImageColor
from PIL import Image



with open("elevation_small.txt", 'r') as f:
   all_elvations = [line.strip('\n').split() for line in f]


elevation_list = [[int(elevation ) for elevation in row] for row in all_elvations]

big_max = max([max(elevation) for elevation in elevation_list])
little_min = min([min(elevation) for elevation in elevation_list])
conv_to_rgb_values = [[int((elevation - little_min)/(big_max - little_min) * 255) for elevation in row] for row in elevation_list]

def display_map(list):
    """
    converts data to an image. 
    """
    list = conv_to_rgb_values
    im = Image.new("RGB", (600, 600))
    for y, row in enumerate(conv_to_rgb_values):
        for x, value, in enumerate(row):
            im.putpixel((x, y), (value, value, value))
            im.putpixel((x, 300), (0, 0, 200))
    im.save('map_image.png')
    im.show('map_image.png')

print(display_map(list))

# the next lines put a straight blue line vertically down the middle of the image

# im = map_image.png
# for x, row in enumerate(conv_to_rgb_values):
#     im.putpixel((x, 300), (0, 0, 200))
# im.save("map_veritcal_line.png")
# im.show("map_vertical_line.png")



# for tuple in 'map_image':
#     display_map(conv_to_rgb_values).putpixel((tuple[0], tuple[1]), (255, 0, 0))
# display_map(conv_to_rgb_values).save('map.png')