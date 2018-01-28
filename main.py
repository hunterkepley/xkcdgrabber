# Grabs some sweet sweet XKCD

import os, bs4, urllib.request, sys
from random import randint

url = 'https://xkcd.com/'


def grabComic(num):
	print('Attempting to grab comic #{}'.format(num))
	try:
		page = url + num
		response = urllib.request.urlopen(page)
		text = str(response.read())
		
		li = text.find('embedding')
		lj = text.find('<div id="transcript"')
		link = text[li+12:lj-2]
		ti = text.find('ctitle')
		tj = text.find('<ul class="comicNav"')
		title = text[ti+8:tj-8]
		img = title + '.png'
		# Download
		print('Downloading image ' + img)
		urllib.request.urlretrieve(link, img)
		print('Finished!')
	except urllib.error.URLError:
		print('Problem downloading comic')
		exit()

def newestComicNumber():
	try:
		new = urllib.request.urlopen(url)
		content = str(new.read())
		num = content.find('this comic:')
		con = content.find('<br />\\nImage URL')
		newest = content[num+29:con-1]
		return int(newest) # Newest number
	except urllib.error.URLError:
		print('Network error; make sure you\'re connected to the internet or that there is nothing blocking ', url)
		exit()

def changeDir(directory):
	print('Changing to {}'.format(directory))
	try:
		os.chdir(directory)
		print('Cd\'d properly. Continuing')
	except OSError:
		print('{} not found'.format(directory))
		print('Making')
		os.makedirs(directory, exist_ok=True)
		os.chdir(directory)

def sysArgCheck(): # Deals with system args
	directory = 'xkcd'
	comicNumber = ''
	currentArg = 0
	for arg in sys.argv: # Checks for arguments and sets them
		if arg == '-h' or arg == '--help':
			print('\nXKCDGrabber help ---\n\n-h|--help\tDisplays this\n-d|--directory\t-d X changes download dir to X\n-n|--number\t-n X changes comic number to download to X.\n\n')
			exit()
		elif arg == '-d' or arg == '--directory':
			try:
				if sys.argv[currentArg+1][0] != '-':
					directory = sys.argv[currentArg+1]
				else:
					print('No argument after {}'.format(sys.argv[currentArg]))
					exit()
			except IndexError:
				print('No argument after {}'.format(sys.argv[currentArg]))
				exit()
		elif arg == '-n' or arg == '--number':
			try:
				if sys.argv[currentArg+1][0] != '-':
					comicNumber = sys.argv[currentArg+1]
				else:
					print('No argument after {}'.format(sys.argv[currentArg]))
					exit()
			except IndexError:
				print('No argument after {}'.format(sys.argv[currentArg]))
				exit()
		currentArg += 1
	return directory, comicNumber

def main():
	directory = 'xkcd'
	comicNumber = ''
	directory, comicNumber = sysArgCheck()
	print('Newest comic number: ' + str(newestComicNumber()) + '\n')
	if comicNumber == '': # If no argument provided [-n]
		num = input("What comic number do you want [Type r for random]?: ")
	if comicNumber == '': # If nothing entered for input
		comicNumber = str(newestComicNumber())
	changeDir(directory)
	if comicNumber == 'r':
		comicNumber = str(randint(0, newestComicNumber()))
		grabComic(comicNumber)
	else:
		grabComic(comicNumber)

if __name__ == "__main__":
	main()
