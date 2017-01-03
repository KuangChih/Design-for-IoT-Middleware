from twisted.internet import reactor
from udpwkpf import WuClass, Device
import sys
from udpwkpf_io_interface import *
import pyupm_lpd8806

nLED = 4

Touch_Pad_Pin = 7

if __name__ == "__main__":
    class Counter(WuClass):
        def __init__(self):
            WuClass.__init__(self)
            self.loadClass('Counter')
            self.touch_pad_gpio = pin_mode(Touch_Pad_Pin, PIN_TYPE_DIGITAL, PIN_MODE_INPUT)
            self.previous_state = 0
            print "Touch Pad init success"

        def update(self, obj, pID=None, val=None):
            try:
                input_value = digital_read(self.touch_pad_gpio)
                if self.previous_state == input_value:
                    return
                self.previous_state = input_value
                current_value = obj.getProperty(0)
                if input_value == 1:
                    if current_value == 3:
                        current_value = 0
                    else:
                        current_value += 1
                    print "Touch Pad input: ", input_value, " Current Value: ", current_value
                    obj.setProperty(0, current_value)
            except IOError:
                print "Touch Pad IOError"

    class LED_Pattern(WuClass):
        def __init__(self):
            WuClass.__init__(self)
            self.loadClass('LED_Pattern')
            self.mystripe = pyupm_lpd8806.LPD8806(nLED, 7)
            self.led_case = 0
            self.led_two_hz = False
            self.led_step_count = 0
            print "LED stripe init success"

        def update(self, obj, pID=None, val=None):
            try:
                if pID == 0:
                    self.led_case = val
                    self.led_step_count = 0

                if self.led_case == 0:
                    self.mystripe.setPixelColor(0, 0, 0, 0)
                    self.mystripe.setPixelColor(1, 0, 0, 0)
                    self.mystripe.setPixelColor(2, 0, 0, 0)
                    self.mystripe.setPixelColor(3, 0, 0, 0)
                elif self.led_case == 1:
                    if self.led_step_count == 0 or self.led_step_count == 2:
                        self.mystripe.setPixelColor(0, 20, 0, 0)
                        self.mystripe.setPixelColor(1, 20, 0, 0)
                        self.mystripe.setPixelColor(2, 20, 0, 0)
                        self.mystripe.setPixelColor(3, 20, 0, 0)
                    else:
                        self.mystripe.setPixelColor(0, 0, 0, 0)
                        self.mystripe.setPixelColor(1, 0, 0, 0)
                        self.mystripe.setPixelColor(2, 0, 0, 0)
                        self.mystripe.setPixelColor(3, 0, 0, 0)
                elif self.led_case == 2:
                    if self.led_step_count == 0:
                        self.mystripe.setPixelColor(0, 20, 20, 0)
                        self.mystripe.setPixelColor(1, 0, 0, 0)
                        self.mystripe.setPixelColor(2, 0, 0, 0)
                        self.mystripe.setPixelColor(3, 0, 0, 0)
                    elif self.led_step_count == 1:
                        self.mystripe.setPixelColor(0, 0, 0, 0)
                        self.mystripe.setPixelColor(1, 20, 20, 0)
                        self.mystripe.setPixelColor(2, 0, 0, 0)
                        self.mystripe.setPixelColor(3, 0, 0, 0)
                    elif self.led_step_count == 2:
                        self.mystripe.setPixelColor(0, 0, 0, 0)
                        self.mystripe.setPixelColor(1, 0, 0, 0)
                        self.mystripe.setPixelColor(2, 20, 20, 0)
                        self.mystripe.setPixelColor(3, 0, 0, 0)
                    elif self.led_step_count == 3:
                        self.mystripe.setPixelColor(0, 0, 0, 0)
                        self.mystripe.setPixelColor(1, 0, 0, 0)
                        self.mystripe.setPixelColor(2, 0, 0, 0)
                        self.mystripe.setPixelColor(3, 20, 20, 0)
                elif self.led_case == 3:
                    if self.led_step_count == 0:
                        self.mystripe.setPixelColor(0, 20, 20, 0)
                        self.mystripe.setPixelColor(1, 0, 0, 0)
                        self.mystripe.setPixelColor(2, 0, 0, 0)
                        self.mystripe.setPixelColor(3, 0, 0, 0)
                    elif self.led_step_count == 1:
                        self.mystripe.setPixelColor(0, 0, 0, 0)
                        self.mystripe.setPixelColor(1, 0, 0, 0)
                        self.mystripe.setPixelColor(2, 0, 0, 0)
                        self.mystripe.setPixelColor(3, 20, 20, 0)
                    elif self.led_step_count == 2:
                        self.mystripe.setPixelColor(0, 0, 0, 0)
                        self.mystripe.setPixelColor(1, 0, 0, 0)
                        self.mystripe.setPixelColor(2, 20, 20, 0)
                        self.mystripe.setPixelColor(3, 0, 0, 0)
                    elif self.led_step_count == 3:
                        self.mystripe.setPixelColor(0, 0, 0, 0)
                        self.mystripe.setPixelColor(1, 20, 20, 0)
                        self.mystripe.setPixelColor(2, 0, 0, 0)
                        self.mystripe.setPixelColor(3, 0, 0, 0)

                self.mystripe.show()
                if self.led_step_count == 3:
                    self.led_step_count = 0
                else:
                    self.led_step_count += 1

                if self.led_case == 1:
                    obj.setProperty(1, 250)
                else:
                    obj.setProperty(1, 200)

            except IOError:
                print "LED stripe IOError"

    class MyDevice(Device):
        def __init__(self, addr, localaddr):
            Device.__init__(self, addr, localaddr)

        def init(self):
            led_stripe = LED_Pattern()
            self.addClass(led_stripe, 0)
            self.obj_led_pattern = self.addObject(led_stripe.ID)

            counter = Counter()
            self.addClass(counter, 0)
            self.obj_counter = self.addObject(counter.ID)

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
