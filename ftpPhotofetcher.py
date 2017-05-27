# -*- coding: utf-8 -*-
# @Author: h005
# @Date:   2017-05-21 11:21:19
# @Last Modified by:   h005
# @Last Modified time: 2017-05-24 22:48:45

# this script was created for crawling pictures
# from the phone.
# 1. install the "ES file explore" on your phone
# 2. open the "remote manager".
# 3. modify the ftpAddress and the dateMonth as well as the dateDay
# 4. modify the folder you will store the photos


import os
import wget
import requests
import bs4
import re
import urllib2

import io

ftpAddress = 'ftp://192.168.1.105:3721/DCIM/Camera/'

dateMonth = 'May'
dateDay = '24'

Dir = './photos/'

# response = requests.get(ftpAddress)
response = urllib2.urlopen(ftpAddress)

context = response.read()

context = context.strip()
context = context.split('\n')

for ele in context:
	# ele '-rw-r--r-- 1 nobody nobody      2888891 Oct 14 06:26 IMG_20161014_072604.jpg'
	# remove continuous spaces from the ele
	eleContext = ' '.join(filter(lambda x: x, ele.split(' ')))
	# eleContext '-rw-r--r-- 1 nobody nobody 2888891 Oct 14 06:26 IMG_20161014_072604.jpg'
	eleContext = eleContext.strip()
	eleContext = eleContext.split(' ')
	if eleContext[5] == dateMonth and eleContext[6] == dateDay:
		fileName = eleContext[-1]
		# print fileName[-3:]
		if fileName[-3:] == 'jpg':
			# copy the file into the Dir
			f = urllib2.urlopen(ftpAddress + fileName)
			data = f.read()
			with open(Dir + fileName, 'wb') as pic:
				pic.write(data)
			print 'cp ' + ftpAddress + fileName
			print '  to ' + Dir + fileName
			print ' '
			# wget has some errors when downloading the photos
			# wget.download(ftpAddress + fileName)
print 'copy done'
