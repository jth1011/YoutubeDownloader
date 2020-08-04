import os
import sys
import requests
import getpass
import ffmpeg
from re import sub
from pytube import YouTube
from pytube import Stream

def down_done(stream, file_path):
    print("Downloaded to " + file_path)
    
def get_down(tube, video: bool) -> Stream:
    best = 0
    to_down = None
    only_vid = False
    only_aud = False
    if (video):
        only_vid = True
    else:
        only_aud = True
    for video in tube.streams.filter(only_video=only_vid, only_audio=only_aud,):
        if (only_vid and video.get_fr() != None and int(sub("[^0-9]", "", video.get_fr())) > best):
            to_down = video
            best = int(sub("[^0-9]", "", video.get_fr()))
        elif (only_aud and video.get_abr() != None and int(sub("[^0-9]", "", video.get_abr())) > best):
            to_down = video
            best = int(sub("[^0-9]", "", video.get_abr()))
    #print(tube.streams.filter(only_video=True).json())
    return to_down

def convert(in_file):
    print("None")


def main():
    SAVE_SPOT = "C:\\Users\\"+getpass.getuser()+"\\Downloads"
    vid_name = input("Enter Video Name: ")
    vid_name = vid_name.strip()
    vid_name = vid_name.replace(" ","+")
    if (vid_name == ""):
        print("Nothing to Search")
        exit()
    link = "https://www.googleapis.com/youtube/v3/search/?key=AIzaSyCPpjgXrEJcPFm1PuxEfmwWKH1u2s-7H6s&part=snippet&type=video&maxResults=1&order=relevance&q=" + vid_name
    resp = requests.get(link)
    resp=resp.json()
    vid=resp['items'][0]['id']['videoId']
    link="https://www.youtube.com/watch?v=" + vid
    tube = None
    #try:
    tube = YouTube(link, on_complete_callback=down_done)
    #except:
        #print("Error getting requested video...")
    withVid = input("Download (V)ideo or (A)udio)? ")
    while(withVid != 'v' and withVid != 'V' and withVid != 'a' and withVid != 'A'):
        withVid = input("Download (V)ideo or (A)udio)? ")
    if tube is not None:
        if withVid == 'v' or withVid == 'V':
            to_down = get_down(tube, True).download(output_path=SAVE_SPOT)
            to_down = get_down(tube, False).download(output_path=SAVE_SPOT)
        else:
            to_down = get_down(tube, False).download(output_path=SAVE_SPOT)
            pre, ext = os.path.splitext(to_down)
            if (ext != '.mp3'):
                in_aud = ffmpeg.input(to_down)
                out_aud = ffmpeg.output(in_aud, pre + '.mp3', aq=0)
                out_aud.run()
                os.remove(to_down)

if __name__ == "__main__":
    main()
