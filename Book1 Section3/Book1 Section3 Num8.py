from AltinoLite import *

Open()
Steering(127)
go(400,400)
delay(6000)

steering(-127) 
delay(6000)

go(-300,-300)
delay(200)

go(0,0)
steering(0)
close()
