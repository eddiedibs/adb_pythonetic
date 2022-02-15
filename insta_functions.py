#!/home/edd1e/Desktop/stuff/studies/Programming/python_projects/insta_bot/instabot_env/bin/python3.8

from gettext import install
import platform
import os
import subprocess
from tkinter import E
import settings as s
import time
import cv
from img_functions import img_text_detection


class main_functions:

    def __init__(self) -> None:
        pass

    @classmethod
    def open_app(cls):
        try:
            process = subprocess.run(s.start_command, shell=True)

           
        except KeyboardInterrupt as ex:
            print(ex)
            quit()


    @classmethod
    def list_adb_app_activities(cls):
        try:
            process = subprocess.run(s.list_app_activities, stdout=subprocess.PIPE, shell=True)
            std = process.stdout.decode()
            print(f"{s.green}[INFO]{s.re1} instagram app activities are:\n\n\n {std}")


        
        except KeyboardInterrupt as ex:
            print(ex)
            quit()





    @classmethod
    def get_post_screencap(cls, count:int=0, purpose:str=''):
        try:
            post = f'post_{count}.png'
            print(s.taking_screencap_msg)
            if purpose == s.post_cap:
                process = subprocess.run(f'{s.take_post_screencap}{post}', stdout=subprocess.PIPE, shell=True)
                time.sleep(.5)

            elif purpose == s.analytics_cap:
                process = subprocess.run(f'{s.take_analytics_screencap}{post}', stdout=subprocess.PIPE, shell=True)
                time.sleep(.5)


        except KeyboardInterrupt as ex:
            print(ex)
            quit()



    @classmethod
    def enter_post(cls, count:int):
        try:
            ## first it enters the post
            print(s.entering_post_msg)
            
            process = subprocess.run(f'{s.tap_phone}{s.posts_x_coordinates[count]}{s.first_row_Y_coordinates}', stdout=subprocess.PIPE, shell=True)
            time.sleep(.5)
            ## Then takes a screencap
            main_functions.get_post_screencap(count, s.post_cap)
            post = f'post_{count}.png'
            ## Then it analizes if the 'View insights' button is present
            insight_btn = img_text_detection.img_analize(img_name=post, type='post')
            
            ## Then if it is indeed present, it will press it
            if insight_btn == True:
                print(s.view_insights_msg)
                print(s.entering_post_analytics_msg)
                process = subprocess.run(f'{s.tap_phone}{s.v_insights_btn_coordinates}', stdout=subprocess.PIPE, shell=True)
                time.sleep(2)
                
                ## Once it presses it, it will take a screencap
                main_functions.get_post_screencap(count, s.analytics_cap)
                print(s.exiting_post_analytics_msg)
                ## And then go back
                process = subprocess.run(f'{s.keycode_back}', stdout=subprocess.PIPE, shell=True)
                time.sleep(.5)



            else:
                print(s.view_not_insights_msg)



            print(s.exiting_post_msg)

            process = subprocess.run(s.keycode_back, stdout=subprocess.PIPE, shell=True)
            time.sleep(.5)
           


        except KeyboardInterrupt as ex:
            print(ex)
            quit()




    @classmethod
    def start_app(cls):
        try:

            ## First we initialize the app by going to the home screen
            print(s.initializing_msg)
            process = subprocess.run(s.go_home, stdout=subprocess.PIPE, shell=True)
            time.sleep(.5)


            ## Then we fire up instagram
            print(s.entering_instagram_msg)
            process = subprocess.run(s.enter_app_command, stdout=subprocess.PIPE, shell=True)
            time.sleep(.5)


            ## Then we enter the profile
            print(s.entering_profile_msg)
            tap_on_profile = f"{s.tap_phone}{s.profile_btn_coordinates}"
            swipe_down_action = f"{s.swipe_down}"
            swipe_up_action = f"{s.swipe_up}"
            process = subprocess.run(tap_on_profile, stdout=subprocess.PIPE, shell=True)
            time.sleep(.5)

            ##We first swipe up
            process = subprocess.run(swipe_up_action, stdout=subprocess.PIPE, shell=True)
            time.sleep(1)


            ## then we swipe down a little
            process = subprocess.run(swipe_down_action, stdout=subprocess.PIPE, shell=True)
            time.sleep(.5)


            ##And then we take a screencapture for relocation (To know later if we are where we want to be)
            main_functions.get_post_screencap(0, s.relocation_cap)
            time.sleep(.5)


            row_count = [0, 1, 2]
            for c in row_count: 

                print(c)
                main_functions.enter_post(c)
                # if c == 2:


            
        except KeyboardInterrupt as ex:
            print(ex)
            quit()


if __name__ == '__main__':
    main_functions.start_app()