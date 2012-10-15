#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Version CU 1.01 - January 21, 2010
#
# History:
# This module was started by Mark Guzdial at Georgia Tech in July 2002, for his
# "Introduction to Media Computation" course.
#
# The CU implementation of this module is based on a version that was developed
# from Guzdial's module at U of T in Summer 2007.
#
# Changes in CU 1.00:
# 1. Removed class OpenPictureTool.
# 2. From the global misc functions, deleted open_picture_tool().
#    From the global vars, deleted default_frequency, default_sample_size
#    and default_num_channels.
# 3. From the global picture functions, deleted open_picture_tool(),
#    open_picture_tool_safe().
# 4. Deleted the wrapper functions that provided a procedural interface to
#    the methods provided by Picture, Pixel and Color.
# 5. Renamed make_picture() to load_picture(), to better reflect what it does.
# 6. Class Color:
#    - deleted set_red(), set_green(), set_blue(), set_rgb(), make_darker()
#      and make_lighter(). Color objects are now immutable. This eliminates
#      a potential source of confusion; namely, calling set_red(), set_green()
#      or set_blue() on a Pixel object changes the colour of the pixel (and the
#      picture containing that pixel); however, calling get_color() on a Pixel,
#      then calling set_red(), set_green() or set_blue() on the Color object,
#      had no effect on the pixel.
#    - changed __init__ to throw an exception if the spcified r, g, and b
#      values aren't between 0 and 255. (The mutator methods in Pixel ensure
#      that we can't change a pixel's r, g, and b components to values outside
#      this range, so it seems odd that __init__, along with the deleted setter
#      methods, accepted rgb values that were negative or >= 256.)
# 7. Changed Picture, Pixel and Color to new-style classes.
#
# Changes in CU 1.01
# 1. Renamed pick_a_file to choose_file.
#
# To do: Add docstrings to methods in Picture, Pixel and Color.
#        Consider converting load_picture() and make_empty_picture() into
#        factory methods inside Picture.
#

from math import sqrt
from Tkinter import *
import Image
import ImageDraw
import ImageFont
import ImageTk as imtk
import os
import sys
import time
import tkColorChooser
import tkFileDialog
import tkMessageBox
import tkFont
import user
import thread

##
## Global vars -------------------------------------------------------
##

ver = "CU 1.00"

default_font = ImageFont.load_default()

media_folder = user.home + os.sep

##
## Global misc functions -------------------------------------------------------
##

def version():
    global ver
    return ver


def set_media_path():
    global media_folder
    file = pick_a_folder()
    media_folder = file
    print "New media folder: " + media_folder


def get_media_path(filename):
    global media_folder
    file = media_folder + filename
    if not os.path.isfile(file):
        print "Note: There is no file at " + file
    return file


def choose_file(**options):
    root = Tk()
    root.title("Choose File")
    root.focus_force()
    root.geometry("0x0")
#   root.geometry("+100+200")
    if((sys.platform)[:3] == 'win'):
        root.attributes("-alpha",0.0)
    #root.withdraw()
    path = tkFileDialog.askopenfilename()

    root.destroy()
    return path

def pick_a_folder(**options):
    global media_folder
    folder = tkFileDialog.askdirectory()
    if folder == '':
        folder = media_folder
    return folder


def pick_a_color(**options):
    color = tkColorChooser.askcolor()
    new_color = Color(color[0][0], color[0][1], color[0][2])
    return new_color


#And for those who think of things as folders (5/14/03 AW)


def set_media_folder():
    global media_folder
    file = pick_a_folder()
    media_folder = file
    print "New media folder: " + media_folder


def get_media_folder(filename):
    global media_folder
    file = media_folder + filename
    if not os.path.isfile(file) or not os.path.isdir(file):
        print "Note: There is no file at " + file
    return file


def get_short_path(filename):
    dirs = filename.split(os.sep)
    if len(dirs) < 1:  # does split() ever get to this stage?
        return "."
    elif len(dirs) == 1:
        return dirs[0]
    else:
        return dirs[len(dirs) - 2] + os.sep + dirs[len(dirs) - 1]


