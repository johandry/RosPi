#!/usr/bin/env python 

from RoboterryPi.robot import Robot
import sys
from time import sleep

def main():
	verbose = len(sys.argv) > 1 and sys.argv[1] == '-v'
	robot = Robot( verbose )

	robot.look('lft')
	sleep(2)
	robot.look('fnt')
	sleep(2)
	robot.look('rgt')
	sleep(2)
	robot.look('up')
	sleep(2)
	robot.look('dwn')
	# sleep(2)
	# robot.lookTo(90, 90)

	robot.finish()

if __name__ == "__main__":
	main()