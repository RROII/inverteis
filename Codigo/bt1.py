from machine import Pin, PWM
import time

rele1=Pin(7,Pin.OUT)
pulsador1=Pin(20,Pin.IN,Pin.PULL_UP)

c=0

while True:
    if pulsador1.value() == 0:
        c=c+1
        if c>1:
            c=0
    if c==0:
        rele1.off()
        time.sleep_ms(500)
        
    else:
        rele1.on()
        time.sleep_ms(500)
    print(c)