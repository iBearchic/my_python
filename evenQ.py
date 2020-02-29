def evenQ(x):
    """
    >>> evenQ(2)
    True
    
    >>> evenQ(3)
    False
    """
    return x%2==0

import doctest
doctest.testmod()
