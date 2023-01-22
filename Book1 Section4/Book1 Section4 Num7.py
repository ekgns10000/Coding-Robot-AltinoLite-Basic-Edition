from AltinoLite import *

Open()

Steering(127)
light(8)
go(400,400)
delay(6000)

steering(-127)
light(4)
delay(6000)

go(0,0)
steering(0)
light(2)
delay(1000)

light(0)

close()
