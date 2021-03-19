from servo import * #import Led
pwm = Servo() #create an object
#Servo rotates from 30 degrees to 150 degrees
for i in range(30, 150, 1) :
    pwm.setServoPwm('0', i)
    time.sleep(0.01)
#Servo rotates from 150 degrees to 0 degrees
for i in range(150, 30, -1) :
    pwm.setServoPwm('0', i)
    time.sleep(0.01)