"""
# FIRST ATTEMPT
import exifread
f = open("img.jpg", 'rb')

tags = exifread.process_file(f)

for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        "Key: %s, value %s" % (tag, tags[tag])

# OTHER ATTEMPT
import PIL.Image
img = PIL.Image.open('img.jpg')
exif_data = img._getexif()
print(exif_data)
"""
"""
import os

for filename in os.listdir("E:/17th Bday"):
    info = os.stat(filename)
    print(info.st_mtime)


list1 = ["a","b","c","d"]
list2 = []

for letter in list1:
    if letter == "a":
        continue 
    list2.append([letter])
print(list2)

i = 0
while i != len(list2):
    list2[i].append("worked")
    i += 1

print(list2)

import pathlib
import datetime
fname = pathlib.Path('a.py')
mtime = datetime.datetime.fromtimestamp(fname.stat().st_mtime)
print(mtime)

fname = pathlib.Path(oldfilepath)
ctime = datetime.datetime.fromtimestamp(fname.stat().st_ctime)
sortingfiles[i].append(ctime)
"""
import datetime
list1 = [['17_1.jpg', datetime.datetime(2021, 6, 27, 21, 48, 59, 252578)], ['17_10.jpg', datetime.datetime(2021, 7, 21, 0, 15, 54, 468175)], ['17_2.jpg', datetime.datetime(2021, 6, 27, 21, 48, 59, 233593)], ['17_3.jpg', datetime.datetime(2021, 6, 27, 21, 48, 59, 237582)], ['17_4.jpg', datetime.datetime(2021, 6, 27, 21, 48, 59, 247572)], ['17_5.jpg', datetime.datetime(2021, 6, 27, 21, 48, 59, 145073)], ['17_6.jpg', datetime.datetime(2021, 6, 27, 21, 48, 59, 242578)], ['17_7.jpg', datetime.datetime(2021, 6, 20, 15, 52, 14, 85379)], ['17_8.jpg', datetime.datetime(2021, 6, 20, 15, 58, 33, 838040)], ['17_9.jpg', datetime.datetime(2021, 6, 27, 21, 48, 59, 130823)]]

