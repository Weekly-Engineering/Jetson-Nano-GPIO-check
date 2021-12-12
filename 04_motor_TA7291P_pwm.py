#=====================================================================================
#04_motor_TA7291P_pwm.py V1.0
#Driving motor by PWM control.
#
#Copyright (c) 2021 Weekly Engineering
#
#Released under the MIT license.
#see https://opensource.org/licenses/MIT
#=====================================================================================

import Jetson.GPIO as GPIO
import time

in1 = 31
in2 = 32
vref = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(in2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(vref, GPIO.OUT, initial=GPIO.HIGH)

pwm = GPIO.PWM(vref, 200)    #GPIO.PWM(channel, freqency[Hz]) 

pwm.start(25)  #.start(duty[%])
time.sleep(1)

pwm.start(50)  #.start(duty[%])
time.sleep(1)

pwm.start(100)  #.start(duty[%])
time.sleep(1)

pwm.start(50)  #.start(duty[%])
time.sleep(1)

pwm.start(25)  #.start(duty[%])
time.sleep(1)

GPIO.setup(in1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(in2, GPIO.OUT, initial=GPIO.HIGH)
pwm.stop()
time.sleep(1)

GPIO.setup(in1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(in2, GPIO.OUT, initial=GPIO.HIGH)

pwm.start(25)  #.start(duty[%])
time.sleep(1)

pwm.start(50)  #.start(duty[%])
time.sleep(1)

pwm.start(100)  #.start(duty[%])
time.sleep(1)

pwm.start(50)  #.start(duty[%])
time.sleep(1)

pwm.start(25)  #.start(duty[%])
time.sleep(1)

GPIO.setup(in1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(in2, GPIO.OUT, initial=GPIO.HIGH)
pwm.stop()
time.sleep(1)

GPIO.cleanup()
