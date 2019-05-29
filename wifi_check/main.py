import socket
import time
from boot import params, red, green


def blink(led):
    i = 0
    while i < 3:
        led.on()
        time.sleep(1)
        led.off()
        i += 1
        time.sleep(1)


html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <p>params of connect: <p>
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
    row = [str(params)]
    response = html % '\n'.join(row)
    cl.send(response)
    blink(red)
    cl.close()
