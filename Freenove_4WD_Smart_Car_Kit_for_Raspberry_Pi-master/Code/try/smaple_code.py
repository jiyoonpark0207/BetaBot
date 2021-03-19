from Ultrasonic import * #import Led
ultrasonic=Ultrasonic() #create an object
data=ultrasonic.get_distance() #Get the value
print ("Obstacle distance is "+str(data)+"CM")

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

from Motor import * #import Motor
PWM=Motor() #create an object
PWM.setMotorModel(2000,2000,2000,2000) #Forward
time.sleep(3) #waiting 3 second
PWM.setMotorModel(0,0,0,0) #Stop