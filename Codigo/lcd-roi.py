from machine import Pin, ADC, I2C
import time
from esp8266_i2c_lcd import I2cLcd
import dht
global temp
global hum

ldr=ADC(Pin(28))
DEFAULT_I2C_ADDR = 0X27
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
d = dht.DHT11(machine.Pin(12))

temp = d.temperature()
hum = d.humidity()

while True:
    luz=ldr.read_u16()
    lcd.clear()
    lcd.move_to(0, 1)
    lcd.putstr(str ("Inverteis"))
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(str ("Roi"))
    lcd.move_to(0 , 1)
    lcd.putstr(str ("Tizon Counago"))
    time.sleep_ms(2000)
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(str ("Inverteis"))
    lcd.move_to(0 , 1)
    lcd.putstr(str ("IES Teis"))
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(str ("luz"))
    lcd.move_to(0 , 1)
    lcd.putstr(str (luz))
    time.sleep_ms(3000)
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(str ("Humedad:" + str(hum) + "%"))
    lcd.move_to(0, 1)
    lcd.putstr(str ("Temperatura:"+ str(temp) + chr (0xDF) + "C"))
    time.sleep_ms(3000)
    
    
  
    