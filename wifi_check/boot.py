import network
import machine
import json

red = machine.Pin(5, machine.Pin.OUT)
yellow = machine.Pin(4, machine.Pin.OUT)
green = machine.Pin(0, machine.Pin.OUT)
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

with open('data.txt') as json_file:
    keys = json.load(json_file)
    essid = keys['essid']
    pwd = keys['pwd']
    print('Status OK...')


def do_connect(essid, password):
    yellow.on()
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(essid, password)
        while not sta_if.isconnected():
            pass
    yellow.off()
    green.on()


while True:
    red.on()
    if not button.value():
        print('Button pressed!\nCheck wifi...')
        do_connect(essid, pwd)
        red.off()
        break

params = network.WLAN(network.STA_IF).ifconfig()
print('network config:', params)
