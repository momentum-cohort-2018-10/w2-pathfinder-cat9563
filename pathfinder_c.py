import PIL
import random
from PIL import ImageColor
from PIL import Image 

class Display_map:

    def __selfint__(self, all_elevations, image_name, height, width):
        self.all_elevations = all_elevations
        self.image_name = image_name
        self.height = height 
        self.width = width
        self.map_image = None

    with open("elevation_small.txt", 'r') as f:
        all_elvations = [line.strip('\n').split() for line in f]
    
    elevation_list = [[int(elevation ) for elevation in row] for row in all_elvations]
    big_max = max([max(elevation) for elevation in elevation_list])
    little_min = min([min(elevation) for elevation in elevation_list])
    
    self.all_elevations = [[int((elevation - little_min)/(big_max - little_min) * 255) for elevation in row] for row in elevation_list]


    def print_map(self, list):
        """
        creates a map from elevation data
        """
        self.map_image = Image.new("RGB", (self.height, self.width))
        for y, row in enumerate(list):
            for x, value, in enumerate(row):
                self.map_image.putpixel((x, y), (value, value, value))
        self.map_image.save(self.image_name)


    # im = Image.new("RGB", (600, 600))
    # for y, row in enumerate(conv_to_rgb_values):
    #     for x, value, in enumerate(row):
    #         im.putpixel((x, y), (value, value, value))
    # im.save('hmm.png')
    # im.show('hmm.png')

Display_map.print_map()



# elvation/max elevation * 255 turn that into an integer

# print(big_max)
# print(little_min)
#print(elevation_list)
