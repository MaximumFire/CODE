import os
from time import sleep as s

cmd = "youtube-dl " + '"' + input("Enter a youtube url: ") + '"'

os.system(cmd)