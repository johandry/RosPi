import logging
import sys

class Motor:
	"""A class to control the motor"""

	MotorLeftA = 19 # BOARD = 19 # BMC = 9
	MotorLeftB = 21 # BOARD = 21 # BMC = 10
	MotorLeftE = 23 # BOARD = 23 # BMC = 11

	MotorRightA = 16 # BOARD = 16 # BMC = 23
	MotorRightB = 18 # BOARD = 18 # BMC = 24
	MotorRightE = 22 # BOARD = 22 # BMC = 25

	MotorRightDeltha = 15
	MotorLeftDeltha  = 0

	def __init__(self, _GPIO_, _logging_):
		self.GPIO = _GPIO_
		self.logging = _logging_

		# self.GPIO.setmode(self.GPIO.BOARD)

		self.GPIO.setup(self.MotorLeftA, self.GPIO.OUT)
		self.GPIO.setup(self.MotorLeftB, self.GPIO.OUT)
		self.GPIO.setup(self.MotorLeftE, self.GPIO.OUT)

		self.GPIO.setup(self.MotorRightA, self.GPIO.OUT)
		self.GPIO.setup(self.MotorRightB, self.GPIO.OUT)
		self.GPIO.setup(self.MotorRightE, self.GPIO.OUT)

		self.MotorRight = self.GPIO.PWM(self.MotorRightE, 50)
		self.MotorRight.start(0)
		self.MotorLeft  = self.GPIO.PWM(self.MotorLeftE, 50)
		self.MotorLeft.start(0)

	def forwardMotorLeft(self, speed):
		speed += self.MotorLeftDeltha
		self.GPIO.output(self.MotorLeftA, self.GPIO.HIGH)
		self.GPIO.output(self.MotorLeftB, self.GPIO.LOW)
		self.GPIO.output(self.MotorLeftE, self.GPIO.HIGH)
		self.MotorLeft.ChangeDutyCycle(speed)
		self.logging.debug("Forward Motor Left at %d", speed)

	def forwardMotorRight(self, speed):
		speed += self.MotorRightDeltha
		self.GPIO.output(self.MotorRightA, self.GPIO.HIGH)
		self.GPIO.output(self.MotorRightB, self.GPIO.LOW)
		self.GPIO.output(self.MotorRightE, self.GPIO.HIGH)
		self.MotorRight.ChangeDutyCycle(speed)
		self.logging.debug("Forward Motor Right at %d", speed)

	def backwardMotorLeft(self, speed):
		speed += self.MotorLeftDeltha
		self.GPIO.output(self.MotorLeftA, self.GPIO.LOW)
		self.GPIO.output(self.MotorLeftB, self.GPIO.HIGH)
		self.GPIO.output(self.MotorLeftE, self.GPIO.HIGH)
		self.MotorLeft.ChangeDutyCycle(speed)
		self.logging.debug("Backward Motor Left at %d", speed)

	def backwardMotorRight(self, speed):
		speed += self.MotorRightDeltha
		self.GPIO.output(self.MotorRightA, self.GPIO.LOW)
		self.GPIO.output(self.MotorRightB, self.GPIO.HIGH)
		self.GPIO.output(self.MotorRightE, self.GPIO.HIGH)
		self.MotorRight.ChangeDutyCycle(speed)
		self.logging.debug("Backward Motor Right at %d", speed)

	def stopMotorLeft(self):
		self.GPIO.output(self.MotorLeftE, self.GPIO.LOW)
		self.MotorLeft.ChangeDutyCycle(0)
		self.logging.debug("Stop Motor Left")

	def stopMotorRight(self):
		self.GPIO.output(self.MotorRightE, self.GPIO.LOW)
		self.MotorRight.ChangeDutyCycle(0)
		self.logging.debug("Stop Motor Right")

	def forward(self, speed):
		self.logging.debug("Moving forward")
		self.forwardMotorRight(speed)
		self.forwardMotorLeft(speed)

	def backward(self, speed):
		self.logging.debug("Moving backward")
		self.backwardMotorRight(speed)
		self.backwardMotorLeft(speed)

	def rightTurn(self, speed):
		self.logging.debug("Turn right")
		self.stopMotorRight()
		self.forwardMotorLeft(speed)

	def right(self, speed):
		self.logging.debug("Moving to the right")
		self.backwardMotorRight(speed)
		self.forwardMotorLeft(speed)

	def leftTurn(self, speed):
		self.logging.debug("Turn left")
		self.stopMotorLeft()
		self.forwardMotorRight(speed)

	def left(self, speed):
		self.logging.debug("Moving to the left")
		self.backwardMotorLeft(speed)
		self.forwardMotorRight(speed)

	def stop(self):
		self.logging.debug("Stop!")
		self.stopMotorRight()
		self.stopMotorLeft()
