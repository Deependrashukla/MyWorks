""" 
Unit Test for Assignment A3

This module implements several test cases for a3.  It is incomplete.  You should look 
though this file for places to add tests.

SONAL KUMARI
21 st feburary,2023
""" 
import introcs
import a3


def test_complement():
    """
    Test function complement
    """
    print('Testing complement')
    
    # One test is really good enough here
    comp = a3.complement_rgb(introcs.RGB(250, 0, 71))
    introcs.assert_equals(255-250, comp.red)
    introcs.assert_equals(255-0,   comp.green)
    introcs.assert_equals(255-71,  comp.blue)
    
    # One more for good measure
    comp = a3.complement_rgb(introcs.RGB(128, 64, 255))
    introcs.assert_equals(255-128, comp.red)
    introcs.assert_equals(255-64,  comp.green)
    introcs.assert_equals(255-255, comp.blue)


def test_str5():

    """
    Test function str5
    """
    print('Testing str5')

    introcs.assert_equals('130.6',  a3.str5(130.59))
    introcs.assert_equals('130.5',  a3.str5(130.54))
    introcs.assert_equals('100.0',  a3.str5(100))
    introcs.assert_equals('100.6',  a3.str5(100.56))
    introcs.assert_equals('99.57',  a3.str5(99.566))
    introcs.assert_equals('99.99',  a3.str5(99.99))
    introcs.assert_equals('100.0',  a3.str5(99.995))
    introcs.assert_equals('22.00',  a3.str5(21.99575))
    introcs.assert_equals('21.99',  a3.str5(21.994))
    introcs.assert_equals('10.01',  a3.str5(10.013567))
    introcs.assert_equals('10.00',  a3.str5(10.000000005))
    introcs.assert_equals('10.00',  a3.str5(9.9999))
    introcs.assert_equals('9.999',  a3.str5(9.9993))
    introcs.assert_equals('1.355',  a3.str5(1.3546))
    introcs.assert_equals('1.354',  a3.str5(1.3544))
    introcs.assert_equals('0.046',  a3.str5(.0456))
    introcs.assert_equals('0.045',  a3.str5(.0453))
    introcs.assert_equals('0.006',  a3.str5(.0056))
    introcs.assert_equals('0.001',  a3.str5(.0013))
    introcs.assert_equals('0.000',  a3.str5(.0004))
    introcs.assert_equals('0.001',  a3.str5(.0009999))
    introcs.assert_equals('0.000',  a3.str5(1e-9))


def test_str5_color():
    """
    Test the str5 functions for cmyk and hsv.
    """
    print('Testing str5_cmyk and str5_hsv')
    
    # Tests for str5_cmyk
    # We need to make sure the coordinates round properly
    text = a3.str5_cmyk(introcs.CMYK(98.448, 25.362, 72.8, 1.0))
    introcs.assert_equals('(98.45, 25.36, 72.80, 1.000)',text)
    
    text = a3.str5_cmyk(introcs.CMYK(0.0, 1.5273, 100.0, 57.846))
    introcs.assert_equals('(0.000, 1.527, 100.0, 57.85)',text)

    text = a3.str5_hsv(introcs.HSV(270.0, 0.100009, 0.5989))
    introcs.assert_equals('(270.0, 0.100, 0.599)',text)

    text = a3.str5_hsv(introcs.HSV(98.448, 0.98906, 1.0000))
    introcs.assert_equals('(98.45, 0.989, 1.000)',text)
    


def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    print('Testing rgb_to_cmyk')
    
    # The function should guarantee accuracy to three decimal places
    rgb = introcs.RGB(255, 255, 255)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan, 3))
    introcs.assert_equals(0.0, round(cmyk.magenta, 3))
    introcs.assert_equals(0.0, round(cmyk.yellow, 3))
    introcs.assert_equals(0.0, round(cmyk.black, 3))
    
    rgb = introcs.RGB(0, 0, 0)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan, 3))
    introcs.assert_equals(0.0, round(cmyk.magenta, 3))
    introcs.assert_equals(0.0, round(cmyk.yellow, 3))
    introcs.assert_equals(100.0, round(cmyk.black, 3))
        
    rgb = introcs.RGB(217, 43, 164)
    cmyk = a3.rgb_to_cmyk(rgb)
    introcs.assert_equals(0.0, round(cmyk.cyan, 3))
    introcs.assert_equals(80.184, round(cmyk.magenta, 3))
    introcs.assert_equals(24.424, round(cmyk.yellow, 3))
    introcs.assert_equals(14.902, round(cmyk.black, 3))


