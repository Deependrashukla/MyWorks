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
    X = value 
    C = contrast
    if C == 1 :
        if X >= 0.5 :
            return 1 

        else:
            return 0 
    else:
        if X < 0.25 + 0.25 * C :
            return ((1 - C ) / (1 + C)) * X 

        elif X > 0.75 - 0.25 * C :
            return (((1 - C) / (1 + C)) * (X - (3 - C) / 4)) + (3 + C) / 4

        else:
            return (((1 + C) / (1 - C)) * (X - (1 + C) / 4)) + (1 - C) / 4

print(contrast_value(240/255,0.4)*255)
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
    R = rgb.red / 255
    G = rgb.green / 255
    B = rgb.blue / 255

    rgb.red = round(contrast_value(R, contrast) * 255)
    rgb.green = round(contrast_value(G, contrast) * 255)
    rgb.blue = round(contrast_value(B, contrast) * 255)

print()


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
        num_str = str(value)
        pos = num_str.find('.')
        round_value = round(value, 4 - pos)
        str_round_value = str(round_value)
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
print(str5(0.01))