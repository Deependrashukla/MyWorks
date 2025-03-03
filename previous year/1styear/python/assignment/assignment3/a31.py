""" 
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

SONAL KUMARI
20 th feburary,2023
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    
    return introcs.RGB(255 - rgb.red, 255 - rgb.green, 255 - rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.
    
    value = float(value)
    point_position = str(value).find('.')
    if point_position == 3:
        value = round(value, 1)
    elif point_position == 2:
        value = round(value, 2)
    elif point_position == 1:
        value = round(value, 3)
    else:
        value = round(value, 4)
    value=str(value)
    
    while len(value) < 5:
        value += "0"
        
    return (value[:5])    
           
    


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    
    c = str5(cmyk.cyan)
    m = str5(cmyk.magenta)
    y = str5(cmyk.yellow)
    k = str5(cmyk.black)
    return f'({c}, {m}, {y}, {k})'


def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """

    h=str5(hsv.hue)
    s=str5(hsv.saturation)
    v=str5(hsv.value)
    return f'({h}, {s}, {v})'


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.

    r_prime = rgb.red / 255.0
    g_prime = rgb.green / 255.0
    b_prime = rgb.blue / 255.0

    k= 1- max(r_prime,g_prime,b_prime)
    if k == 1.0:
        return introcs.CMYK(0.0, 0.0, 0.0, 100.0)
    else:
        c = (1 - r_prime - k) / (1 - k)
        m = (1 - g_prime - k) / (1 - k)
        y = (1 - b_prime - k) / (1 - k)
    return introcs.CMYK(c * 100.0, m * 100.0, y * 100.0, k * 100.0)    
        

def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0. 
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()
    r_prime = (1 - cmyk.cyan / 100.0) * (1 - cmyk.black / 100.0)
    g_prime = (1 - cmyk.magenta / 100.0) * (1 - cmyk.black / 100.0)
    b_prime = (1 - cmyk.yellow / 100.0) * (1 - cmyk.black / 100.0)
    return introcs.RGB(round( r_prime * 255.0 ), round( g_prime * 255.0 ), round( b_prime * 255.0 ))


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    r_prime = rgb.red / 255.0
    g_prime = rgb.green / 255.0
    b_prime = rgb.blue / 255.0
    maxOfRgb=max(r_prime, g_prime, b_prime)
    minOfRgb=min(r_prime, g_prime, b_prime)


    if maxOfRgb == minOfRgb:
        hue = 0.0
    elif maxOfRgb == r_prime and g_prime >= b_prime:
        hue = 60.0 * (g_prime - b_prime) / (maxOfRgb - minOfRgb)
    elif maxOfRgb == r_prime and g_prime < b_prime:
        hue = 60.0 * (g_prime - b_prime) / (maxOfRgb - minOfRgb) + 360.0
    elif maxOfRgb == g_prime:
        hue = 60.0 * (g_prime - b_prime) / (maxOfRgb - minOfRgb) + 120.0
    elif maxOfRgb == b_prime:
        hue=60.0 * (g_prime - b_prime) / (maxOfRgb - minOfRgb) + 240.0


    if maxOfRgb==0:
        saturation=0.0
    else:
        saturation = 1 - minOfRgb / maxOfRgb

    value = maxOfRgb 
    return introcs.HSV(hue, saturation, value)  
        

def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """

    h_i = math.floor( hsv.hue / 60 )
    f=hsv.hue / 60-h_i
    p=hsv.value * ( 1 - hsv.saturation )
    q=hsv.value * ( 1- f * hsv.saturation )
    t=hsv.value * ( 1 - (1 - f) * hsv.saturation)

    if h_i == 0 or h_i == 5:
        red = hsv.value
    elif h_i == 1:
        red = q
    elif h_i == 2 or h_i == 3:
        red = p
    elif h_i == 4:
        red = t

    
    if h_i == 0:
        green = t
    elif h_i == 1 or h_i == 2:
        green = hsv.value
    elif h_i == 3:
        green = q
    elif h_i == 4 or h_i == 5:
        green = p
    

    if h_i == 0 or h_i == 1:
        blue = p
    elif h_i == 1 or h_i == 2:
        blue = t
    elif h_i == 3 or h_i == 4:
        blue = hsv.value
    elif h_i == 5:
        blue = q

    
    return introcs.RGB(round( red*255 ),round( green*255 ),round( blue*255 )) 


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast
    
    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart, 
    with all values becoming 0 or 1 when contrast = 1.
    
    Parameter value: the value to adjust
    Precondition: value is a float in 0..1
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """

    if -1 <= contrast < 1:
        if value < 0.25 + 0.25 * contrast:
            y = ((1 - contrast) / (1 + contrast)) * value
        elif value > 0.75 - 0.25 * contrast:
            y = ((1 - contrast) / (1 + contrast)) * (value - (3 - contrast) / 4) + (3 + contrast) / 4
        else:
            y = ((1 + contrast) / (1 - contrast)) * (value -((1 + contrast) / 4)) + (1 - contrast) / 4
    else:
        if value >= 0.5:
            y = 1
        else:
            y = 0
    return y       



def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb
    
    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.
    
    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    rgb.red = round((contrast_value( rgb.red / 255, contrast)) * 255)
    rgb.green = round((contrast_value( rgb.green / 255, contrast)) * 255)
    rgb.blue = round((contrast_value( rgb.blue / 255, contrast)) * 255)

    
