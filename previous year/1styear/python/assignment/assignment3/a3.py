""" 
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

YOUR KIRTAN KHICHI 
DATE:- 15 FEB, 2022.
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
    if '.' in str(value):
        num_str = str(value)                           # Converting value into string.
        pos = num_str.find('.')                        # Finding Position of dot(.).
        round_value = round(value, 4 - pos)            # Rounding the value according to the position of dot(.).
        str_round_value = str(round_value)             # Converting rounded value into string.
        if len(str_round_value) == 5:                  # Round value have five characters.
            return str_round_value
        else:
            return str_round_value + '0' * (5 - len(str_round_value)) 

    else:                                              # If value not contains dot(.0) 
        if not 'e' in str(value):                      # If value not contains scientific notation(e).
            num_str = str(value)
            len_value = len(num_str)
            value_str = num_str + '.' + (4 - len_value) * '0'
            return value_str

        else:                                          # If contains scientific notation(e). 
            num_str = "{:5f}".format(value)
            return str5(float(num_str))


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
    return f'({str5((cmyk.cyan))}, {str5((cmyk.magenta))}, {str5((cmyk.yellow))}, {str5((cmyk.black))})'



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
    return f'({str5(float(hsv.hue))}, {str5(float(hsv.saturation))}, {str5(float(hsv.value))})'


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    red = rgb.red / 255
    green = rgb.green / 255
    blue = rgb.blue / 255

  
    black = (1 - max(red, green, blue))   #black color.

    if black == 1.0 :
        return introcs.CMYK(0.0, 0.0, 0.0, 100.0)

    else:
        cyan = (1 - red - black) / (1 - black)            #cyan.
        magenta = (1 - green - black) / (1 - black)       #Magenta.
        yellow = (1 - blue - black) / (1 - black)         #yellow.
    

    return introcs.CMYK(cyan * 100, magenta * 100, yellow * 100, black * 100)


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0. 
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()

   
    red = 255 * (1 - cmyk.cyan / 100) * (1 - cmyk.black / 100)
    green = 255 * (1 - cmyk.magenta / 100) * (1 - cmyk.black / 100) 
    blublack = 255 * (1 - cmyk.yellow / 100) * (1 - cmyk.black / 100) 

    return introcs.RGB(round(red) , round(green), round(blublack))

def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    red = rgb.red / 255
    green = rgb.green / 255
    blue = rgb.blue / 255

    maxOfRgb = max(red, green, blue)
    minOfRgb = min(red, green, blue)

    if maxOfRgb == minOfRgb :
        hue = 0.0

    elif maxOfRgb == red and green >= blue :
        hue = 60.0 * (green - blue) / (maxOfRgb - minOfRgb)

    elif maxOfRgb == red and green < blue :
        hue = 60.0 * (green - blue) / (maxOfRgb - minOfRgb) + 360.0

    elif maxOfRgb == green :
        hue = 60.0 * (blue - red) / (maxOfRgb - minOfRgb) + 120.0

    elif maxOfRgb == blue :
        hue = 60.0 * (red - green) / (maxOfRgb - minOfRgb) + 240.0

    if maxOfRgb == 0 :
        saturation = 0

    else:
        saturation = 1 - minOfRgb / maxOfRgb

    value = maxOfRgb 

    return introcs.HSV(float(hue), float(saturation), float(value)) 


def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    hue_floor = hsv.hue // 60
    v = hsv.value
    f = (hsv.hue / 60) - hue_floor
    p = hsv.value * (1 - hsv.saturation)
    q = hsv.value * (1 - (f * hsv.saturation))
    t = hsv.value * (1 - (1 - f) * hsv.saturation)

    if hue_floor == 0 :
        red = v
        green = t 
        blue = p 

    elif hue_floor == 1 :
        red = q
        green = v
        blue = p 

    elif hue_floor == 2 :
        red = p 
        green = v 
        blue = t 

    elif hue_floor == 3 :
        red = p
        green = q
        blue = v 

    elif hue_floor == 4 :
        red = t
        green = p
        blue = v 

    elif hue_floor == 5 :
        red = v 
        green = p
        blue = q

    return introcs.RGB(round(red * 255), round(green * 255), round(blue * 255))


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
    if contrast == 1 :
        if value >= 0.5 :
            return 1 

        else:
            return 0 
    else:
        if value < 0.25 + 0.25 * contrast :
            return ((1 - contrast ) / (1 + contrast)) * value 

        elif value > 0.75 - 0.25 * contrast :
            return (((1 - contrast) / (1 + contrast)) * (value - (3 - contrast) / 4)) + (3 + contrast) / 4

        else:
            return (((1 + contrast) / (1 - contrast)) * (value - (1 + contrast) / 4)) + (1 - contrast) / 4


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
    red = rgb.red / 255
    green = rgb.green / 255
    blue = rgb.blue / 255

    rgb.red = round(contrast_value(red, contrast) * 255)
    rgb.green = round(contrast_value(green, contrast) * 255)
    rgb.blue = round(contrast_value(blue, contrast) * 255)