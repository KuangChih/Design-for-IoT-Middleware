import mraa
import pyupm_lpd8806
import time
nLED = 4
mystrip = pyupm_lpd8806.LPD8806(nLED, 7)

fogSensor=mraa.Gpio(2)
fogSensor.dir(mraa.DIR_IN)

touchpad=mraa.Gpio(4)
touchpad.dir(mraa.DIR_IN)

def redlight():
mystrip.setPixelColor(0, 10, 0, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(1, 10, 0, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(2, 10, 0, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(3, 10, 0, 0) #setPixelColor(id, r, g, b)
return

def greenlight():
mystrip.setPixelColor(0, 0, 10, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(1, 0, 10, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(2, 0, 10, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(3, 0, 10, 0) #setPixelColor(id, r, g, b)
return

while True:
mystrip.show()
#reset for some issue
touchValue=touchpad.read()
fogValue=fogSensor.read()
if touchValue==0 && fogValue==0 :
greenlight()
elif touchValue==1 && fogValue==0 :
redlight()
time.sleep(5000)
elif touchValue==0 && fogValue==1 :
redlight()
elif touchValue==1 && fogValue==1 :
greenlight()
time.sleep(5000)
mystrip.show()
time.sleep(1)
