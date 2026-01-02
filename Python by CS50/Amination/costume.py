import sys
from PIL import Image

images =[]

for arg in sys.argv[1:]:    # [1:] this will not print the name of file
    image = Image.open(arg)
    image.append(image)

images[0].save(
    "costume.gif", save_all = True, append_images=[image[1]], duration = 200, loop = 0
)
