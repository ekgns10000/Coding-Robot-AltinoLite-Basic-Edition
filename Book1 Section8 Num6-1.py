from AltinoLite import*

Open()

while 1:
    if sensor.CDS>=800:
        displayline(128,128,128,128,128,128,128,128)
        delay(1000)
    elif sensor.CDS>=700:
        displayline(64,64,64,64,64,64,64,64)
        delay(1000)
    elif sensor.CDS>=600:
        displayline(32,32,32,32,32,32,32,32)
        delay(1000)
    elif sensor.CDS>=500:
        displayline(16,16,16,16,16,16,16,16)
        delay(1000)
    elif sensor.CDS>=400:
        displayline(8,8,8,8,8,8,8,8)
        delay(1000)
    elif sensor.CDS>=300:
        displayline(4,4,4,4,4,4,4,4)
        delay(1000)
    elif sensor.CDS>=200:
        displayline(2,2,2,2,2,2,2,2)
        delay(1000)
    elif sensor.CDS>=100:
        displayline(1,1,1,1,1,1,1,1)
        delay(1000)
    else:
        displayline(0,0,0,0,0,0,0,0)
        delay(1000)
Close()
