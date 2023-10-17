import json
import subprocess

#The first backslash in string is being interpreted as a special character. In fact, because it's followed by a "U", it's being interpreted as the start of a Unicode code point.
#possible solution r"C:\Users\DeePak\Desktop\myac.csv" or:
file_path = 'C:/Users/<User>/AppData/Roaming/discord/settings.json'

with open(file_path, "r") as file:
    data = json.load(file)

data["MIN_WIDTH"], data["MIN_HEIGHT"] = 0, 0

with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

#discord autolaunch
application_path = 'C:/Users/<User>/AppData/Local/Discord/app-1.0.9019/Discord.exe'

try:
    # Start the application
    subprocess.Popen(application_path)
    print(f"Started {application_path}")
except Exception as e:
    print(f"An error occurred: {e}")