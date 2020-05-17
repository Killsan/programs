import os

# name = input('Enter the name of the .txt file: ')
name = 'dark_matter.txt'

file = open(name, 'r', encoding='utf-8').read().split()


fxfile = open(name + '_FIXED.txt', 'w', encoding='utf-8')
fixed_file = []
# hot_words = [
# 	'обнаружены.', 
# 	'ИСТОРИЯ', 
# 	'B.', 
# 	'воздействию.',
# 	'света.',
# 	'звёзд.',
# 	'массы.',
# 	'войной.',
# 	'галактики.',
# 	'скоплений'


# ]

def fix(elem):
	x = elem.split('[')
	for y in x:
		if ']' in y:
			z = y.split(']')
			z.remove(z[0])
			y = "".join(z)
		x = "".join(y)
	return "".join(x)

for i in file:
	if '[' in i and ']' in i:
		i = fix(i)
	fixed_file.append(i)

for x in file:
	for y in fixed_file:
		if y in x:
			x = y

# for i in fixed_file:
# 	for x in hot_words:
# 		if x in i:
# 			fxfile.write(i + '\n')
# 		else:
# 			fxfile.write(i + ' ')

for i in fixed_file:
	fxfile.write(i + ' ')

fxfile.close()