from machine import Pin, PWM
import time

rele2=Pin(8,Pin.OUT)
pulsador2=Pin(21,Pin.IN,Pin.PULL_UP)

v=0

while True:
    if pulsador2.value() == 0:
        v=v+1
        if v>1:
            v=0
    if v==0:
        rele2.off()
        time.sleep_ms(500)
        
    else:
        rele2.on()
        time.sleep_ms(500)
    print(v)