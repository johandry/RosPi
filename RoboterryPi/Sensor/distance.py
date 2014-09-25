import logging
import sys
import time

class Distance:
	"""A class to measure the distance"""

	GPIO_TRIGGER = 11 # BOARD = 11 # BMC = 17
	GPIO_ECHO		 = 13 # BOARD = 13 # BMC = 27

	def __init__(self, _GPIO_, _logging_):
		self.GPIO = _GPIO_
		self.logging = _logging_

		self.GPIO.setup(self.GPIO_TRIGGER,self.GPIO.OUT)
		self.GPIO.setup(self.GPIO_ECHO,self.GPIO.IN)

	def _measure(self):
	  self.GPIO.output(self.GPIO_TRIGGER, self.GPIO.LOW)
	  time.sleep(0.3)

	  self.GPIO.output(self.GPIO_TRIGGER, True)
	  time.sleep(0.00001)
	  self.GPIO.output(self.GPIO_TRIGGER, False)

	  while self.GPIO.input(self.GPIO_ECHO)==0:
	    pass
	  start = time.time()

	  while self.GPIO.input(self.GPIO_ECHO)==1:
	    pass
	  stop = time.time()

	  return (stop-start) * 34300/2

	def getDistance(self):
	  # This function takes 3 measurements and
	  # returns the average.
	  distance1=self._measure()
	  time.sleep(0.1)
	  distance2=self._measure()
	  time.sleep(0.1)
	  distance3=self._measure()
	  return (distance1 + distance2 + distance3)/3
