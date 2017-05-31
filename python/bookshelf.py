import shelve



def putOnShelf(key, value):
    "Persist a variable to storage"
    filename = "/home/pi/python/bookshelf.txt"
    d = shelve.open(filename)
    d[key] = value
    d.close()

def takeOffShelf(key):
    "Retreive a variable from storage"
    filename = "/home/pi/python/bookshelf.txt"
    d = shelve.open(filename)
    value = d[key]
    return value
    d.close()
