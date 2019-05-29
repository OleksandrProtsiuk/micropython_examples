import network
import machine

red = machine.Pin(5, machine.Pin.OUT)
yellow = machine.Pin(4, machine.Pin.OUT)
green = machine.Pin(0, machine.Pin.OUT)

wifi = 'WIFI ESSID'
pwd = 'WIFI PASS'


def do_connect(essid, password):
    red.on()
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        yellow.on()
        sta_if.active(True)
        sta_if.connect(essid, password)
        while not sta_if.isconnected():
            pass
    yellow.off()
    green.on()
    print('network config:', sta_if.ifconfig())


do_connect(wifi, pwd)
params = network.WLAN(network.STA_IF).ifconfig()
