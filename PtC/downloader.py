import urllib
import os.path

backs = ['03001b.jpg', '03002b.jpg', '03003b.png', '03004b.png','03005b.png', '03006b.png', '03009b.png']
jpg = [15, 16, 17, 20,23, 24, 28, 31, 35, 36, 37, 38, 39, 40, 41, 42]

toFetch = backs
for i in range(1, 43):
	fileNameBase = '0' + str(3000 + i)
	fileName = ''
	if i in jpg:
		fileName = fileNameBase + '.jpg'
	else:
		fileName = fileNameBase + '.png'
	toFetch.append(fileName)
	
for fileName in toFetch:
	if not os.path.exists(fileName):
		res = urllib.urlretrieve('https://arkhamdb.com/bundles/cards/' + fileName, fileName)