#=====================================================================================
#01_Ltika_time.py V1.0
#Put on a LED at regular intervals.
#
#Copyright (c) 2021 Weekly Engineering
#
#Released under the MIT license.
#see https://opensource.org/licenses/MIT
#=====================================================================================

import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)

GPIO.output(33, GPIO.HIGH)
time.sleep(1)
GPIO.output(33, GPIO.LOW)

GPIO.cleanup()
