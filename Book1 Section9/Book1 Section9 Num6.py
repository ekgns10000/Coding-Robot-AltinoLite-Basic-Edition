from AltinoLite import*

Open()

while 1:
    if sensor.IR[1]>500:
        sound(37)
        delay(1000)
        
    elif sensor.IR[2]>500:
        sound(39)
        delay(1000)

    elif sensor.IR[3]>500:
        sound(41)
        delay(1000)

    elif sensor.IR[4]>500:
        sound(42)
        delay(1000)

    elif sensor.IR[5]>500:
        sound(44)
        delay(1000)

    elif sensor.IR[6]>500:
        sound(46)
        delay(1000)
      
    else:
        sound(0)
        
Close()        
