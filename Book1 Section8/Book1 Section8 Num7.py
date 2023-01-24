from AltinoLite import*

Open()

while 1 :
    if sensor.CDS>=900 :
        display('9')
    elif sensor.CDS>=800 :
        display('8')
    elif sensor.CDS>=700 :
        display('7')
    elif sensor.CDS>=600 :
        display('6')
    elif sensor.CDS>=500 :
        display('5')
    elif sensor.CDS>=400 :
        display('4')
    elif sensor.CDS>=300 :
        display('3')
    elif sensor.CDS>=200 :
        display('2')
    elif sensor.CDS>=100 :
        display('1')
    else :
        display('0')

close()
    
