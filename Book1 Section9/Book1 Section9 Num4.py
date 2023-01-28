from AltinoLite import*

Open()

while 1:
    if sensor.IR[2]<10:
        go(350,350)

    elif sensor.IR[2]>=30:
        go(0,0)
        sound(0)
        
    elif sensor.IR[2]>=10:
        go(300,300)
        sound(47)
 
Close()        
