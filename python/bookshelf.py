#!/usr/bin/python

#routines to persist variables between executions
#data is stored in a file
#protocol must be stated due to conflicts between Python 2 and 3
import shelve



def putOnShelf(key, value):
    "Persist a variable to storage"
    filename = "/home/pi/python/bookshelf.db"
    d = shelve.open(filename, protocol= 2)
    d[key] = value
    d.close()

def takeOffShelf(key):
    "Retreive a variable from storage"
    filename = "/home/pi/python/bookshelf.db"
    d = shelve.open(filename, protocol= 2)
    value = d[key]
    return value
    d.close()
