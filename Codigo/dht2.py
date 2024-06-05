from machine import Pin, PWM
import time
import dht
global temp

rele1=Pin(7,Pin.OUT)
d = dht.DHT11(machine.Pin(12))

temp = d.temperature()

while True:
    if temp > 25 :
        rele1.off()
        time.sleep_ms(500)
    else:
        rele1.on()
    print(temp)
