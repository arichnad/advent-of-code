#!/usr/bin/python3

data='''
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''.strip().splitlines()

data='''
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
'''.strip().splitlines()


data='''
'''.strip().splitlines()



valid=set(['shiny gold'])
changes=True
while changes:
	changes=False
	for line in data:
		line = line.replace('.', '')
		outerColor, contents = line.split(' bags contain ')
		for content in contents.split(', '):
			content = content.replace(' bags', '').replace(' bag', '')
			if content == 'no other': continue
			count,content = content.split(' ', 1)
			if content in valid and outerColor not in valid:
				valid.add(outerColor)
				changes=True


print(len(valid)-1)

size={}
changes=True
while changes:
	changes=False
	for line in data:
		line = line.replace('.', '')
		outerColor, contents = line.split(' bags contain ')
		total=0
		for content in contents.split(', '):
			content = content.replace(' bags', '').replace(' bag', '')
			if content == 'no other':
				continue
			count,content = content.split(' ', 1)
			if content not in size:
				break
			total+=int(count)*size[content]
		else:
			if outerColor not in size:
				size[outerColor]=total+1
				changes=True
print(size['shiny gold']-1)


