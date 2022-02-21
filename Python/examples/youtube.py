#/usr/bin/env python

# requirements
# pytube and moviepy --> pip install pytube and pip install moviepy
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from os import system, name
import time
import datetime
from datetime import time, timedelta, datetime

standard_header=">> YOUTUBE VIDEO DOWNLOADER <<"

def header(header):
    print(f"{header}")

# clearing the screen 
def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")

# downloading the video from youtube
def download_video(video_url, final_video_name):

    print("- Downloading your video...")
    
    yt = YouTube(video_url)

    video = yt.streams.get_highest_resolution()
    video.download(filename=f"{final_video_name}.mp4")

# cutting the video by section
def cut_video(video_local_path, start_time, end_time, final_file):

    print("- Cutting your video...")

    time_format = '%H:%M:%S'
    #diff = datetime.strptime(end_time, time_format) - datetime.strptime(start_time, time_format)

    #start_time = datetime.datetime(2022,1,1,0,3,10)
    #end_time = datetime.datetime(2022,1,1,0,6,0)
    #diff = (end_time-start_time).total_seconds()

    ffmpeg_extract_subclip(r"{}".format(video_local_path), time_to_sec(start_time), time_to_sec(end_time), targetname=f"{final_file}.mp4")

# downloading and cutting 
def download_and_cut_video(video_url, video_name_after_cut, start_time, end_time):
    
    download_video(video_url,"temp_video") 
    cut_video(r"./temp_video.mp4", start_time, end_time, video_name_after_cut)
 
#converting time to seconds
def time_to_sec(t):
   h, m, s = map(int, t.split(':'))
   return h * 3600 + m * 60 + s

while True:
    clear_screen()

    header(standard_header)
    print("(1) - Download Youtube video")
    print("(2) - Cut Video")
    print("(3) - Download and cut video")
    user_option = input("Option: ")

    match user_option:
        case ("1"):

            while True:

                clear_screen()
                header(standard_header)
                header("> Download Youtube Video")
            
                url = input(" - Video URL: ")
                file_name = input(" - File output name: ")

                if url == "" or file_name == "":
                    print("- Provide the info required!") ; input()
                else:
                    if download_video(url,file_name):
                        print("Video downloaded!") ; input() ; break
                    else:
                        print("Sorry, video not downloaded!") ; input() ; break

        case ("2"):

            clear_screen()
            header(standard_header)
            header("> Cut video")
            print("Option 2 logic here...") ; input()

        case("3"):

            while True:

                clear_screen()
                header(standard_header)
                header("> Download and Cut Youtube video")
                
                url = input(" - Video URL: ")
                file_name = input(" - File output name: ")
                start = input(" - Start point: ")
                end = input(" - End point: ")

                download_and_cut_video(url, file_name, start, end)

        case("q"):
            print("Exiting now...")
            time.sleep(1)

        case _: 
            print("Insert a valid option...") ; time.sleep(1)

    if user_option.lower() == "q":
        break;