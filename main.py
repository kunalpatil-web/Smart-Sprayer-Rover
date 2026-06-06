import network
import socket
from machine import Pin, time_pulse_us
from time import sleep, sleep_us

# =====================================
# FRONT MOTOR DRIVER
# =====================================

f_in1 = Pin(23, Pin.OUT)
f_in2 = Pin(22, Pin.OUT)
f_in3 = Pin(21, Pin.OUT)
f_in4 = Pin(19, Pin.OUT)

# =====================================
# REAR MOTOR DRIVER
# =====================================

r_in1 = Pin(18, Pin.OUT)
r_in2 = Pin(5, Pin.OUT)
r_in3 = Pin(17, Pin.OUT)
r_in4 = Pin(16, Pin.OUT)

# =====================================
# PUMP RELAY
# =====================================

pump = Pin(2, Pin.OUT)

# Relay OFF initially
pump.value(1)

# =====================================
# ULTRASONIC SENSOR
# =====================================

trig = Pin(23, Pin.OUT)
echo = Pin(22, Pin.IN)

# =====================================
# AI RESULT VARIABLE
# =====================================

ai_result = "NO DETECTION"

# =====================================
# MOTOR FUNCTIONS
# =====================================

def stop():

    pins = [
        f_in1, f_in2, f_in3, f_in4,
        r_in1, r_in2, r_in3, r_in4
    ]

    for pin in pins:
        pin.value(0)

def forward():

    stop()

    f_in1.value(1)
    f_in2.value(0)

    f_in3.value(1)
    f_in4.value(0)

    r_in1.value(1)
    r_in2.value(0)

    r_in3.value(1)
    r_in4.value(0)

def backward():

    stop()

    f_in1.value(0)
    f_in2.value(1)

    f_in3.value(0)
    f_in4.value(1)

    r_in1.value(0)
    r_in2.value(1)

    r_in3.value(0)
    r_in4.value(1)

def left():

    stop()

    f_in1.value(0)
    f_in2.value(1)

    f_in3.value(1)
    f_in4.value(0)

    r_in1.value(0)
    r_in2.value(1)

    r_in3.value(1)
    r_in4.value(0)

def right():

    stop()

    f_in1.value(1)
    f_in2.value(0)

    f_in3.value(0)
    f_in4.value(1)

    r_in1.value(1)
    r_in2.value(0)

    r_in3.value(0)
    r_in4.value(1)

# =====================================
# PUMP FUNCTIONS
# =====================================

def pump_on():

    pump.value(0)

    print("Pump ON")

def pump_off():

    pump.value(1)

    print("Pump OFF")

# =====================================
# DISTANCE FUNCTION
# =====================================

def get_distance():

    trig.off()
    sleep_us(2)

    trig.on()
    sleep_us(10)

    trig.off()

    try:

        duration = time_pulse_us(echo, 1, 30000)

        distance = (duration * 0.0343) / 2

        return round(distance, 2)

    except:

        return 0

# =====================================
# WIFI ACCESS POINT
# =====================================

ssid = "ESP32_CAR"
password = "12345678"

ap = network.WLAN(network.AP_IF)

ap.active(True)

ap.config(essid=ssid, password=password)

while not ap.active():
    pass

print("WiFi Name:", ssid)
print("IP Address:", ap.ifconfig()[0])

# =====================================
# SERVER
# =====================================

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()

server.bind(addr)

server.listen(5)

print("Server Running...")

# =====================================
# MAIN LOOP
# =====================================

while True:

    cl, addr = server.accept()

    request = cl.recv(1024).decode()

    print(request)

    global ai_result

    # =================================
    # CAR CONTROL
    # =================================

    if 'cmd=forward' in request:
        forward()

    elif 'cmd=backward' in request:
        backward()

    elif 'cmd=left' in request:
        left()

    elif 'cmd=right' in request:
        right()

    elif 'cmd=stop' in request:
        stop()

    # =================================
    # PUMP MANUAL CONTROL
    # =================================

    elif 'cmd=pump_on' in request:
        pump_on()

    elif 'cmd=pump_off' in request:
        pump_off()

    # =================================
    # AI CONTROL
    # =================================

    elif 'cmd=healthy' in request:

        ai_result = "HEALTHY"

        pump_off()

    elif 'cmd=unhealthy' in request:

        ai_result = "UNHEALTHY"

        pump_on()

    # =================================
    # DISTANCE
    # =================================

    distance = get_distance()

    # =================================
    # HTML WEBPAGE
    # =================================

    html = """<!DOCTYPE html>

<html>

<head>

<title>AI AGRICULTURE ROVER</title>

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

body{
    text-align:center;
    font-family:Arial;
    background:#dff0d8;
}

button{
    width:140px;
    height:60px;
    font-size:18px;
    margin:6px;
    border:none;
    border-radius:10px;
    background:#27ae60;
    color:white;
}

.distance{
    font-size:28px;
    color:red;
    margin:20px;
}

.ai{
    font-size:35px;
    color:blue;
    margin:20px;
}

</style>

</head>

<body>

<h1>AI AGRICULTURE ROVER</h1>

<div class="distance">

Distance: """ + str(distance) + """ cm

</div>

<h2>VEHICLE CONTROL</h2>

<button onclick="send('forward')">Forward</button>

<br><br>

<button onclick="send('left')">Left</button>

<button onclick="send('stop')">Stop</button>

<button onclick="send('right')">Right</button>

<br><br>

<button onclick="send('backward')">Backward</button>

<h2>PUMP CONTROL</h2>

<button onclick="send('pump_on')">Pump ON</button>

<button onclick="send('pump_off')">Pump OFF</button>

<h2>AI RESULT</h2>

<div class="ai">

""" + ai_result + """

</div>

<script>

function send(cmd)
{
    fetch('/?cmd=' + cmd);
}

</script>

</body>

</html>
"""

    # =================================
    # SEND RESPONSE
    # =================================

    cl.send('HTTP/1.1 200 OK\r\n')
    cl.send('Content-Type: text/html\r\n')
    cl.send('Connection: close\r\n\r\n')

    cl.sendall(html)

    cl.close()