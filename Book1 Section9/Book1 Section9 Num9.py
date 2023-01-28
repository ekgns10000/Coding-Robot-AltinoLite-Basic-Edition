from AltinoLite import*

Open()
a=53 #5
display(a)
delay(1000)

while 1:
    if a>47 and a<58:
        if sensor.IR[1]>300:
            a=a-1
            display(a)
            delay(1000)
        
        elif sensor.IR[3]>300:
            a=a+1
            display(a)
            delay(1000)
        
Close()        
