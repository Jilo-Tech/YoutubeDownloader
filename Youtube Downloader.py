#!/usr/bin/env python3
### Libraries ###
from pytube.contrib.playlist import Playlist
from pytube import YouTube
from pytube.cli import on_progress
import os	
### Main ###
def Single_Downloader():
	video_url = input("Enter The URL ===> ")
	video = YouTube(video_url)
	video = video.streams.get_highest_resolution()
	video.download()
	print("\nDone .")


def Playlist_Downloader():
	url = input("Enter The URL ===> ")
	playlist = Playlist(url)
	print("Total Videos: ",len(playlist.video_urls))
	for video_url in playlist.video_urls:
	    yt=YouTube(video_url,on_progress_callback=on_progress)
	    stream=yt.streams.get_highest_resolution()
	    print(yt.title)
	    stream.download(filename=yt.title+".mp4")
	print("\nDone .")

def main():
	os.system('cls')
	print("\nHey, Which one You Want ==> ?\n","\n1.Single Video Downloader","\n2.Playlist Downloader","\n3.Quit")
	answer = input("\n===> ")
	if answer =='1':
		os.system('cls')
		Single_Downloader()
	elif answer =='2':
		os.system('cls')
		Playlist_Downloader()
	elif answer =='3':
		exit()
	else:
		print("Wrong input...,Try Again ")
		os.system('cls')
		main()

if __name__ == '__main__':
	main()