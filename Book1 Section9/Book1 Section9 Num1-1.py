from AltinoLite import*

Open()

go(300,300)
while sensor.IR[2]>20:
    go(0,0)
    delay(3000)
        
Close()        
