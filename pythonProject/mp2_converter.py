import os
import sys
from rgb_yuv import resize_images

def convert_mp4_to_mp2(name):
    # Converts a mp4 video to mpg video
    # Takes as inputs the name of the video

    command = 'ffmpeg -i ' + name + ' -c:v mpeg2video -q:v 6 -c:a mp2 output.mpg'
    os.system(command)

convert_mp4_to_mp2("BBB.mp4")

def modify_resolution(name, width, height):
    command = 'ffmpeg -i ' + name + ' -vf "scale=' + str(width) + ':' + str(height) +'" BBB_res2.mp4'
    os.system(command)

modify_resolution("BBB.mp4", 1080, 720)

def chroma_subsampling(name, pr1, pr2):

    # Check for appropiate values
    if (pr1 != 4 and pr1 != 2):
        print("Incorrect values")
        return -1
    if (pr1 == 4 and pr2 != 4):
        print("Incorrect values")
        return -1
    if (pr1 == 2 and pr2 != 2):
        if (pr2 != 0):
            print("Incorrect values")
            return -1
    command = 'ffmpeg -i ' + name + ' -c:v libx264 -vf format=yuv4' + str(pr1) + str(pr2) + 'p BBB_chroma.mp4'
    os.system(command)

chroma_subsampling('BBB.mp4', 2, 2)

def print_info(name):
    command = 'ffmpeg -i ' + name +' 2>&1 | grep "Duration"'
    os.system(command)
    command = 'ffprobe ' + name +' 2>&1 >/dev/null | grep Stream.*Video'
    os.system(command)

print_info('BBB.mp4')

def resize_frame(name):
    command = "ffmpeg -i " + name + " -vf 'select=eq(n\,34)' -vframes 1 out.png"
    os.system(command)
    resize_images("out.png", 480)

resize_frame("BBB.mp4")