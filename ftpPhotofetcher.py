# -*- coding: utf-8 -*-
# @Author: h005
# @Date:   2017-05-21 11:21:19
# @Last Modified by:   h005
# @Last Modified time: 2017-06-17 15:34:41

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

ftpAddress = 'ftp://192.168.2.101:3721/PlayMemories Mobile/'
# ftpAddress = 'ftp://172.28.148.138:3721/DCIM/Camera/'
# ftpAddress = 'ftp://172.28.171.253:3721/DCIM/Camera/'

# ftpAddress = 'ftp://172.28.24.149:3721/DCIM/Camera/'


dateMonth = 'Jun'
dateDayLst = range(8,18)

for ele in dateDayLst:
	# dateDay = str(ele)
	dateDay = '%02d' % ele
	# print dateDay
# dateDay = '28'

	Dir = './photos/'

	# response = requests.get(ftpAddress)
	response = urllib2.urlopen(ftpAddress)

	context = response.read()

	context = context.strip()
	context = context.split('\n')

	Dir = Dir + dateMonth + '_' + dateDay + '/'
	if not os.path.exists(Dir):
		os.mkdir(Dir)

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
			if fileName[-3:] == 'jpg' or fileName[-3:] == 'JPG':
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
	print dateMonth + ' ' + dateDay + ' copy done'

print 'copy done'