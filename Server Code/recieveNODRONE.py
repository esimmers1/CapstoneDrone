import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as pkrsa
from Crypto.Cipher import AES
from moviepy.editor import *
from Splice import splice
import zipfile
import os
import glob
import time
import requests

servername = "http://10.25.10.91:63654"
timestamp = str(int(time.time()))
#video_location = "videos/" + timestamp
video_location = "FieldTest3"
ask_for_ip = False
#ask_for_ip = False
verbose = True

if(ask_for_ip):
    servername = "http://" + input("Enter IP and port (eg, 1.1.1.1:1234): ")

def clean_folder(foldername):
    if verbose:
        print("Clearing directory " + foldername)
    try:
        foldername += "/*" if foldername[-1] != '/' else '*'
        [os.remove(file) for file in glob.glob(foldername, recursive=True)]
    except Exception:
        print("Nothing to remove.")

def decrypt_rsa(data):
    key = RSA.import_key(open("privatekey.pem").read())
    cipher = pkrsa.new(key)
    return cipher.decrypt(data)

def download_and_decrypt(url_with_port):
    # init vars, make folder to store videos in based on timestamp
    url = url_with_port + "/num_files.txt"
    r = requests.get(url, allow_redirects=True)
    os.mkdir(video_location)
    num_files = int(r.content)

    for i in range(num_files):
        if verbose:
            print(f"\nDownloading file {str(i+1)}/{str(num_files)}")
        # get key and video file as variables
        key_url = url_with_port + "/keys/" + str(i+1) + ".asc"
        vid_url = url_with_port + "/videos/encrypted/" + str(i+1) + ".mpc"
        key_data = requests.get(key_url, allow_redirects=True).content
        vid_data = requests.get(vid_url, allow_redirects=True).content
        
        # hack to allow vid_data to be subscriptable
        with open("tempfile.mpc", "wb+") as tempfile:
            tempfile.write(vid_data)
        vid_data = open("tempfile.mpc", "rb")
        os.remove("tempfile.mpc")

        # decrypt key and data in turn
        if verbose:
            print(f" Decrypting file {str(i+1)}/{str(num_files)}")
        nonce, tag, ciphertext = [vid_data.read(x) for x in (16, 16, -1)]
        cipher = AES.new(decrypt_rsa(key_data), AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)

        # write data to file
        with open(video_location + "/" + str(i+1) + ".mp4", "wb+") as f:
            f.write(data)

def ImageDetection(foldername):
    count = os.listdir(foldername)
    i = 0

    while(i < len(count)):
        os.system("cd darknet/ \n ls \n ./darknet detector test data/obj.data cfg/yolov3_custom.cfg yolov3_custom_final.weights /Users/evanday/Capstone/Drone/Encrypted-GoPro-Companion-master/Spliced/frame_%d.jpg -out /Users/evanday/Capstone/Drone/Encrypted-GoPro-Companion-master/FinalImages/frame_%d -thresh 0.2" %(i, i))
        i = i+1



#download_and_decrypt(servername)

""" if verbose:
    print("\nStitching videos")
videos = [VideoFileClip(file) for file in glob.glob(video_location+"/*", recursive=False)]
long_vid = concatenate_videoclips(videos)
long_vid.write_videofile(video_location + ".mp4") """

#clean_folder(video_location)
#New 10/22
clean_folder("Spliced/")
#os.rmdir(video_location)
#New 10/22
#Using new Splice.py file
clean_folder("FinalImages/")
splice(video_location + ".mp4")
ImageDetection("Spliced/")



















