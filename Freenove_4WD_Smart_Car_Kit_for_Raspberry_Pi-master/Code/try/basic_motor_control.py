from Motor import *

PWM = Motor()

def forward():
    PWM.setMotorModel(1000, 1000, 1000, 1000)  # Forward
    print("The car is moving forward")
    time.sleep(1)


def backward():
    PWM.setMotorModel(-1000, -1000, -1000, -1000)  # Back
    print("The car is going backwards")
    time.sleep(1)


def left():
    PWM.setMotorModel(-1500, -1500, 2000, 2000)  # Left
    print("The car is turning left")
    time.sleep(1)


def right():
    PWM.setMotorModel(2000, 2000, -1500, -1500)  # Right
    print("The car is turning right")
    time.sleep(1)


def stop():
    PWM.setMotorModel(0, 0, 0, 0)  # Stop


if __name__ == '__main__':
    for i in range (10):
        forward()
    for i in range (10):
        left()