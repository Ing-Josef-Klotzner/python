#! /usr/bin/env python2
# mozart.py  --  created by Ing. Josef Klotzner
import Image,re

def get_image(s):
    return Image.open(s, "r")
im = get_image('mozart.gif')
w,h = im.size

magenta = 195   # deduced by looking at the GIF's colour palette in GraphicConverter
bars = []
for j in range(h):
    for i in range(w - 5):
        if im.getpixel((i,j)) == magenta and im.getpixel((i+4,j)) == magenta:
            bars.append((i,j))
print min(bars)
shift = Image.new(im.mode, (w, h), 0)
shift.palette = im.palette  # share colour table
for j in range(h):
    for i in range(w):
        shift.putpixel(((i + w - bars[j][0]) % w, j), im.getpixel((i,j)))
shift.show()

img = Image.open("mozart.gif")
imgtext = img.tostring().replace('\n','0')
imgtext = '\n'.join([imgtext[i*640:(i+1)*640] for i in range(480)])
imgtext = re.compile('^(.*?)(\xc3{5})(.*?)$',re.M).sub(r'\2\3\1', imgtext).replace('\n',"")
img.fromstring(imgtext)
img.show()

im = Image.open("mozart.gif")
magic = chr(195)
for y in range(im.size[1]):
    box = 0, y, im.size[0], y+1 # box bounding row y
    row = im.crop(box)
    bytes = row.tostring()
    # Rotate 195 to the first column.
    i = bytes.index(magic)
    bytes = bytes[i:] + bytes[:i]
    row.fromstring(bytes)
    im.paste(row, box)  # overwrite the original row
im.show()
