#=====================================================================================
#02_Ltika_sw.py V1.0
#Put on a LED by switchi input.
#
#Copyright (c) 2021 Weekly Engineering
#
#Released under the MIT license.
#see https://opensource.org/licenses/MIT
#=====================================================================================

import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)
GPIO.setup(33, GPIO.OUT)

GPIO.output(33, GPIO.LOW)
for i in range(10):
    ledsta = GPIO.input(13)
    if ledsta == GPIO.HIGH:
        GPIO.output(33, GPIO.LOW)
    else:
        GPIO.output(33, GPIO.HIGH)
    time.sleep(1)

GPIO.cleanup()