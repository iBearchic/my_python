def evenQ(x):
    """
    >>> evenQ(5)
    False
    
    >>> evenQ(4)
    True
    
    >>> evenQ(1)
    False
    """
    return x%2==0

import doctest
doctest.testmod()