def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    print('Testing cmyk_to_rgb')

    # case with all values as 0.0 
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, round(rgb.red))
    introcs.assert_equals(255, round(rgb.green))
    introcs.assert_equals(255, round(rgb.blue))

    # case with all diffrent values. 
    cmyk = introcs.CMYK(78.0, 90.0, 67.0, 23.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(43, round(rgb.red))
    introcs.assert_equals(20, round(rgb.green))
    introcs.assert_equals(65, round(rgb.blue))

    # case with all values as 100.0
    cmyk = introcs.CMYK(100.0, 100.0, 100.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, round(rgb.red))
    introcs.assert_equals(0, round(rgb.green))
    introcs.assert_equals(0, round(rgb.blue))

    #case with magenta = 100.0 and cyan = yellow = black = 0.0 
    cmyk = introcs.CMYK(0.0, 100.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, round(rgb.red))
    introcs.assert_equals(0, round(rgb.green))
    introcs.assert_equals(255, round(rgb.blue))

    #case with just reverse of the above case.
    #magenta = 0.0 and cyan = yellow = black = 100.0 
    cmyk = introcs.CMYK(100.0, 0.0, 100.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, round(rgb.red))
    introcs.assert_equals(0, round(rgb.green))
    introcs.assert_equals(0, round(rgb.blue))

    #case with black = 100.0 and cyan = magneta = yellow = 100.0
    cmyk = introcs.CMYK(0.0, 0.0, 0.0, 100.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, round(rgb.red))
    introcs.assert_equals(0, round(rgb.green))
    introcs.assert_equals(0, round(rgb.blue))

    #case with just reverse of the above case.
    #black = 0.0 and cyan = magneta = yellow = 100.0
    cmyk = introcs.CMYK(100.0, 100.0, 100.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, round(rgb.red))
    introcs.assert_equals(0, round(rgb.green))
    introcs.assert_equals(0, round(rgb.blue))


    cmyk = introcs.CMYK(100.0, 100.0, 0.0, 0.0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, round(rgb.red))
    introcs.assert_equals(0, round(rgb.green))
    introcs.assert_equals(255, round(rgb.blue))




def test_rgb_to_hsv():
    """
    Test translation function rgb_to_hsv
    """
    print('Testing rgb_to_hsv')
    

    rgb=introcs.RGB(0, 0, 0)
    hsv=a3.rgb_to_hsv(rgb)
    introcs.assert_equals(0.0, round(hsv.hue, 3)) 
    introcs.assert_equals(0.0, round(hsv.saturation, 3))
    introcs.assert_equals(0.0, round(hsv.value, 3))

    rgb=introcs.RGB(255, 255, 255)
    hsv=a3.rgb_to_hsv(rgb)
    introcs.assert_equals(0.0, round(hsv.hue, 3)) 
    introcs.assert_equals(0.0, round(hsv.saturation, 3))
    introcs.assert_equals(1.0, round(hsv.value, 3))

    rgb=introcs.RGB(108, 162, 101)
    hsv=a3.rgb_to_hsv(rgb)
    introcs.assert_equals(113.115, round(hsv.hue, 3)) 
    introcs.assert_equals(0.377, round(hsv.saturation, 3))
    introcs.assert_equals(0.635, round(hsv.value, 3))



def test_hsv_to_rgb():
    """
    Test translation function hsv_to_rgb
    """
    print('Testing hsv_to_rgb')
    
    hsv=introcs.HSV(0.0, 0.0, 0.0)
    rgb=a3.hsv_to_rgb(hsv)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    hsv=introcs.HSV(359.0, 0.987, 0.001)
    rgb=a3.hsv_to_rgb(hsv)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    hsv=introcs.HSV(359.0, 0.001, 0.987)
    rgb=a3.hsv_to_rgb(hsv)
    introcs.assert_equals(252, rgb.red)
    introcs.assert_equals(251, rgb.green)
    introcs.assert_equals(251, rgb.blue)

    hsv=introcs.HSV(359.0, 0.001, 0.001)
    rgb=a3.hsv_to_rgb(hsv)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    hsv=introcs.HSV(359.0, 0.987, 0.987)
    rgb=a3.hsv_to_rgb(hsv)
    introcs.assert_equals(252, rgb.red)
    introcs.assert_equals(3, rgb.green)
    introcs.assert_equals(7, rgb.blue)


    hsv=introcs.HSV(0.9, 0.001, 0.987)
    rgb=a3.hsv_to_rgb(hsv)
    rgb=a3.hsv_to_rgb(hsv)
    introcs.assert_equals(252, rgb.red)
    introcs.assert_equals(251, rgb.green)
    introcs.assert_equals(251, rgb.blue)

    hsv=introcs.HSV(0.9, 0.987, 0.001)
    rgb=a3.hsv_to_rgb(hsv)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    hsv=introcs.HSV(0.9, 0.987, 0.987)
    rgb=a3.hsv_to_rgb(hsv)
    introcs.assert_equals(252, rgb.red)
    introcs.assert_equals(7, rgb.green)
    introcs.assert_equals(3, rgb.blue)

    hsv=introcs.HSV(0.9, 0.001, 0.001)
    rgb=a3.hsv_to_rgb(hsv)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)


