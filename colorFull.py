import time
from time import sleep
import RPi.GPIO as GPIO

ledRed = 11
ledYellow = 29
ledGreen =33

GPIO.setwarnings(False)

Gpio.setmode(GPIO.BOARD)

GPIO.setup(ledRed,GPIO.OUT)
GPIO.setup(ledYellow,GPIO.OUT)
GPIO.setup(ledGreen,GPIO.OUT)

x = 0

while x == 0
  GPIO.output(ledREd,GPIO.HIGH)
  time.sleep(.7)
  GPIO.output(ledRed,GPIO.LOW)
  time.sleep(.2)
  GPIO.output(ledYellow,GPIO.HIGH)
  time.sleep(.7)
  GPIO.output(ledYellow,GPIO.LOW)
  time.sleep(.2)
  
  