def quit():
    sys.exit(0)

##
## COLOR -----------------------------------------------------------------------
##

class Color(object):
    '''An RGB color.'''

    def __init__(self, r, g, b):
        if 0 <= r and r <= 255:
            self.r = r
        else:
            raise ValueError('Invalid red component value (' + str(r) +
                             '), expected value within [0, 255]')

        if 0 <= g and g <= 255:
            self.g = g
        else:
            raise ValueError('Invalid green component value (' + str(g) +
                             '), expected value within [0, 255]')

        if 0 <= b and b <= 255:
            self.b = b
        else:
            raise ValueError('Invalid blue component value (' + str(b) +
                             '), expected value within [0, 255]')

    def __str__(self):
        return "color r=" + str(self.get_red()) + " g=" + str(self.get_green()) + \
            " b=" + str(self.get_blue())

    def __repr__(self):
        return "Color(" + str(self.get_red()) + ", " + str(self.get_green()) + \
            ", " + str(self.get_blue()) + ")"

    def __sub__(self, color):
        return Color(self.r - color.r, self.g - color.g, self.b - color.b)

    def __add__(self, color):
        return Color(self.r + color.r, self.g + color.g, self.b + color.b)

    def __eq__(self, newcolor):
        return self.get_red() == newcolor.get_red() and self.get_green() == \
            newcolor.get_green() and self.get_blue() == newcolor.get_blue()

    def __ne__(self, newcolor):
        return not self.__eq__(newcolor)

    def distance(self, color):
        """
        Return the distance between self and color.
        """
        r = pow(self.r - color.r, 2)
        g = pow(self.g - color.g, 2)
        b = pow(self.b - color.b, 2)
        return sqrt(r + g + b)

    def difference(self, color):
        return self - color

    def get_rgb(self):
        return [self.r, self.g, self.b]

    def get_red(self):
        return self.r

    def get_green(self):
        return self.g

    def get_blue(self):
        return self.b

##
## Color Constants -------------------------------------------------------------
##

