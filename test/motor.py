#!/usr/bin/env python 

from RoboterryPi.robot import Robot
import sys

def main():
	verbose = len(sys.argv) > 1 and sys.argv[1] == '-v'
	robot = Robot( verbose )

	robot.move('fwd')
	robot.move('lft')
	robot.move('fwd')
	robot.move('rgm')
	robot.move('bwd')
	robot.move('lfm')
	robot.move('bwd')
	robot.move('rgt')
	robot.move('stp')

	robot.finish()

if __name__ == "__main__":
	main()