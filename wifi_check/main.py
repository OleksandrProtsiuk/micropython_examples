import socket
import time
from boot import params, red, green


def blink(led):
    # helper for led confirmation
    i = 0
    while i < 3:
        led.on()
        time.sleep(0.5)
        led.off()
        i += 1
        time.sleep(0.5)


html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Page</title> </head>
    <body> <h1>ESP8266 Page</h1>
        <p><b>params of connect:</b></p>
         <p> %s <p>
    </body>
</html>
"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    blink(green)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break

    response = html % '<br>'.join(map(str, params))
    cl.send(response)
    blink(red)
    cl.close()
