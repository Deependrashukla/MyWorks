def last_name_first(n):
    """Returns: copy of <n> in form <last>, <first>

    >>> last_name_first("Sonika Thakral")
    'Thakral, Sonika'
    >>> last_name_first("Sonika    Thakral")
    'Thakral, Sonika'
    """
    
    end_first = n.find(' ')
    first = n[:end_first]
    last  = n[end_first+1:]
    
    return last+', '+first

'''
if __name__=='__main__':
    import doctest
    doctest.testmod()
'''