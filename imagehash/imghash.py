from PIL import Image

import imagehash

imglist = []

# hash1 = imagehash.average_hash(Image.open('/home/dale/Projects/originals/IMG12.jpg'))
hash1 = imagehash.average_hash(Image.open('test.jpg'))
# pichh = imagehash.average_hash(Image.open(picFileDirectory))

imglist.append(hash1)

print(hash1)

hash2 = imagehash.average_hash(Image.open('test2.jpg'))

imglist.append(hash2)

print(hash2)

print imglist[0]