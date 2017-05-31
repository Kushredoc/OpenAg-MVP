from datetime import tzinfo, datetime

#Output to file
def logData(name, value, comment=''):
    f = open('/home/pi/Documents/OpenAg-MVP/data.txt', 'a')
#    s ='{:%Y-%m-%d %H:%M:%S}'.format(datetime.utcnow()) + ", Temperature, " + str(cTemp) + ",\n"
    s= '{:%Y-%m-%d %H:%M:%S}'.format(datetime.utcnow()) + ", " + name + ", " + value + "," + comment + "\n"
    print(s)
    f.write(s)
    f.close()
