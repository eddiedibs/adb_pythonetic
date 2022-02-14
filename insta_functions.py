#!/home/edd1e/Desktop/stuff/studies/Programming/python_projects/insta_bot/instabot_env/bin/python3.8

import platform
import os
import subprocess
import settings as s
import time
import cv


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
            print(f"{s.yellow}[TAKING SCREENCAP]{s.re1}\n")
            if purpose == s.post_cap:
                process = subprocess.run(f'{s.take_post_screencap}{post}', stdout=subprocess.PIPE, shell=True)
                time.sleep(.5)

            elif purpose == s.relocation_cap:
                process = subprocess.run(f'{s.take_relo_screencap}{post}', stdout=subprocess.PIPE, shell=True)
                time.sleep(.5)

        except KeyboardInterrupt as ex:
            print(ex)
            quit()



    @classmethod
    def enter_post(cls, count:int):
        try:
            print(f"{s.green}[ENTERING POST]...{s.re1}\n")
            
            process = subprocess.run(f'{s.enter_post}{s.posts_x_coordinates[count]}{s.first_row_Y_coordinates}', stdout=subprocess.PIPE, shell=True)
            main_functions.get_post_screencap(count, s.post_cap)
            time.sleep(.5)
            print(f"{s.green}[EXITING FIRST POST]...{s.re1}\n")

            process = subprocess.run(s.keycode_back, stdout=subprocess.PIPE, shell=True)
            time.sleep(.5)
           


        except KeyboardInterrupt as ex:
            print(ex)
            quit()




    @classmethod
    def start_app(cls):
        try:

            print(f"{s.green}[INITIALIZING]...{s.re1}\n")
            process = subprocess.run(s.go_home, stdout=subprocess.PIPE, shell=True)
            time.sleep(.5)

            print(f"{s.green}[ENTERING INSTAGRAM APP]...{s.re1}\n")
            process = subprocess.run(s.enter_app_command, stdout=subprocess.PIPE, shell=True)
            time.sleep(.5)



            print(f"{s.green}[ENTERING PROFILE]...{s.re1}\n")
            process = subprocess.run(s.tap_on_profile, stdout=subprocess.PIPE, shell=True)
            time.sleep(.5)

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