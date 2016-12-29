from udpwkpf import WuClass, Device
import sys
from udpwkpf_io_interface import *
from twisted.internet import reactor

Light_R_Pin = 11
Light_G_Pin = 12
Light_B_Pin = 13
cnt = 0

if __name__ == "__main__":
    class Light_Actuator(WuClass):
        def __init__(self):
            WuClass.__init__(self)
            self.loadClass('Light_Actuator')
            self.light_R = pin_mode(Light_R_Pin, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.light_G = pin_mode(Light_G_Pin, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)
            self.light_B = pin_mode(Light_B_Pin, PIN_TYPE_DIGITAL, PIN_MODE_OUTPUT)

        def update(self,obj,pID=None,val=None):
            global cnt;
            try:
                if pID == 0:
                    if val == True:
                        if cnt % 2 == 0:
                            digital_write(self.light_R, 0)
                        else:
                            digital_write(self.light_R, 1)

                        if (cnt >> 1)%2 == 0:
                            digital_write(self.light_G, 0)
                        else:
                            digital_write(self.light_G, 1)

                        if (cnt >> 2)%2 == 0:
                            digital_write(self.light_B, 0)
                        else:
                            digital_write(self.light_B, 1)
                        if cnt < 7:
                            cnt = cnt + 1
                        else:
                            cnt = 0
                    print "Touched"
                else:
                        print "Not Touched"
            except IOError:
                print ("Error")

    class MyDevice(Device):
        def __init__(self,addr,localaddr):
            Device.__init__(self,addr,localaddr)

        def init(self):
            cls = Light_Actuator()
            self.addClass(cls,0)
            self.obj_light_actuator = self.addObject(cls.ID)

    if len(sys.argv) <= 2:
        print 'python %s <gip> <dip>:<port>' % sys.argv[0]
        print '      <gip>: IP addrees of gateway'
        print '      <dip>: IP address of Python device'
        print '      <port>: An unique port number'
        print ' ex. python %s 192.168.4.7 127.0.0.1:3000' % sys.argv[0]
        sys.exit(-1)

    d = MyDevice(sys.argv[1],sys.argv[2])
    reactor.run()
