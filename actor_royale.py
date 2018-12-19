import requests
import bs4
import re
import random

page = 1
url  = 'https://www.imdb.com/list/ls002984722/?page={:d}'
names = []

# Do while we are still on a valid page
while True:

    # Grab and parse page
    print ('Dealing with page {:d}...'.format(page))

    r = requests.get(url.format(page))
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    dirty_list = soup.findAll('a', href=re.compile('ref_=nmls_hd'))

    # If this is no longer part of the main list, break out of loop
    if len(dirty_list) == 0:
        break

    # Add names to full list
    for name in dirty_list:
        names.append(name.text[1:-1]) #remove space in beginning and \n at end

    # Increment page number
    page += 1

print(names)

# Select 32 random names

random_samples = random.sample(range(len(names)),32)
bracket_names = []

for sample in random_samples:
    bracket_names.append(names[sample])

print(bracket_names)

# Create bracket with names
from PIL import Image, ImageDraw

img = Image.new('RGB', (640,480), color='white')
draw = ImageDraw.Draw(img)
current_y = 0
for name in bracket_names:
    draw.text((0,current_y),name,(0,0,0))
    current_y = current_y + 20

img.save('newimage.png')
