import logging
import sys
import os

class PanAndTilt:
	"""A class to control the servos to pan and tilt"""

	Min				= 50
	MaxY			= 250
	MaxX			= 230
	NeutralY	= 150
	NeutralX	= 130

	def __init__(self, __logging__):
		self.logging = __logging__
		if not os.path.exists("/dev/servoblaster"):
			self.logging.debug("Executing servod to upgrade Kernel")
			servod = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bin', 'servod'))
			os.system(servod)


	def pan(self, angle):
		self.logging.debug("Panning to %s deg", angle)
		os.system('echo 0='+str(angle)+' > /dev/servoblaster')

	def tilt(self, angle):
		self.logging.debug("Tilting to %s deg", angle)
		os.system('echo 1='+str(angle)+' > /dev/servoblaster')

	def front(self):
		self.logging.debug("Looking to the front")
		self.pan(self.NeutralY)
		self.tilt(self.NeutralX)
	def left(self):
		self.logging.debug("Looking to the left")
		self.pan(self.Min)
		self.tilt(self.NeutralX)
	def right(self):
		self.logging.debug("Looking to the right")
		self.pan(self.MaxY)
		self.tilt(self.NeutralX)
	def up(self):
		self.logging.debug("Looking up")
		self.pan(self.NeutralY)
		self.tilt(self.Min)
	def down(self):
		self.logging.debug("Looking down")
		self.pan(self.NeutralY)
		self.tilt(self.MaxX)
