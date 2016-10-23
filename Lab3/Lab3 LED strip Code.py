import mraa
import pyupm_lpd8806
import time
nLED = 4
mystrip = pyupm_lpd8806.LPD8806(nLED, 7)
while True:
mystrip.show()
#reset for some issue
mystrip.setPixelColor(0, 10, 0, 0) #setPixelColor(id, r, g, b)
mystrip.setPixelColor(1, 0, 10, 0) #r,g,b value is from 0 to 255
mystrip.setPixelColor(2, 0, 0, 10) #But, values larger than 20
mystrip.setPixelColor(3, 10, 10, 10) #are almost same.
mystrip.show()
time.sleep(1)
