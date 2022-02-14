from colorama import Style as Style2

################################################

               #SETTINGS FILE

################################################





## Colors and Prompt
green = "\033[32;1m"
red = "\033[31;1m"
re1 = Style2.RESET_ALL
prompt_arrow = 'profkit>>'



#### COMMANDS ####

#PROMPT COMMANDS
ig_start = 'start'


#INTERNAL COMMANDS
start_command = 'adb shell am start -n com.instagram.android/.activity.MainTabActivity'
enter_app_command = 'adb shell am start -n com.instagram.android/.activity.MainTabActivity'
list_app_activities = "adb shell dumpsys package | grep -Eo '^[[:space:]]+[0-9a-f]+[[:space:]]+com.instagram.android/[^[:space:]]+' | grep -oE '[^[:space:]]+$'"








settings_file = __file__





















