#Run this file once to initialize the persistent variables

from bookshelf import takeOffShelf, putOnShelf

putOnShelf("targetTemp", 24)
putOnShelf("lightOn", "0600")
putOnShelf("lightOff", "2230")
putOnShelf("priorFanOn", True)
putOnShelf("priorLightOn", True)
