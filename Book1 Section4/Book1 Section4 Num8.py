from AltinoLite import*

Open()

steering(127)
light(8)
go(300,300)
delay(3000)

go(0,0)
steering(0)
light(2)
delay(1000)

go(-300,-300)
light(2)
delay(2000)

go(0,0)
light(2)
delay(1000)

steering(127)
light(8)
go(300,300)
delay(1000)

steering(0)
light(0)
go(300,300)
delay(2000)

go(0,0)
close()