aliceblue = Color(240, 248, 255)
antiquewhite = Color(250, 235, 215)
aqua = Color(0, 255, 255)
aquamarine = Color(127, 255, 212)
azure = Color(240, 255, 255)
beige = Color(245, 245, 220)
bisque = Color(255, 228, 196)
black = Color(0, 0, 0)
blanchedalmond = Color(255, 235, 205)
blue = Color(0, 0, 255)
blueviolet = Color(138, 43, 226)
brown = Color(165, 42, 42)
burlywood = Color(222, 184, 135)
cadetblue = Color(95, 158, 160)
chartreuse = Color(127, 255, 0)
chocolate = Color(210, 105, 30)
coral = Color(255, 127, 80)
cornflowerblue = Color(100, 149, 237)
cornsilk = Color(255, 248, 220)
crimson = Color(220, 20, 60)
cyan = Color(0, 255, 255)
darkblue = Color(0, 0, 139)
darkcyan = Color(0, 139, 139)
darkgoldenrod = Color(184, 134, 11)
darkgray = Color(169, 169, 169)
darkgreen = Color(0, 100, 0)
darkkhaki = Color(189, 183, 107)
darkmagenta = Color(139, 0, 139)
darkolivegreen = Color(85, 107, 47)
darkorange = Color(255, 140, 0)
darkorchid = Color(153, 50, 204)
darkred = Color(139, 0, 0)
darksalmon = Color(233, 150, 122)
darkseagreen = Color(143, 188, 143)
darkslateblue = Color(72, 61, 139)
darkslategray = Color(47, 79, 79)
darkturquoise = Color(0, 206, 209)
darkviolet = Color(148, 0, 211)
deeppink = Color(255, 20, 147)
deepskyblue = Color(0, 191, 255)
dimgray = Color(105, 105, 105)
dodgerblue = Color(30, 144, 255)
firebrick = Color(178, 34, 34)
floralwhite = Color(255, 250, 240)
forestgreen = Color(34, 139, 34)
fuchsia = Color(255, 0, 255)
gainsboro = Color(220, 220, 220)
ghostwhite = Color(248, 248, 255)
gold = Color(255, 215, 0)
goldenrod = Color(218, 165, 32)
gray = Color(128, 128, 128)
green = Color(0, 128, 0)
greenyellow = Color(173, 255, 47)
honeydew = Color(240, 255, 240)
hotpink = Color(255, 105, 180)
indianred = Color(205, 92, 92)
indigo = Color(75, 0, 130)
ivory = Color(255, 255, 240)
khaki = Color(240, 230, 140)
lavender = Color(230, 230, 250)
lavenderblush = Color(255, 240, 245)
lawngreen = Color(124, 252, 0)
lemonchiffon = Color(255, 250, 205)
lightblue = Color(173, 216, 230)
lightcoral = Color(240, 128, 128)
lightcyan = Color(224, 255, 255)
lightgoldenrodyellow = Color(250, 250, 210)
lightgreen = Color(144, 238, 144)
lightgrey = Color(211, 211, 211)
lightpink = Color(255, 182, 193)
lightsalmon = Color(255, 160, 122)
lightseagreen = Color(32, 178, 170)
lightskyblue = Color(135, 206, 250)
lightslategray = Color(119, 136, 153)
lightsteelblue = Color(176, 196, 222)
lightyellow = Color(255, 255, 224)
lime = Color(0, 255, 0)
limegreen = Color(50, 205, 50)
linen = Color(250, 240, 230)
magenta = Color(255, 0, 255)
maroon = Color(128, 0, 0)
mediumaquamarine = Color(102, 205, 170)
mediumblue = Color(0, 0, 205)
mediumorchid = Color(186, 85, 211)
mediumpurple = Color(147, 112, 219)
mediumseagreen = Color(60, 179, 113)
mediumslateblue = Color(123, 104, 238)
mediumspringgreen = Color(0, 250, 154)
mediumturquoise = Color(72, 209, 204)
mediumvioletred = Color(199, 21, 133)
midnightblue = Color(25, 25, 112)
mintcream = Color(245, 255, 250)
mistyrose = Color(255, 228, 225)
moccasin = Color(255, 228, 181)
navajowhite = Color(255, 222, 173)
navy = Color(0, 0, 128)
oldlace = Color(253, 245, 230)
olive = Color(128, 128, 0)
olivedrab = Color(107, 142, 35)
orange = Color(255, 165, 0)
orangered = Color(255, 69, 0)
orchid = Color(218, 112, 214)
palegoldenrod = Color(238, 232, 170)
palegreen = Color(152, 251, 152)
paleturquoise = Color(175, 238, 238)
palevioletred = Color(219, 112, 147)
papayawhip = Color(255, 239, 213)
peachpuff = Color(255, 218, 185)
peru = Color(205, 133, 63)
pink = Color(255, 192, 203)
plum = Color(221, 160, 221)
powderblue = Color(176, 224, 230)
purple = Color(128, 0, 128)
red = Color(255, 0, 0)
rosybrown = Color(188, 143, 143)
royalblue = Color(65, 105, 225)
saddlebrown = Color(139, 69, 19)
salmon = Color(250, 128, 114)
sandybrown = Color(244, 164, 96)
seagreen = Color(46, 139, 87)
seashell = Color(255, 245, 238)
sienna = Color(160, 82, 45)
silver = Color(192, 192, 192)
skyblue = Color(135, 206, 235)
slateblue = Color(106, 90, 205)
slategray = Color(112, 128, 144)
snow = Color(255, 250, 250)
springgreen = Color(0, 255, 127)
steelblue = Color(70, 130, 180)
tan = Color(210, 180, 140)
teal = Color(0, 128, 128)
thistle = Color(216, 191, 216)
tomato = Color(255, 99, 71)
turquoise = Color(64, 224, 208)
violet = Color(238, 130, 238)
wheat = Color(245, 222, 179)
white = Color(255, 255, 255)
whitesmoke = Color(245, 245, 245)
yellow = Color(255, 255, 0)
yellowgreen = Color(154, 205, 50)

