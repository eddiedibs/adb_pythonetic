#!/home/edd1e/Desktop/stuff/studies/Programming/python_projects/insta_bot/instabot_env/bin/python3.8

from tkinter import E
import pytesseract 
from PIL import Image
import settings as s



class img_text_detection:

    def __init__(self) -> None:
        pass



    @classmethod
    def handle_post_img(cls, img_name):
        try:
                
            img = Image.open(f'{s.screen_post_path}{img_name}')

            width, height = img.size
            
            # # Setting the points for cropped image
            left = 1
            top = height / 2
            right = 500
            bottom = 6 * height / 6
            # # Cropped image of above dimension
            # # (It will not change original image)
            im1 = img.crop((left, top, right, bottom))
            newsize = (500, 500)
            im1 = im1.resize(newsize)
            # Shows the image in image viewer
            # im1.show()
            
            text = pytesseract.image_to_string(im1, config=s.OCR_config)

            curated_text = []

            text_final = text.split('\n')
            for t in text_final:
                text_final2 = t.split()
                for t2 in text_final2:
                    curated_text.append(t2)

            for t in curated_text:
                if t == 'View' or t == 'Insights':
                    return True


        except Exception as ex:
            print(ex)



    @classmethod
    def handle_analytics_img(cls, img_name):
        try:
            
            img = Image.open(f'{s.screen_post_path}{img_name}')

            width, height = img.size
            
            # # Setting the points for cropped image
            left = 2
            top = height / 2
            right = 1000
            bottom = 5 * height / 6
            # # Cropped image of above dimension
            # # (It will not change original image)
            im1 = img.crop((left, top, right, bottom))
            newsize = (800, 500)
            im1 = im1.resize(newsize)
            # Shows the image in image viewer
            # im1.show()

            text = pytesseract.image_to_string(im1)

            curated_text = []

            # text_final = text.split('\n')
            # for t in text_final:
            #     text_final2 = t.split()
            #     for t2 in text_final2:
            #         curated_text.append(t2)

            # for t in curated_text:
            #     if t == 'View' or t == 'Insights':
            #         return True



        except Exception as ex:
            print(ex)





    @classmethod
    def img_analize(cls, img_name, type):
        try:

            if type == 'post':
                post_img = img_text_detection.handle_post_img(img_name)
                if post_img == True:
                    return True
                else:
                    return False

            elif type == 'analytics':
                analytics_img = img_text_detection.handle_analytics_img(img_name)
                if analytics_img == True:
                    return True
                else:
                    return False
        except KeyboardInterrupt as ex:
            print(ex)




if __name__ == '__main__':
    img_text_detection.img_analize('post_2.png', type='post')