def test_contrast_value():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_value')
    
    # contrast == -1.0 (extreme)
    result = a3.contrast_value(0.0, -1.0)
    introcs.assert_floats_equal(0.5, result)
    
    result = a3.contrast_value(1.0, -1.0)
    introcs.assert_floats_equal(0.5, result)
    
    # contrast < 0, bottom part of sawtooth
    result = a3.contrast_value(0.1, -0.5)
    introcs.assert_floats_equal(0.3, result)
    
    # contrast < 0, middle of sawtooth
    result = a3.contrast_value(0.4, -0.4)
    introcs.assert_floats_equal(0.4571429, result)
    
    # contrast < 0, upper part of sawtooth
    result = a3.contrast_value(0.9, -0.3)
    introcs.assert_floats_equal(0.8142857, result)
    
    # contrast == 0.0, bottom part of sawtooth
    result = a3.contrast_value(0.1, 0.0)
    introcs.assert_floats_equal(0.1, result)
    
    # contrast == 0, middle of sawtooth
    result = a3.contrast_value(0.6, 0.0)
    introcs.assert_floats_equal(0.6, result)
    
    # contrast == 0.0, upper part of sawtooth
    result = a3.contrast_value(0.9, 0.0)
    introcs.assert_floats_equal(0.9, result)
    
    # contrast > 0, bottom part of sawtooth
    result = a3.contrast_value(0.1, 0.3)
    introcs.assert_floats_equal(0.05384615, result)
    
    # contrast > 0, middle of sawtooth
    result = a3.contrast_value(0.4, 0.5)
    introcs.assert_floats_equal(0.2, result)
    
    # contrast > 0, upper part of sawtooth
    result = a3.contrast_value(0.9, 0.4)
    introcs.assert_floats_equal(0.95714286, result)
    
    # contrast == 1.0 (extreme)
    result = a3.contrast_value(0.2, 1.0)
    introcs.assert_floats_equal(0.0, result)
    
    result = a3.contrast_value(0.6, 1.0)
    introcs.assert_floats_equal(1.0, result)


def test_contrast_rgb():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_rgb')
    
    # Negative contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb, -0.4)
    introcs.assert_equals(220, rgb.red)
    introcs.assert_equals(35, rgb.green)
    introcs.assert_equals(123, rgb.blue)
    
    # zero contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb, 0.0)
    introcs.assert_equals(240, rgb.red)
    introcs.assert_equals(15, rgb.green)
    introcs.assert_equals(118, rgb.blue)
    

    # positive contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb, 0.4)
    introcs.assert_equals(249, rgb.red)
    introcs.assert_equals(6, rgb.green)
    introcs.assert_equals(105, rgb.blue)


# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == '__main__':
    test_complement()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    test_contrast_value()
    test_contrast_rgb()
    print('Module a3 passed all tests.')
