from pytube import YouTube
from sys import argv

'''we'll this program from the command 
line using the program name and the link to the video'''

link = argv[1] #gets the first command line argument when we run the program which is the link to the youtube video

yt = YouTube(link) #

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Description: ", yt.description)

resolutions = 720

yd = yt.streams.get_by_resolution(resolutions)

yd.download("/Users/ASUS-PC/Downloads/Video")