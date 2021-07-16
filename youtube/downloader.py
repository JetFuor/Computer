from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

print(yt.streams) # Shows all available download streams
print(yt.streams.filter(only_audio=True)) # Shows audio only
print(yt.streams.filter(only_video=True)) # Shows video only
print(yt.streams.filter(progressive=True)) # Shows ones that have both audio and video in them
ys = yt.streams.get_highest_resolution() # Gives highest res video
ys = yt.streams.get_by_itag('22') # Can chooase the specific one as well
ys.download() # Downloads the specifc one wanted, can specify location in the brackets

# Can also download higher res video only, then download audio and merge later for better quality

# Sample code
"""
from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
"""