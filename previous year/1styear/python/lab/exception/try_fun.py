def fun(a):
    # if a < 4:
    #     try :
    #         b = a/(a-3)

    #     except UnboundLocalError:
    #         print('enter the value < 4')

    #     except ZeroDivisionError:
    #         print('value of b =', 'inf')

    try:
        if a < 4:
            b = a / (a - 3)

        print('Value of b = ', b)
    except UnboundLocalError:
        print('b does not exist.')

    except ZeroDivisionError:
        print('Value of b =', 'inf')

    except TypeError:
        print('Value of b', )

    except:
        print('Enter the value < 4')
  
    # print("Value of b = ", b)
a = fun('5')
# try :
#     a = fun(4)

# except UnboundLocalError:
#     print('enter the value < 4')

# except ZeroDivisionError:
#     print('value of b =', 'inf')