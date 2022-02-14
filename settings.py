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
tap_on_profile = 'adb shell input tap 995 2209'
keycode_back = 'adb shell input keyevent KEYCODE_BACK'
enter_post = 'adb shell input tap '
take_post_screencap = f'adb exec-out screencap -p > {screen_post_path}'
take_relo_screencap = f'adb exec-out screencap -p > {screen_relo_path}'


#### screencap Purpose args  ####

post_cap = 'post_cap'
relocation_cap = 'relocation_cap'



### COORDINATE PARAMS ###

first_post_X_coordinates = '180 '
second_post_X_coordinates = '379 '
third_post_X_coordinates = '752 '

posts_x_coordinates = [first_post_X_coordinates, second_post_X_coordinates, third_post_X_coordinates]

first_row_Y_coordinates = ' 1783'






settings_file = __file__





















