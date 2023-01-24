from AltinoLite import*

Open()
while 1:
    if sensor.CDS<1000:
        sound(37)
        delay(3000)

        sound(0)
        delay(1000)
    else:
        sound(0)
        delay(1000)
close()
