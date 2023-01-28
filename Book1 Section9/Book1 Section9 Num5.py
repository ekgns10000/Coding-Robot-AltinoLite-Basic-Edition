from AltinoLite import*

Open()

while 1:
    if sensor.IR[4]>500:
        steering(127)
        delay(1000)
        
    elif sensor.IR[5]>500:
        steering(-127)
        delay(1000)
        
    else:
        steering(0)
        
Close()        
