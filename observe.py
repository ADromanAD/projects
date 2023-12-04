# Подключение библиотек
import cv2
import numpy as np
from adafruit_servokit import ServoKit


# Подключение серводвигателей и установка начального положения серводвигателя
kit = ServoKit(channels=16)
pan = 90
tilt = 45
kit.servo[0].angle = pan
kit.servo[1].angle = tilt

dispW = 640
dispH = 480
flip = 2
# Подключение камеры
cam = cv2.VideoCapture(0)
# Подключение классификатора для распознавания объекта
car_cascade = cv2.CascadeClassifier("C:\\Users\\User\\source\\repos\\PythonApplication2\\cars.xml")

width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

while True:
    # Получение кадра
    ret, frame = cam.read()
    # Преобразование кадра из цветного в серый
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Обнаружение объекта(автомобиля)
    cars = car_cascade.detectMultiScale(gray, 1.3, 3)
    for (x, y, w, h) in cars:
        # Выделение объекта прямоугольником
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, 'Car', (x + 6, y - 6), font, 0.5, (0, 0, 255), 1)
        # Совмещение центра кадра и центра объекта
        objX = x + w / 2
        objY = y + h / 2
        errorPan = objX - width / 2
        errorTilt = objY - height / 2
        if abs(errorPan) > 15:
            pan = pan - errorPan / 75
        if abs(errorTilt) > 15:
            tilt = tilt - errorTilt / 75
        if pan > 180:
            pan = 180
            print("Pan Out of  Range")
        if pan < 0:
            pan = 0
            print("Pan Out of  Range")
        if tilt > 180:
            tilt = 180
            print("Tilt Out of  Range")
        if tilt < 0:
            tilt = 0
            print("Tilt Out of  Range")

        kit.servo[0].angle = pan
        kit.servo[1].angle = tilt
        break
    # Вывод результата на экран
    cv2.imshow('Cam', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
