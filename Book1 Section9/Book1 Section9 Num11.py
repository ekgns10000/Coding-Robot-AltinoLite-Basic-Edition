from AltinoLite import*

Open()

while 1:
    if (sensor.CDS<200) or (sensor.IR[6]>100):
        go(300,300)
    
    else:
        go(0,0)
        
Close()        
