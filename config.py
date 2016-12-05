#!/usr/bin/python3

import sys
import os

minutes = 0

if len(sys.argv) < 2:
	minutes = int(input('Interval (minutes): '))
else:
	minutes = int(sys.argv[1])

crontab = os.popen('crontab -l').read()
cwd = os.getcwd()
output = ''
for line in crontab.split('\n')[:-1]:
	if cwd not in line:
		output += line + '\n'

output += '*/' + str(minutes) + ' * * * * cd ' + cwd + ' && ./background-randomizer.py' + '\n'

open('temp', 'w').write(output)

os.system('crontab temp')

os.remove('temp')
