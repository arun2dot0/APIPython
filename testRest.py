#!/usr/bin/python
from time import sleep
import apiCall

while True:
	try:
		apiCall.postConditions(22,55,253,500)
		sleep(300)			
	except (IOError,TypeError) as e:
		print("Error")

