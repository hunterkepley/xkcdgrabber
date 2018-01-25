# Grabs some sweet sweet XKCD

import os, bs4, urllib.request

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)

print("Grabbing newest XKCD!")

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
		print('No internet or other network error.. Exiting')
		exit()

print('Newest comic number: ' + str(newestComicNumber()) + '\n')
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

grabComic(str(newestComicNumber()))
