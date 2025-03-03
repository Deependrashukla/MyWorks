import introcs
import math
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
    if '.' in str(float(value)):
        num_str = str(value)
        pos = num_str.find('.')
        round_value = round(value, 4 - pos)
        # print(round_value)
        str_round_value = str(round_value)
        # print(str_round_value)
        if len(str_round_value) == 5:
            return str_round_value
        else:
            return str_round_value + '0' * (5 - len(str_round_value)) 


    else:
        if not 'e' in str(value):
            num_str = str(value)
            len_value = len(num_str)
            value_str = num_str + '.' + (4 - len_value) * '0'
            return value_str
        else:
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
    return str((str5(cmyk.cyan), str5(cmyk.magenta), str5(cmyk.yellow), str5(cmyk.black)))
    # return(str5(CMYK.cyan), str5(CMYK.magenta), str5(CMYK.yellow), str5(CMYK.black))
print(str5_cmyk())

# print(str5(0.00000006))
# print("{:.2f}".format())
# string_value = str("{:.{}f}".format(value, decimal_places)
# def rgb_to_cmyk(rgb):
#     """
#     Returns a CMYK object equivalent to rgb, with the most black possible.
    
#     Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
#     Parameter rgb: the color to convert to a CMYK object
#     Precondition: rgb is an RGB object
#     """
#     # The RGB numbers are in the range 0..255.
#     # Change them to the range 0..1 by dividing them by 255.0.
#     R_new = rgb.red / 255
#     G_new = rgb.green / 255
#     B_new = rgb.blue / 255

#     K = (1 - max(R_new, G_new, B_new))  #black color.
#     C = (1 - R_new - K) / (1 - K)       #cyan.
#     M = (1 - G_new - K) / (1 - K)       #Magenta.
#     Y = (1 - B_new - K) / (1 - K)       #yellow.
#     if rgb.red == 0 and rgb.green == 0 and rgb.blue == 0:
#         introcs.cmyk.cyan = 0
#         introcs.cmyk.magenta = 0 
#         introcs.cmyk.yellow = 0 
#         introcs.cmyk.black = 0
#         return introcs.cmyk 

# print(rgb_to_cmyk())




















    