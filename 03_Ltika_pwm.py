#=====================================================================================
#03_Ltika_pwm.py V1.0
#Put on a LED by PWM control.
#
#Copyright (c) 2021 Weekly Engineering
#
#Released under the MIT license.
#see https://opensource.org/licenses/MIT
#=====================================================================================

import Jetson.GPIO as GPIO
import time

led = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200)  # GPIO.PWM(channel, freqency[Hz]) 
pwm.start(25)  # .start(duty[%])
time.sleep(1)
pwm.start(50)  # .start(duty[%])
time.sleep(1)
pwm.start(75)  # .start(duty[%])
time.sleep(1)
pwm.start(100)  # .start(duty[%])
time.sleep(1)
pwm.stop()

GPIO.cleanup()