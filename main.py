# Grabs some sweet sweet XKCD

import os, bs4, urllib.request

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)


def grabComic(num):
	print('Attempting to grab latest comic')
	try:
		page = url + num + '/'
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
		print('Network error; make sure you\'re connected to the internet or that there is no firewall blocking xkcd.')
		exit()

def changeDir():
	print('Changing to ./xkcd')
	try:
		os.chdir('./xkcd')
		print('Cd\'d properly. Continuing')
	except OSError:
		print('./xkcd not found')
		print('Making')
		os.makedirs(directory)
		try:
			os.chdir('./xkcd')
			print('Cd\'d properly. Continuing')
		except:
			print('Cannot change dir to ./xkcd... Exiting')
			exit()

def main():
	print("Grabbing newest XKCD!")
	print('Newest comic number: ' + str(newestComicNumber()) + '\n')
	changeDir()
	grabComic(str(newestComicNumber()))


if __name__ == "__main__":
	main()
