#!/usr/bin/env python

from RoboterryPi.robot import Robot
import sys

def main():
	verbose = len(sys.argv) > 1 and sys.argv[1] == '-v'
	robot = Robot( verbose )

	robot.start()
	robot.stop()

if __name__ == "__main__":
	main()