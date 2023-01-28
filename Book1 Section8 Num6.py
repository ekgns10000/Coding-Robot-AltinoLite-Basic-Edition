from AltinoLite import*

Open()

while 1:
    a=1
    if sensor.CDS>=800:
        a=a<<7
        displayline(a,a,a,a,a,a,a,a)
        delay(1000)
    elif sensor.CDS>=700:
        a=a<<6
        displayline(a,a,a,a,a,a,a,a)
        delay(1000)
    elif sensor.CDS>=600:
        a=a<<5
        displayline(a,a,a,a,a,a,a,a)
        delay(1000)
    elif sensor.CDS>=500:
        a=a<<4
        displayline(a,a,a,a,a,a,a,a)
        delay(1000)
    elif sensor.CDS>=400:
        a=a<<3
        displayline(a,a,a,a,a,a,a,a)
        delay(1000)
    elif sensor.CDS>=300:
        a=a<<2
        displayline(a,a,a,a,a,a,a,a)
        delay(1000)
    elif sensor.CDS>=200:
        a=a<<1
        displayline(a,a,a,a,a,a,a,a)
        delay(1000)
    elif sensor.CDS>=100:
        displayline(a,a,a,a,a,a,a,a)
        delay(1000)
    else:
        displayline(0,0,0,0,0,0,0,0)
        delay(1000)
Close()
