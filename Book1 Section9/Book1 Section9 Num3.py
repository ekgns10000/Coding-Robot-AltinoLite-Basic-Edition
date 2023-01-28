from AltinoLite import*

Open()

while 1:
    if sensor.IR[4]>500 and sensor.IR[5]>500:
        sound(37)
        delay(1000)
    else:
        sound(0)
        delay(1000)
Close()        
