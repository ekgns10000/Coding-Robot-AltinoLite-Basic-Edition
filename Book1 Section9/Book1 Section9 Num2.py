from AltinoLite import*

Open()

while 1:
    if sensor.IR[3]>500:
        steering(127)
        go(300,300)
        delay(1000)
    else:
        go(0,0)
        steering(0)
        delay(1000)
        
Close()        
