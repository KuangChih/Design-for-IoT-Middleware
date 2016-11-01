from twisted.internet import reactor
from udpwkpf import WuClass, Device
import sys
from udpwkpf_io_interface import *
import mraa
import pyupm_lpd8806
import time
nLED = 4
mystrip = pyupm_lpd8806.LPD8806(nLED, 7)

touch_pin = 2

if __name__ == "__main__":
    class Counter(WuClass):
        def __init__(self):
            WuClass.__init__(self)
            self.loadClass('Counter')
            current_value = 0
            x = mraa.Gpio(touch_pin)
            x.dir(mraa.DIR_IN)
            
        def update(self,obj,pID=None,val=None):
            try:
                value = x.read()
                if value == 1 :
                    if current_value < 4
                        current_value = current_value +1
                    else
                        current_value = 0
                print "Counter value: %d" % current_value
            except IOError:
                print "Error"

    class Light_Pattern(WuClass):
        def __init__(self):
            WuClass.__init__(self)
            self.loadClass('Light_Pattern')
            input_value = 0
            cnt = 0

        def update(self,obj,pID=None,val=None):
            try:
                if input_value == 0 :
                    mystrip.setPixelColor(0, 0, 0, 0) #setPixelColor(id, r, g, b)
                    mystrip.setPixelColor(1, 0, 0, 0) #setPixelColor(id, r, g, b)
                    mystrip.setPixelColor(2, 0, 0, 0) #setPixelColor(id, r, g, b)
                    mystrip.setPixelColor(3, 0, 0, 0) #setPixelColor(id, r, g, b)
                    mystrip.show()
                elif input_value == 1 :
                    mystrip.setPixelColor(0, 10, 0, 0) #setPixelColor(id, r, g, b)
                    mystrip.setPixelColor(1, 10, 0, 0) #setPixelColor(id, r, g, b)
                    mystrip.setPixelColor(2, 10, 0, 0) #setPixelColor(id, r, g, b)
                    mystrip.setPixelColor(3, 10, 0, 0) #setPixelColor(id, r, g, b)
                    mystrip.show()
                    time.sleep(0.2)
                elif input_value == 2 :
                    if cnt = 0 :
                        mystrip.setPixelColor(0, 0, 10, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(1, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(2, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(3, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.show()
                        time.sleep(0.2)
                        cnt = cnt +1
                    elif cnt = 1 :
                        mystrip.setPixelColor(0, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(1, 0, 10, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(2, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(3, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.show()
                        time.sleep(0.2)
                        cnt = cnt +1
                    elif cnt = 2 :
                        mystrip.setPixelColor(0, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(1, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(2, 0, 10, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(3, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.show()
                        time.sleep(0.2)
                        cnt = cnt +1
                    elif cnt = 3 :
                        mystrip.setPixelColor(0, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(1, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(2, 0, 0, 0) #setPixelColor(id, r, g, b)
                        mystrip.setPixelColor(3, 0, 10, 0) #setPixelColor(id, r, g, b)
                        mystrip.show()
                        time.sleep(0.2)
                        cnt = 0s
                print "Light_Pattern value: %d" % input_value
            except IOError:
                print "Error"

        class MyDevice(Device):
            def __init__(self,addr,localaddr):
                Device.__init__(self,addr,localaddr)
            def init(self):
                m1 = Counter()
                self.addClass(m1,0)
                self.obj_Counter = self.addObject(m1.ID)
                
                m2 = Light_Pattern()
                self.addClass(m2,0)
                self.obj_Light_Pattern = self.addObject(m2.ID)

        if len(sys.argv) <= 2:
            print 'python %s <gip> <dip>:<port>' % sys.argv[0]
            print '      <gip>: IP addrees of gateway'
            print '      <dip>: IP address of Python device'
            print '      <port>: An unique port number'
            print ' ex. python %s 192.168.4.7 127.0.0.1:3000' % sys.argv[0]
            sys.exit(-1)

        d = MyDevice(sys.argv[1],sys.argv[2])
        reactor.run()
        device_cleanup()

