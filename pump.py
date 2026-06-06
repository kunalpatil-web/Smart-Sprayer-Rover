from machine import Pin
from time import sleep

# Relay connected to GPIO2
relay = Pin(2, Pin.OUT)

while True:
    relay.on()          # Relay ON
    print("Relay ON")
    sleep(5)

    relay.off()         # Relay OFF
    print("Relay OFF")
    sleep(5)