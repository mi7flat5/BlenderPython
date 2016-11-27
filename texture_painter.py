'''Renders text from a CSV file to textures
and applies them to multiple objects.

Use snippets...
import os, sys; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
import importlib; importlib.reload(texture_painter); texture_painter.go()
'''
import codecs, csv, os, bpy
from PIL import Image, ImageDraw, ImageFont


def get_backers(csv_filename):
   with codecs.open(csv_filename, 'r', 'utf-8-sig') as stream:
       iterable = csv.reader(stream)
       header = next(iterable)
       for row in iterable:
           backers = dict(zip(header,row))
           yield backers

def render_text_to_file(text_to_render, to_filename):
    baseimage = Image.new('RGB', (512,64))
    draw = ImageDraw.Draw(baseimage)
    fnt = ImageFont.truetype('arial.ttf',50)
    draw.text((0,0),text_to_render, font = fnt, fill=(255,255,255))
    baseimage.save(to_filename)

def readCSV():
    cwd = os.path.dirname(bpy.data.filepath)
    for backer in get_backers('backers.csv'):
        textToRender = backer.get('Name')+' '+backer.get('Country')
        toFileName = cwd +'\\texture_cache\\'+backer.get('Number')+'.png'
        render_text_to_file(textToRender ,toFileName)

def throw_invalid_selection():
    if len(bpy.context.selected_objects)== 0:
        raise Exception("Please select exactly one prototype object")
    if len(bpy.context.selected_objects) > 1:
        raise Exception("Please select exactly one prototype object")

def create_plaque(prototype,offset):
    prototype.select = True
    bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":offset})
    new_plaque = bpy.context.selected_objects[0]
    bpy.ops.object.select_all(action='TOGGLE')
    return new_plaque

def get_offset(num, rows, spacing):
    x_offset = (num % rows) * spacing[0]
    y_offst =  (num //rows) * spacing[1]
    return (x_offset,y_offst)


def go():
    print("Texture Painter starting up.")
    #readCSV()
    throw_invalid_selection()
    print("prototype object found")
    prototype = bpy.context.selected_objects[0]
   
    for num, backer in enumerate(get_backers("backers_10.csv")):
        if num== 0:
            plaque = prototype
        else:
            x,y = get_offset(num,4,(2,2,0))
            plaque = create_plaque(prototype,(x,y,0))
        print("swapping texture to:",backer)

