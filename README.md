redis-py-datamapper
===================

Version 0.2.0
--------------
Dependencies: redis-py. 

Make sure to start redis-server.

Not all native Python List functions are implemented due to the nature of redis's native list, but most are. Check source and tests.

All Python Dict functions are implemented in redisdict. All operations are atomic.

Check the source and tests for complete usage. 


###How to Use
    
    >>>mylist = RedisList(key)
    >>>mylist.append('github', 'google', 'facebook')
    >>>mylist.unshift('yo', 'secret')
    >>>list(mylist)
    ['secret', 'yo', 'github', 'google', 'facebook']
    
Bracket notation and assignment is fully supported:

    >>>mylist[0]
    'secret'
    
    >>>mylist[1:3]
    [yo', 'github']
    
    >>>mylist[0] = 'pizza'
    >>>list(mylist)
    ['pizza', 'yo', 'github', 'google', 'facebook']

Python "in" is supported:

    >>>'github' in mylist ### True
    
    >>>for i, c in enumerate(mylist):
    >>> print(i,c) 
    0 'pizza'
    1 'yo' 
    2 'github'
    ...

Most other native array functions are supported - len, sort, pop, clear.
