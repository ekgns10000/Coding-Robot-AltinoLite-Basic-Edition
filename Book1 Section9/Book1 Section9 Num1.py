from AltinoLite import*

Open()

while 1:
    go(300,300)
    if sensor.IR[2]>=20:
        go(0,0)
        delay(3000)
        
Close()        
