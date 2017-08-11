# -*- coding: utf-8 -*-
# @Author: h005
# @Date:   2017-08-10 20:21:31
# @Last Modified by:   h005
# @Last Modified time: 2017-08-10 21:55:23

# usage: -s yyyy-mm-dd hh:mm:ss
# 		 -c -m minutes
#   	 	-h hours
#  			-s second

# example:
# python schedule.py -s 2017-08-10 20:41:11
# python schedule.py -c -m 60


import time
import datetime
import sys
import os
import platform


def printHelp():
	print ('parameter error')
	print ('usage: -s yyyy-mm-dd hh:mm:ss')
	print (' 	   -c -m minutes')
	print ('          -h hours')
	print ('          -s second')
	exit()

def action():
	sysstr = platform.system()
	if sysstr == 'Windows':
		os.system("shutdown -s -t 0")
	elif sysstr == 'Linux':
		os.system("poweroff")
#	print ('done')

t1 = datetime.datetime.now()

if len(sys.argv) < 3:
	printHelp()
else:
	if sys.argv[1] == '-s':
		scheduleTime = sys.argv[2] + ' ' + sys.argv[3]
		# print scheduleTime
		fromTime = datetime.datetime.now() 
		toTime = time.strptime(scheduleTime, "%Y-%m-%d %H:%M:%S")
		toTime = datetime.datetime(toTime[0],toTime[1],toTime[2],toTime[3],toTime[4],toTime[5])
		# print toTime		
		# print fromTime
		# print (toTime - fromTime).seconds
		if fromTime < toTime:
			counter = (toTime - fromTime).seconds
		else:
			print ("from time is later than end time")
			printHelp()
	elif sys.argv[1] == '-c':
		if sys.argv[2] == '-m':
			counter = int(sys.argv[3]) * 60
		elif sys.argv[2] == '-h':
			counter = int(sys.argv[3]) * 3600
		elif sys.argv[2] == '-s':
			counter = int(sys.argv[3])
		else:
			printHelp()
	else:
		printHelp()
	
	timeCounts = int(counter)
#	print(timeCounts)
	print ('take action in %d hours %d mins %d seconds' % (timeCounts//3600,(timeCounts%3600)//60,timeCounts%60))
	time.sleep(counter)
	action()
t2 = datetime.datetime.now()
print ((t2-t1).seconds)

