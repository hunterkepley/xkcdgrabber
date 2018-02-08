# Grabs some sweet sweet XKCD

import os
import sys
from argparse import ArgumentParser
from random import randint
from urllib.error import URLError
from urllib.request import urlopen, urlretrieve

BASE_URL = 'https://xkcd.com'


def grab_comic(num):
    print('Attempting to grab comic #{}'.format(num))
    page = '{}/{}'.format(BASE_URL, num)
    try:
        response = urlopen(page)
    except URLError:
        print('Problem downloading comic')
        sys.exit()
    else:
        text = str(response.read())

        li = text.find('embedding')
        lj = text.find('<div id="transcript"')
        link = text[li + 12:lj - 2]
        ti = text.find('ctitle')
        tj = text.find('<ul class="comicNav"')
        title = text[ti + 8:tj - 8]
        ty = text.find('<div id="transcript" style="display:') # Grabs the type
        imtype = text[ty - 6:ty - 2] # of image extension
        img = '{}.png'.format(title) # Default incase of error below
        if imtype == '.png':
            img = '{}.png'.format(title)
        elif imtype == '.jpg':
            img = '{}.jpg'.format(title)
        # Download
        print("Downloading image '{}'".format(img))
        urlretrieve(link, img)
        print('Finished!')


def newest_comic_number():
    try:
        new = urlopen(BASE_URL)
    except URLError:
        print("Network error; make sure you're connected to the internet or "
              "that there is nothing blocking {}".format(BASE_URL))
        sys.exit()
    else:
        content = str(new.read())
        num = content.find('this comic:')
        con = content.find('<br />\\nImage URL')
        newest = content[num + 29:con - 1]
        return int(newest)  # Newest number


def change_dir(directory):
    print("Changing to '{}'".format(directory))
    os.makedirs(directory, exist_ok=True)
    os.chdir(directory)

def multiple_grab(m_first, m_second):
    i = int(m_first) # For the loop
    if int(m_second) < int(m_first): # Reverse the numbers if the first is bigger
        i = int(m_second)
        t = m_second
        m_second = m_first
        m_first = t
    elif int(m_second) == int(m_first): # If equal, ignore the loop and grab
        grab_comic(m_first)
    while i < int(m_second): # Keep downloading until done
        grab_comic(str(i))
        i += 1

def parse_cmdline_args():
    parser = ArgumentParser(
        description='Command-line program to grab comics from XKCD'
    )
    parser.add_argument(
        '-d', '--directory',
        default='xkcd',
        help='Directory to download comic to'
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-n', '--number',
        help='Download a specific comic number',
        type=int
    )
    group.add_argument(
        '-r', '--random',
        action='store_true',
        help='Download a random XKCD comic'
    )
    group.add_argument(
        '-m', '--multiple',
        action='store_true',
        help='Prompts you to enter a range of comics from x to y to download.'
    )
    return parser.parse_args()


def main():
    args = parse_cmdline_args()

    m_first = 0
    m_second = 0

    if args.number:
        comic_number = args.number
    elif args.random:
        print('Grabbing a random comic!')
        comic_number = randint(0, newest_comic_number())
    elif args.multiple:
        m_first = input('What is your starting comic?: ')
        m_second = input('What is the last comic you want?: ')
    else:
        print('Grabbing the newest comic!')
        comic_number = newest_comic_number()

    change_dir(args.directory)

    if args.multiple:
        multiple_grab(m_first, m_second) 
    else:
        grab_comic(comic_number)
        

if __name__ == "__main__":
    main()
