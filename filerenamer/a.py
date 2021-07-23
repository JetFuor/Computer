import exifread
# Open image file for reading (binary mode)
f = open("17bday_4.jpg", 'rb')

# Return Exif tags
tags = exifread.process_file(f)

print(tags)