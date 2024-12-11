#!/usr/bin/python3


data='''
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
'''.strip().splitlines()
data='''
'''.strip().splitlines()

all={}
orig=[]

for line in data:
	ingr, contains = line.split(' (contains ')
	contains = contains.replace(')','').split(', ')
	ingr = ingr.split(' ')
	orig.extend(ingr)


	for c in contains:
		if c not in all:
			all[c] = set(ingr)
		else:
			all[c] = all[c].intersection(set(ingr))
	
	change=True
	while change:
		change=False
		for key in list(all.keys()):
			if len(all[key])==1:
				thing=next(iter(all[key]))
				for key2 in list(all.keys()):
					if key==key2:
						continue
					if thing in all[key2]:
						all[key2].remove(thing)
						change=True

output=[]
for v in all.values():
	if len(v) != 1:
		print('fail')
	output.append(next(iter(v)))
print(output, orig, sum([1 if not o in output else 0 for o in orig]))

print(','.join([next(iter(all[k])) for k in sorted(all.keys())]))
for k in sorted(all.keys()):
	print(k, all[k])
#lmxt,rggkbpj,mxf,gpxmf,nmtzlj,dlkxsxg,fvqg,mxf is wrong

