from AltinoLite import*

Open()

while 1:
    if sensor.IR[1]>500:
        steering(-127)
        go(-300,-300)
        delay(1000)
        
    elif sensor.IR[2]>500:
        steering(0)
        go(-300,-300)
        delay(1000)

    elif sensor.IR[3]>500:
        steering(127)
        go(-300,-300)
        delay(1000)

    else:
        steering(0)
        go(0,0)
        
Close()        