##
## PICTURE ---------------------------------------------------------------------
##

class Picture(object):

    def __init__(self, auto_repaint=False):
        self.title = "Unnamed"
        self.disp_image = None
        self.win_active = 0

    def __initialize_picture(self, surf, filename, title):
        self.surf = surf

        # we get the pixels array from the surface

        self.pixels = surf.load()

        self.filename = filename
        self.title = title

    def create_image(self, width, height):

        # fail if dimensions are invalid

        if width < 0 or height < 0:
            raise ValueError("create_image(" + str(width) + ", " + str(height) +
                             "): Invalid image dimensions")
        else:
            self.__initialize_picture(Image.new("RGB", (width, height)),
                    '', 'None')

    def load_image(self, filename):
        # global media_folder
        # if not os.path.isabs(filename):
        #    filename = media_folder + filename

        # fail if file does not exist

        if not os.path.isfile(filename):
            raise ValueError("load_image(" + filename +
                             "): No such file")
        else:
            from Image import open
            mode = "RGB"
            image = open(filename).convert(mode)
            size = image.size
            data = image.tostring()

            # initialize this picture with new properties

            self.__initialize_picture(image, filename, get_short_path(filename))

    def crop(self, x1, y1, x2, y2):
        maxX = self.get_width()
        None
        maxY = self.get_height()
        None
        if not 0 <= x1 <= maxX or not 0 <= y1 <= maxY or not x1 < x2 <= \
            maxX or not y1 < y2 <= maxY:
            raise ValueError('Invalid width/height specified')

        image = self.surf.crop((x1, y1, x2, y2))
        self.__initialize_picture(image, self.filename, self.title)

    def clear(self, color=black):

        # clears the picture pixels to black

        self.set_pixels(color)

    def __str__(self):
        return "Picture, filename " + self.filename + " height " + str(self.get_height()) + \
            " width " + str(self.get_width())

    def show(self):
        #if (sys.platform)[:3] == 'win':
        #    i = 1
        #    p = thread.start_new(self.showchild, (i, ))
        #    time.sleep(0.1)
        #else:
        self.surf.show()

        #if raw_input() == 'c': pass

    def showchild(self, tid):
        self.surf.show()

    def do_pick_color(self, event):
        x = event.x + 1
        y = event.y + 1
        if 0 < x and x <= self.get_width() and 0 < y and y < self.get_height():
            pixel = self.get_pixel(x, y)
            print pixel
            None

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def get_image(self):
        if self.get_height() == 0 and self.get_width() == 0:
            raise ValueError
        return self.surf

    def get_width(self):
        return (self.surf.size)[0]

    def get_height(self):
        return (self.surf.size)[1]

    def get_pixel(self, x, y):
        return Pixel(self, x, y)

    def get_pixels(self):
        collect = []

        # we want the width and the height inclusive since Pixel() is one based
        # we increase the ranges so that we don't have to add in each iteration
        #Changed to 0-based!

        for x in range(0, self.get_width()):
            for y in range(0, self.get_height()):
                collect.append(Pixel(self, x, y))

        return collect

    def set_pixels(self, color):
        """set all the pixels in this picture to a given color"""

        try:
            image = Image.new(self.surf.mode, self.surf.size, tuple(color.get_rgb()))
            self.__initialize_picture(image, self.filename, self.title)
        except:
            raise AttributeError('set_pixels(color): Picture has not yet been initialized.')

    def write_to(self, filename):
        # if not os.path.isabs(filename):
        #    filename = media_folder + filename

        self.surf.save(filename)

    def add_rect_filled(self, acolor, x, y, w, h):
        draw = ImageDraw.Draw(self.surf)
        draw.rectangle([x, y, x + w, y + h], outline=tuple(acolor.get_rgb()),
                       fill=tuple(acolor.get_rgb()))
        del draw

    def add_rect(self, acolor, x, y, w, h, width1=1):
        draw = ImageDraw.Draw(self.surf)
        draw.rectangle([x, y, x + w, y + h], outline=tuple(acolor.get_rgb()))
        del draw

    # Draws a polygon on the image.
    def add_polygon(self, acolor, point_list):
        draw = ImageDraw.Draw(self.surf)
        draw.polygon(point_list, outline=tuple(acolor.get_rgb()))
        del draw

    def add_polygon_filled(self, acolor, point_list):
        draw = ImageDraw.Draw(self.surf)
        draw.polygon(point_list, outline=tuple(acolor.get_rgb()), fill=
                     tuple(acolor.get_rgb()))
        del draw

    def add_oval_filled(self, acolor, x, y, w, h):
        draw = ImageDraw.Draw(self.surf)
        draw.ellipse([x, y, x + w, y + h], outline=tuple(acolor.get_rgb()),
                     fill=tuple(acolor.get_rgb()))
        del draw

    def add_oval(self, acolor, x, y, w, h):
        draw = ImageDraw.Draw(self.surf)
        draw.ellipse([x, y, x + w, y + h], outline=tuple(acolor.get_rgb()))
        del draw

    def add_arc_filled(self, acolor, x, y, w, h, start, end):
        draw = ImageDraw.Draw(self.surf)
        draw.arc([x, y, x + w, y + h], start, end, outline=tuple(acolor.get_rgb()),
                 fill=tuple(acolor.get_rgb()))
        del draw

    def add_arc(self, acolor, x, y, w, h, start, end):
        draw = ImageDraw.Draw(self.surf)
        draw.arc([x, y, x + w, y + h], start, end, outline=tuple(acolor.get_rgb()))
        del draw

    def add_line(self, acolor, x1, y1, x2, y2, width1=1):
        draw = ImageDraw.Draw(self.surf)
        draw.line([x1, y1, x2, y2], fill=tuple(acolor.get_rgb()), width=
                  width1)
        del draw

    def add_text(self, acolor, x, y, string):
        global default_font
        self.add_text_with_style(acolor, x, y, string, default_font)

    def add_text_with_style(self, acolor, x, y, string, font1):
        draw = ImageDraw.Draw(self.surf)
        draw.text((x, y), text=string, fill=tuple(acolor.get_rgb()),
                  font=font1)
        del draw

