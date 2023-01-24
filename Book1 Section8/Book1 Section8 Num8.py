from AltinoLite import*

Open()

while 1 :
    if sensor.CDS>=500 :
        sound(0)
    elif sensor.CDS>=450 :
        sound(37)
    elif sensor.CDS>=400 :
        sound(39)
    elif sensor.CDS>=350 :
        sound(41)
    elif sensor.CDS>=300 :
        sound(42)
    elif sensor.CDS>=250 :
        sound(44)
    elif sensor.CDS>=200 :
        sound(46)
    elif sensor.CDS>=150 :
        sound(48)
    elif sensor.CDS>=100 :
        sound(49)
    else :
        sound(51)

close()
    
