import RPi.GPIO as GPIO

from motor import Motor
from panandtilt import PanAndTilt
from Sensor.distance import Distance

from time import sleep

import logging
import sys

class	Robot:
	"""A class to control the Robot. This class use all the other classes"""
	MoveTime = 0.1
	Speed = 50

	def __init__(self, debugMode = False):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)

		if debugMode:
			level = logging.DEBUG
		else:
			level = logging.CRITICAL
		logging.basicConfig(stream=sys.stderr, level=level)

		self.motor 			= Motor(GPIO, logging)
		self.panandtilt = PanAndTilt(logging)
		self.distance 	= Distance(GPIO, logging)

		self.MoveDirectionsOptions = {
			'fwd': self.motor.forward,
			'stp': self.motor.stop,
			'lft': self.motor.leftTurn,
			'rgt': self.motor.rightTurn,
			'bwd': self.motor.backward,
			'lfm': self.motor.left,
			'rgm': self.motor.right,
		}

		self.LookDirectionsOptions = {
			'fnt': self.panandtilt.front,
			'lft': self.panandtilt.left,
			'rgt': self.panandtilt.right,
			'up': self.panandtilt.up,
			'dwn': self.panandtilt.down,
		}		

	def lookTo(self, anglex, angley):
		self.panandtilt.pan(anglex)
		self.panandtilt.tilt(angley)

	def look(self, direction):
		self.LookDirectionsOptions[direction]()

	def move(self, direction, speed=Speed, moveTime=MoveTime):
		if direction == 'stp':
			logging.debug("Stopping the Robot")
			self.motor.stop()
		else:
			if speed == None:
				speed = self.Speed
			
			logging.debug("Moving %s with speed %d for %f seconds", direction, speed, moveTime)
		
			self.MoveDirectionsOptions[direction](speed)
			sleep(moveTime)

	def whereToMove(self):
		self.look('lft')
		distance_lft = self.distance.getDistance()
		logging.debug("Left distance: %d", distance_lft)

		self.look('rgt')
		distance_rgt = self.distance.getDistance()
		logging.debug("Right distance: %d", distance_rgt)

		if distance_rgt < distance_lft:
			logging.debug("Going to Right")
			return 'rgm'
		else:
			logging.debug("Going to Right")
			return 'lfm'

	def start(self):
		self.on = True
		self.look('fnt')

		while self.on:
			distance = self.distance.getDistance()
			logging.debug("Distance: %d", distance)
			# If there is no object in less than 30 cm ahead
			if distance < 50:
				self.move('stp')
				direction = self.whereToMove()
				self.look('fnt')
				self.move(direction, 40, 0.5)
				self.motor.stop()
			else:
				self.move('fwd')
				
	def stop(self):
		self.on = False

	def finish(self):
		GPIO.cleanup()