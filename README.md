redis-py-datamapper
===================

Version 0.1.0
--------------
Currently only RedisList is implemented. Dependent on redis-py. Make sure to start redis-server.

Not all native Python array functions implemented but most are. Check source.

All operations are atomic!

###How to Use
    
    mylist = RedisList(key)
    mylist.append('github', 'google', 'facebook')
    mylist.unshift('yo', 'secret')
    list(mylist) # ['secret', 'yo', 'github', 'google', 'facebook']
    
Bracket notation and assignment is fully supported:

    mylist[0] # 'secret'
    mylist[1:3] # 'yo', 'github'
    mylist[0] = 'pizza'
    list(mylist) # ['pizza', 'yo', 'github', 'google', 'facebook']

Python "in" is supported:

    'github' in mylist ### True
    for i, c in enumerate(mylist):
      print(i,c) 
      #0 'pizza'
      #1 'yo' 
      #...

Most other native array functions are supported - len, sort, pop, clear.

