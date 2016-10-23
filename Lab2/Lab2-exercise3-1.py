import mraa

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
    if value==1 :
        r.write(1)
        g.write(0)
        b.write(0)
    else :
        r.write(0)
        g.write(1)
        b.write(1)

