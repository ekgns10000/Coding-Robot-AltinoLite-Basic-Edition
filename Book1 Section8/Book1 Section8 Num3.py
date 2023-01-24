from AltinoLite import*

Open()
while 1:
    if sensor.CDS>100:
        go(300,300)
        delay(3000)

        go(0,0)
        delay(1000)
    else :
        go(0,0)
close()
