from AltinoLite import*

Open()

while 1:
    go(300,300)
    light(12)
    delay(500)
    light(0)
    delay(500)
    if sensor.CD<100 :
        light(3)
        delay(3000)
        light(0)
        delay(1000)
Close()
