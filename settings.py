from colorama import Style as Style2

################################################

               #SETTINGS FILE

################################################





## Colors and Prompt
green = "\033[32;1m"
red = "\033[31;1m"
yellow = "\033[1;33m"
re1 = Style2.RESET_ALL
prompt_arrow = 'profkit>>'


#### PATHS #####

screen_post_path = './resources/screencaps/posts/'
screen_relo_path = './resources/screencaps/relocation/'
screen_analytics_path = './resources/screencaps/analytics/'



#### COMMANDS ####

#PROMPT COMMANDS
ig_start = 'start'


#INTERNAL COMMANDS
start_command = 'adb shell am start -n com.instagram.android/.activity.MainTabActivity'
go_home = 'adb shell input keyevent 3'
enter_app_command = 'adb shell am start -n com.instagram.android/.activity.MainTabActivity'
list_apps = 'adb shell pm list packages -3'
list_app_activities = "adb shell dumpsys package | grep -Eo '^[[:space:]]+[0-9a-f]+[[:space:]]+com.instagram.android/[^[:space:]]+' | grep -oE '[^[:space:]]+$'"
swipe_left = 'adb shell input touchscreen swipe 0001 0140 -500 500 100'
swipe_right = 'adb shell input touchscreen swipe 0001 0140 500 500 100'
swipe_down = 'adb shell input touchscreen swipe 500 1919 500 1300 200'
swipe_up = 'adb shell input touchscreen swipe 500 721 500 1919 200'
keycode_back = 'adb shell input keyevent KEYCODE_BACK'
tap_phone = 'adb shell input tap '
take_post_screencap = f'adb exec-out screencap -p > {screen_post_path}'
take_relo_screencap = f'adb exec-out screencap -p > {screen_relo_path}'
take_analytics_screencap = f'adb exec-out screencap -p > {screen_analytics_path}'



#### screencap Purpose args  ####

post_cap = 'post_cap'
analytics_cap = 'analytics_cap'
relocation_cap = 'relocation_cap'



### COORDINATE PARAMS ###

first_post_X_coordinates = '180 '
second_post_X_coordinates = '379 '
third_post_X_coordinates = '752 '

posts_x_coordinates = [first_post_X_coordinates, second_post_X_coordinates, third_post_X_coordinates]

first_row_Y_coordinates = ' 583'

profile_btn_coordinates = '995 2209'

v_insights_btn_coordinates = '191 1569'


#### TERMINAL MESSAGES ####

initializing_msg = f"{green}[INITIALIZING]...{re1}\n"
entering_instagram_msg = f"{green}[ENTERING INSTAGRAM APP]...{re1}\n"
entering_profile_msg = f"{green}[ENTERING PROFILE]...{re1}\n"

view_insights_msg = f"[VIEW INSIGHTS BUTTON {yellow}IS PRESENT{re1}]...{re1}\n"
view_not_insights_msg = f"[VIEW INSIGHTS BUTTON IS {red}NOT{re1} PRESENT]...{re1}\n"



entering_post_msg = f"{green}[ENTERING POST]...{re1}\n"
exiting_post_msg = f"{green}[EXITING POST]...{re1}\n"

entering_post_analytics_msg = f"{green}[ENTERING POST {re1}{yellow}ANALYTICS{re1}{green}]...{re1}\n"
exiting_post_analytics_msg = f"{green}[EXITING POST {re1}{yellow}ANALYTICS{re1}]...\n"

taking_screencap_msg = f"{yellow}[TAKING SCREENCAP]{re1}\n"


####### OCR CONFIG VAR #########

OCR_config = r"--psm 3 --oem 3"


settings_file = __file__





















