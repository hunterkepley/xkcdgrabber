# Use

Change your directory using `-d DIR` [default is ./xkcd]

**[example: -d xkcd]**


Change comic number to download using `-n NUM`

**[example: -n 1234]**

Grab random comic using `-r`

Grab multiple comics using `-m` [It will prompt you after running with `-m` 
which you want]

Display help using `-h`

Not having `-n X`, `-r`, or `-m` will result in the newest comic being grabbed.

# Prerequisites

Works on Python3+ [Python 3+ has the request module]

### Known issue

Needs to tell whether the image is a jpg or png, old ones are jpg, new ones are png... Some old images wont work due to this issue at the moment.
