import PIL
import random
from PIL import ImageColor
from PIL import Image 


# im = Image.new('RGBA', (600, 600), 'forestGreen')
# im.save('map.png')

# did list comprehsion and created a list out of that 
with open("elevation_small.txt", 'r') as f:
    all_elvations = [line.strip('\n').split() for line in f]
    

elevation_list = [[int(elevation ) for elevation in row] for row in all_elvations]


big_max = max([max(elevation) for elevation in elevation_list])
little_min = min([min(elevation) for elevation in elevation_list])

conv_to_rgb_values = [[int((elevation - little_min)/(big_max - little_min) * 255) for elevation in row] for row in elevation_list]





#img = Image.new("RGB",(255,255))
# for y, elevation in enumerate(conv_to_rgb_values):
#   print(elevation)


im = Image.new("RGB", (600, 600))
for y, row in enumerate(conv_to_rgb_values):
    for x, value, in enumerate(row):
        im.putpixel((x, y), (value, value, value))
im.save('hmm.png')
im.show('hmm.png')




# elvation/max elevation * 255 turn that into an integer

# print(big_max)
# print(little_min)
#print(elevation_list)
