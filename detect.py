import cv2
import requests
import numpy as np

ESP32_IP = "192.168.4.1"

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(3, 320)
cap.set(4, 240)

cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Resize image
    img = cv2.resize(frame, (128,128))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calculate brightness
    brightness = np.mean(gray)

    # SIMPLE AI LOGIC
    # Dark leaf = unhealthy
    # Bright leaf = healthy

    if brightness < 100:

        result = "UNHEALTHY"

        try:
            requests.get(
                f"http://{ESP32_IP}/?cmd=unhealthy"
            )
        except:
            pass

    else:

        result = "HEALTHY"

        try:
            requests.get(
                f"http://{ESP32_IP}/?cmd=healthy"
            )
        except:
            pass

    cv2.putText(
        frame,
        result,
        (20,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("Leaf Detection", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()