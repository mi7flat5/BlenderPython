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
    baseimage = Image.new('RGB', (128,128))
    draw = ImageDraw.Draw(baseimage)
    fnt = ImageFont.truetype('arial.ttf',20)
    draw.text((0,0),text_to_render, font = fnt, fill=(255,255,255))
    baseimage.save('test.png')


def go():
    print("Texture Painter starting up.")
    for backer in get_backers('backers_10.csv'):
        print(backer)
    render_text_to_file("junk")
