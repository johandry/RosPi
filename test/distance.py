#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO_TRIGGER=17
GPIO_ECHO=27

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)


def getDistance_1():
  GPIO.output(GPIO_TRIGGER, GPIO.LOW)
  time.sleep(0.3)

  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)

  while GPIO.input(GPIO_ECHO) == 0:
    pass
  signaloff = time.time()
  
  while GPIO.input(GPIO_ECHO) == 1:
    pass
  signalon = time.time()

  return (signalon - signaloff) * 17000

def _measure():
  GPIO.output(GPIO_TRIGGER, GPIO.LOW)
  time.sleep(0.3)

  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)

  while GPIO.input(GPIO_ECHO)==0:
    pass
  start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    pass
  stop = time.time()

  return (stop-start) * 34300/2

def getDistance_2():
  # This function takes 3 measurements and
  # returns the average.
  distance1=_measure()
  time.sleep(0.1)
  distance2=_measure()
  time.sleep(0.1)
  distance3=_measure()
  return (distance1 + distance2 + distance3)/3

start=time.time()
distance = getDistance_1()
stop=time.time()
print "Using function #1: "+str(distance) + " cm at "+str(stop-start)+" sec"

start=time.time()
distance = getDistance_2()
stop=time.time()
print "Using function #2: "+str(distance) + " cm at "+str(stop-start)+" sec"

GPIO.cleanup()
