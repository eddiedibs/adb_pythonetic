#!/home/edd1e/Desktop/stuff/studies/Programming/python_projects/insta_bot/instabot_env/bin/python3.8

import platform
import os
import subprocess
import settings as s


class main_functions:

    def __init__(self) -> None:
        pass

    @classmethod
    def open_app(cls):
        try:
            process = subprocess.run(s.start_command, shell=True)

           
        except KeyboardInterrupt as ex:
            print(ex)

    @classmethod
    def list_adb_app_activities(cls):
        try:
            process = subprocess.run(s.list_app_activities, shell=True)

        
        except KeyboardInterrupt as ex:
            print(ex)










if __name__ == '__main__':
    main_functions.list_adb_app_activities()