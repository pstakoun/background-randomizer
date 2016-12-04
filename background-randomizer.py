#!/usr/bin/python3

import os
import random
import urllib.request
from bs4 import BeautifulSoup

MAX_RECENT = 100
FILE_NAME = 'background.jpg'

sources = [line.strip() for line in open('sources.txt')]
recent = [line.strip() for line in open('recent.txt')]

flag = True
while flag:
	source = urllib.request.urlopen(urllib.request.Request(random.choice(sources),data=None,headers={'User-Agent': 'background-randomizer'}))

	while source.geturl() in recent:
		source = urllib.request.urlopen(urllib.request.Request(random.choice(sources),data=None,headers={'User-Agent': 'background-randomizer'}))

	print(source.geturl())

	recent.append(source.geturl())

	if len(recent) > MAX_RECENT:
		del recent[0]

	open('recent.txt', 'w').write('\n'.join(recent))

	result = BeautifulSoup(source.read()).find_all('img', class_='preview')

	if len(result) > 0:
		urllib.request.urlretrieve(result[0].get('src'), FILE_NAME)
		flag = False

os.system('gsettings set org.gnome.desktop.background picture-uri file://$(pwd)/' + FILE_NAME)
