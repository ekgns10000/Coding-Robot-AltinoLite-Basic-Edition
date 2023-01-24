from AltinoLite import*

Open()
while 1:
    if sensor.CDS<100:
        light(1)
        sound(37)
        go(300,300)
        delay(1000)
        
    else:
        light(0)
        sound(0)
        go(0,0)
        delay(1000)
Close()
