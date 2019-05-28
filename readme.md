###**Some samples of micropython code for esp8266**

Short manual:

####**Getting started with MicroPython on the ESP8266**

1. Get the firmware
    http://micropython.org/download#esp8266

2. Deploy the firmware
    2.1  install esptools.py
    
        pip install esptool
    
    2.2  erase the flash of esp board
    
        esptool.py --port /dev/ttyUSB0 erase_flash
        
    2.3  deploy the new firmware
    
        esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 FIRMWARE_FILE-vx.x.x.bin
        

   After a fresh install and boot the device configures itself as a WiFi access point (AP) that you can connect to.
   ESSID: MicroPython-xxxxxx
   
   PASS:  micropythoN
   
   Details: http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware
   
   ------------------------------------
   
####**MicroPython REPL over the serial port**

For Linux users:

    picocom /dev/ttyUSB0 -b115200
    

Details:  http://docs.micropython.org/en/latest/esp8266/tutorial/repl.html

