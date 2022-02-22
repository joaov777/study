#/usr/bin/env python

# REQUIRED LIBRARIES
#pip install pytube moviepy ffmpeg
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from os import system, name
import time
from datetime import time, timedelta, datetime

standard_header=">> YOUTUBE VIDEO DOWNLOADER <<"

#for headers and better UI
def reloader(header, screen_clear="False"):

    if screen_clear == True:
        clear_screen()

    print(f"{header}")

# clearing the screen 
def clear_screen():
    system("cls") if name == "nt" else system("clear")

# downloading the video from youtube
def download_video(video_url, final_video_name):

    print("- Downloading your video...")
    
    yt = YouTube(video_url)

    video = yt.streams.get_highest_resolution()
    video.download(filename=f"{final_video_name}.mp4")

# cutting the video by section
def cut_video(video_local_path, start_time, end_time, final_file):

    print("- Cutting your video...")
    ffmpeg_extract_subclip(r"{}".format(video_local_path), time_to_sec(start_time), time_to_sec(end_time), targetname=f"{final_file}.mp4")

# downloading and cutting 
def download_and_cut_video(video_url, video_name_after_cut, start_time, end_time):
    
    download_video(video_url,"temp_video") 
    cut_video(r"./temp_video.mp4", start_time, end_time, video_name_after_cut)
 
#converting time to seconds
def time_to_sec(t):
   h, m, s = map(int, t.split(':'))
   return h * 3600 + m * 60 + s

#main menu
while True:
    
    reloader(standard_header)
    print("(1) - Download Youtube video")
    print("(2) - Cut Video")
    print("(3) - Download and cut video")
    user_option = input("Option: ")

    match user_option:
        case "1":

            while True:
                
                reloader(standard_header, True)
                reloader("> Download Youtube Video")
            
                url = input("- Video URL: ")
                file_name = input(" - File output name: ")

                if url == "" or file_name == "":
                    print("- Provide the info required!") ; input()
                else:
                    print("- Success! Video downloaded!") if download_video(url,file_name) else print("- Error! Video not downloaded!")
                    input()
                    break

        case "2":

            reloader(standard_header, True)
            reloader("> Cut video")
            print("Option 2 logic here...") ; input()

        case "3":

            while True:

                reloader(standard_header, True)
                reloader("> Download and Cut Youtube video")
                
                url = input("- Video URL: ")
                file_name = input("- File output name: ")
                start = input("- Start point: ")
                end = input("- End point: ")

                download_and_cut_video(url, file_name, start, end)

        case("q"):
            print("Exiting now...")
            time.sleep(1)

        case _: 
            print("Insert a valid option...") ; time.sleep(1)

    if user_option.lower() == "q":
        break;