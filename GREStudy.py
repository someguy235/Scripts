import random
import os

input = open('GREWordsSorted.txt', 'r')

list = []
words = []
defs = []

offset = 0
quit = ""
done = 0

for line in input.readlines():
	if (len(line) != 1):
		lineList = line.split(' ')
		words.append(lineList[0])
		offset = len(lineList[0]) + 1
		defs.append(line[offset:])

print '%i words in list' %len(words)
raw_input("")
used = words

while((quit.lower() != "q") & (done < len(words))):
	print("-")*100
	print
	rand = random.randint(0, len(words))
	if(used[rand] != "used"):
		print (words[rand])
		quit = raw_input()
		print (defs[rand])
		if (quit.lower() != 'q'):
			quit = raw_input()
		done = done + 1
		used[rand] = "used"
		