#
# PIXEL ------------------------------------------------------------------------
#

class Pixel(object):
    '''A pixel in an image with a color and an x and y location.'''

    def __init__(self, picture, x, y):

        if not picture.__class__ == Picture:
            raise ValueError("Pixel(picture, x, y): picture input is not a Picture")

        len_x = picture.get_width()
        len_y = picture.get_height()
        if x <= -1 * len_x or x >= len_x or y <= -1 * len_y or y >= \
            len_y:
            raise IndexError
        if len_x > 0 and len_y > 0:
            self.x = x % len_x
            self.y = y % len_y

            self.pix = picture
        else:
            raise ValueError('Invalid image dimensions (' + str(len_x) +
                             ", " + str(len_y) + ")")

    def __str__(self):
        return "Pixel, color=" + str(self.get_color())

    def set_red(self, r):
        if 0 <= r and r <= 255:
            (self.pix.pixels)[self.x, self.y] = (r, (self.pix.pixels)[self.x,
                    self.y][1], (self.pix.pixels)[self.x, self.y][2])
        else:
            raise ValueError('Invalid red component value (' + str(r) +
                             '), expected value within [0, 255]')

    def set_green(self, g):
        if 0 <= g and g <= 255:
            (self.pix.pixels)[self.x, self.y] = ((self.pix.pixels)[self.x,
                    self.y][0], g, (self.pix.pixels)[self.x, self.y][2])
        else:
            raise ValueError('Invalid green component value (' + str(g) +
                             '), expected value within [0, 255]')

    def set_blue(self, b):
        if 0 <= b and b <= 255:
            (self.pix.pixels)[self.x, self.y] = ((self.pix.pixels)[self.x,
                    self.y][0], (self.pix.pixels)[self.x, self.y][1], b)
        else:
            raise ValueError('Invalid blue component value (' + str(b) +
                             '), expected value within [0, 255]')

    def get_red(self):
        return int((self.pix.pixels)[self.x, self.y][0])

    def get_green(self):
        return int((self.pix.pixels)[self.x, self.y][1])

    def get_blue(self):
        return int((self.pix.pixels)[self.x, self.y][2])

    def get_color(self):
        return Color(self.get_red(), self.get_green(), self.get_blue())

    def set_color(self, color):
        self.set_red(color.get_red())
        self.set_green(color.get_green())
        self.set_blue(color.get_blue())

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

