def lastF(name):
    assert type(name) == str
    assert name.count(' ') == 1, 'precondition violation'
    index = name.find(' ')
    last_name = name[index + 1 : ].strip()
    first_name = name[ : index]
    return f'{last_name}, {first_name}'


def lastF(name):
    assert type(name) == str, str(name) + ' is not a string.'
    # assert ' ' in name, name + ' is missing space.'
    # assert name.count(' ') == 1, str(name) + ' has too many spaces'
    index = name.find(' ')
    last_name = name[index + 1 : ].strip()
    first_name = name[ : index]
    return f'{last_name}, {first_name}'
    return last_name, first_name


def is_two_words(w):
    """
    Returns: True if w is 2 words sep by 1 or more spaces.

    A word is a string with no spaces.  So this means that 
    1. The first character is not a space (or empty)
    2. The last character is not a space (or empty)
    3. There is at least one space in the middle
    4. If there is more than one space, the spaces are adjacent
    Precondition: w is a str
    """
    assert not(w[0].isspace())
    assert not w[-1].isspace()
    assert ' ' in w
    

