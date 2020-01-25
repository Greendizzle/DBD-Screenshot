import numpy as np
from PIL import ImageGrab
import cv2
import time
import datetime
import os
timelapse_img_dir = "images/"
length = 900
sec_between = 30
if not os.path.exists(timelapse_img_dir):
    os.mkdir(timelapse_img_dir)

now = datetime.datetime.now()
finish_time = now + datetime.timedelta(seconds=length)

i = 0

while datetime.datetime.now() < finish_time:
    x = 93
    y = 933
    offx = 80
    offy = 70
    filename = f"{timelapse_img_dir}/{i}.jpg"
    i += 1

    img = ImageGrab.grab(bbox=(x, y, x+offx, y + offy))
    img_numpy = np.array(img.getdata(),dtype='uint8') \
        .reshape((img.size[1],img.size[0],3))
    frame = cv2.cvtColor(img_numpy, cv2.COLOR_BGR2RGB)
    cv2.imshow('window',frame)
    cv2.imwrite(filename, frame)
    time.sleep(sec_between)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break