#!/home/edd1e/Desktop/stuff/studies/Programming/python_projects/insta_bot/instabot_env/bin/python3.8

import pytesseract 
from PIL import Image
import settings as s


img = Image.open(f'{s.screen_post_path}post_1.png')

width, height = img.size
 
# Setting the points for cropped image
left = 2
top = height / 2
right = 500
bottom = 6 * height / 9
# Cropped image of above dimension
# (It will not change original image)
im1 = img.crop((left, top, right, bottom))
newsize = (500, 500)
im1 = im1.resize(newsize)
# Shows the image in image viewer
# im1.show()

text = pytesseract.image_to_string(im1)

text_final = text.split('\n')

tex = []

for t in text_final:
    if t == 'View Insights':
        tex.append(t)


print(tex[0])










