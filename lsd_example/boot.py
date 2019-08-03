from lsd_example.esp8266_i2c_lcd import I2cLcd
import machine

scl = machine.Pin(5)
sda = machine.Pin(4)

i2c = machine.I2C(scl=scl, sda=sda, freq=400000)
screen = i2c.scan()

lcd = I2cLcd(i2c, screen[0], 2, 16)
lcd.clear()
lcd.putstr('Hello World')
