import os as s
from subprocess import call

test = s.system("cd darknet/ \n ls \n ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg -out /Users/evanday/Capstone/Drone/Encrypted-GoPro-Companion-master/FinalImages/test")
print(test)
#./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg -out test.jpg
#call(["cd", "darknet/","./darknet", "detect", "cfg/yolov3.cfg", "yolov3.weights", "data/dog.jpg", "-out", "test.jpg"])

