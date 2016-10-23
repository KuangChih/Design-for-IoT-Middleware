import mraa

try:
    x = mraa.Aio(0)
    print (x.read())
except:
    print ("Are you sure you have an ADC?")


x = mraa.Gpio(2)
x.dir(mraa.DIR_IN)

b = mraa.Gpio(13)
b.dir(mraa.DIR_OUT)
g = mraa.Gpio(12)
g.dir(mraa.DIR_OUT)
r = mraa.Gpio(11)
r.dir(mraa.DIR_OUT)

while True :
    value = x.read()
    if value<0.25 :
        r.write(0)
        g.write(0)
        b.write(0)
    elif value<0.5 :
        r.write(1)
        g.write(0)
        b.write(0)
    elif value<0.75 :
        r.write(1)
        g.write(1)
        b.write(0)
    elif value<1 :
        r.write(1)
        g.write(1)
        b.write(1)


