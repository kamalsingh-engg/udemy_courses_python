"""
an example to use system python module to use
"""

import time
import os

while True:
    if os.path.exists("veg.txt"):
        with open("veg.text") as myfile:
            print(myfile.read())

    else:
        print("file does not exists")
    time.sleep(4)

