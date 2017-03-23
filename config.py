#!/usr/bin/python3

import sys
import os

minutes = 0

if len(sys.argv) < 2:
	minutes = int(input('Interval (minutes): '))
else:
	minutes = int(sys.argv[1])

crontab = os.popen('crontab -l').read()
ABS_PATH = os.path.dirname(os.path.abspath(__file__))
output = ''
for line in crontab.split('\n')[:-1]:
	if ABS_PATH not in line:
		output += line + '\n'

output += '*/' + str(minutes) + ' * * * * ' + os.path.join(ABS_PATH, 'background-randomizer.py\n')

open('temp', 'w').write(output)

os.system('crontab temp')

os.remove('temp')

os.system('gsettings set org.gnome.desktop.background picture-uri file://' + os.path.join(ABS_PATH, 'background.jpg'))
