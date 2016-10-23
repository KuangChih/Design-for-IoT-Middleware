import mraa
import pyupm_lpd8806
import time
nLED = 4
mystrip = pyupm_lpd8806.LPD8806(nLED, 7)

x=mraa.Gpio(2)
x.dir(mraa.DIR_IN)

while True:
mystrip.show()
#reset for some issue
value=x.read()
if value==0 : #Yes->Low
mystrip.setPixelColor(0, 10, 0, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(1, 10, 0, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(2, 10, 0, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(3, 10, 0, 0) #setPixelColor(id, r, g, b)
else : #No->High
mystrip.setPixelColor(0, 0, 10, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(1, 0, 10, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(2, 0, 10, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(3, 0, 10, 0) #setPixelColor(id, r, g, b)
mystrip.show()
time.sleep(1)