##
## Global picture functions ----------------------------------------------------
##

def load_picture(filename):
    """Creates a picture.

       filename: a string represeting the location and name of picture

       Return a instance of picture class, on success"""

    picture = Picture()
    picture.load_image(filename)
    try:
        w = picture.get_width()
        return picture
    except:
        print "Was unable to load the image in " + filename + \
            "\nMake sure it's a valid image file."

def make_empty_picture(width, height):
    """Generates a blank picture.

       width: the width of the picture
       height:  the height of the picture

       Return a instance of picture class"""

    picture = Picture()
    picture.create_image(width, height)
    return picture

def crop_picture(picture, x1, y1, x2, y2):
    """Replaces picture with a rectangular region from the current picture.
       Note coordinates are zero-based so to get a 50x50 image starting from
       top left corner the coordinates would be: 0,0,49,49.

       picture: the picture to be cropped
       x1: defines left pixel coordinate
       y1: defines upper pixel coordinate
       x2: defines right pixel coordinate
       y2: defines lower pixel coordinate."""

    if not picture.__class__ == Picture:
        raise ValueError("crop_picture(picture,x1,y1,x2,y2): First input is not a picture")
    picture.crop(x1, y1, x2 + 1, y2 + 1)

##
## DEBUG -----------------------------------------------------------------------
##

# the following allows us to wrap an error message and display specific
# information depending on the context


def exception_hook(type, value, traceback):
    try:
        global debug_level
        cur_level = debug_level
    except:
        cur_level = 0

    # handle each level

    if cur_level == 0:

        # user mode

        print str(value)
        sys.exc_clear()
    elif cur_level == 1:
        raise value
    else:

        # normal error mode

        tb = traceback
        framestack = []
        while tb:

            # get the current frame

            framestack.append(tb.tb_frame)

            # and traverse back to the top

            tb = tb.tb_next
        framestack.reverse()

        # print the message and each calling method

        print "Message: (%s)\n    %s" % (str(type), value)
        print "Stack Trace:"
        for temp_frame in framestack:
            print "    [%s:(%d)] - %s()" % (temp_frame.f_code.co_filename,
                    temp_frame.f_lineno, temp_frame.f_code.co_name)
        sys.exc_clear()


# set the hook

sys.excepthook = exception_hook

# graphical warnings and prompts


def show_warning(msg, title="Warning"):
    tkMessageBox.showwarning(title, msg)


def show_error(msg, title="Error"):
    tkMessageBox.showerror(title, msg)


#
# all prompts return:
#       -1 for cancel (if there are > 2 choices)
#       0 for no/cancel (only if there are 2 choices)
#       1 for yes/ok
#


def prompt_yes_no(prompt_msg, title):
    result = tkMessageBox.askquestion(title, prompt_msg, default=
            tkMessageBox.NO)
    if result == 'yes':
        return 1
    else:
        return 0


def prompt_ok_cancel(prompt_msg, title):
    return int(tkMessageBox.askokcancel(title, prompt_msg, default=
               tkMessageBox.CANCEL))


#
# set the default debug level
# 0 - print user friendly error msgs only (default)
# 1 - throw normal errors
# 2 - show simple errors & stack trace
#

debug_level = 0
