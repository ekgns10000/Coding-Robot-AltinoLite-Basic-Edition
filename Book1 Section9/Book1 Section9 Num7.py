from AltinoLite import*

Open()

while 1:
    if sensor.IR[1]>500:
        light(4)
        delay(1000)
        
    elif sensor.IR[2]>500:
        light(1)
        delay(1000)

    elif sensor.IR[3]>500:
        light(2)
        delay(1000)

    else:
        light(0)
        
Close()        
