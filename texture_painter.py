'''Renders text from a CSV file to textures
and applies them to multiple objects.

Use snippets...
import os, sys; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
import importlib; importlib.reload(texture_painter); texture_painter.go()
'''
import codecs
import csv
from PIL import Image, ImageDraw, ImageFont

def get_backers(csv_filename):
   with codecs.open(csv_filename, 'r', 'utf-8-sig') as stream:
       iterable = csv.reader(stream)
       header = next(iterable)
       for row in iterable:
           backers = dict(zip(header,row))
           yield backers

def render_text_to_file(text_to_render):
    burp = 1



def go():
    print("Texture Painter starting up.")
    for backer in get_backers('backers_10.csv'):
        print(backer)
    base = Image.open('stand.png').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
    fnt = ImageFont.truetype('arial.ttf', 400)
# get a drawing context
    d = ImageDraw.Draw(txt)

# draw text, half opacity
    d.text((100,100), "Hello", font=fnt, fill=(255,255,255,128))
# draw text, full opacity
    d.text((100,600), "World", font=fnt, fill=(255,255,255,255))

    out = Image.alpha_composite(base, txt)
    out.save('standWwords.png')
    out.show()