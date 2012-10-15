import CU_picture
import math

def negative(pict):
    for pixel in pict.get_pixels():
        #grabbing pixel values
        red = pixel.get_red()
        green = pixel.get_green()
        blue = pixel.get_blue()
    
        #setting blue pixel values
        
        pixel.set_blue(255 - blue)
        
     #setting green pixel values
       
        pixel.set_green(255 - green)
        
     #setting red pixel values
       
        pixel.set_red(255 - red)
            
def grayscale(pict):
    for pixel in pict.get_pixels():
    #grabbing pixel values
        red = pixel.get_red()
        green = pixel.get_green()
        blue = pixel.get_blue()
    #finding average pixel value to asses brightness of pixel
        ave = int((red + green + blue) / 3)
    
    #setting pixel values for RGB
        pixel.set_red(ave)
        pixel.set_green(ave)
        pixel.set_blue(ave)


def _adjust_component(amount):
    #determining the blin in which the amount lies
    if amount >= 0  and amount <= 63 :
    #setting amount to midpoint of bin
        amount = 31
    elif amount >= 64 and amount <= 127:
        amount = 95
    elif amount >= 128 and amount <= 191:
        amount = 159
    elif amount >= 192 and amount <= 255:
        amount = 223
    
    #print amount   
    return amount

def posterize(pict):
    for pixel in pict.get_pixels():
         #grabbing pixel values
        red = pixel.get_red()
        green = pixel.get_green()
        blue = pixel.get_blue()
        
        #setting the RGB values and calling the _adjust_component function
        
        pixel.set_red(_adjust_component(red))
        pixel.set_green(_adjust_component(green))
        pixel.set_blue(_adjust_component(blue))
    
def sepia_tint(pict):
    
    # call grayscale function
    grayscale(pict)
    
    for pixel in pict.get_pixels():
        
        #grabbing blue pixel value
        
        blue = pixel.get_blue()
        red =pixel.get_red()
        green =pixel.get_green()
        
        # checking if value of the red pixels are in defined bins and changing them accordingly
        if red < 63:
            blue = int(blue*0.9)
            red = int(red*1.1)
        elif 63 <= red <= 191:
            blue = int(blue*0.85)
            red = int(red*1.15)
        elif 192 <= red :
            blue = int(blue*0.93)
            if int(red*1.08) > 255:
                red = 255
            else: 
                red = int(red*1.08)

                pixel.set_blue(blue)
                pixel.set_red(red)
        