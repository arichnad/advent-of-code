#!/usr/bin/python3


data='''
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
'''.strip().splitlines()

data='''
'''.strip().splitlines()
ans=set()
for line in data:
	x=0
	y=0
	while line!='':
		if line.startswith('se'):
			y+=1
			x+=1
			line=line[2:]
		elif line.startswith('sw'):
			y+=1
			line=line[2:]
		elif line.startswith('nw'):
			y-=1
			x-=1
			line=line[2:]
		elif line.startswith('ne'):
			y-=1
			line=line[2:]
		elif line.startswith('w'):
			x-=1
			line=line[1:]
		elif line.startswith('e'):
			x+=1
			line=line[1:]
	#ans[(x, y)]=not ans[(x, y)] if (x, y) in ans else True
	if (x, y) in ans:
		ans.remove((x, y))
	else:
		ans.add((x, y))
print(len(ans))

for i in range(100):
	newAns=set()
	for (x, y) in ans:
		total=0
		for direction in range(6):
			dx=0
			dy=0
			if direction==0:
				dy=1
				dx=1
			elif  direction==1:
				dy=1
			elif  direction==2:
				dy=-1
				dx=-1
			elif  direction==3:
				dy=-1
			elif  direction==4:
				dx=-1
			elif direction==5:
				dx=1

			newX=x+dx
			newY=y+dy
			if (newX, newY) in ans:
				#black
				total+=1
			else:
				#white
				total2=0
				for direction2 in range(6):
					dx=0
					dy=0
			
					if direction2==0:
						dy=1
						dx=1
					elif  direction2==1:
						dy=1
					elif  direction2==2:
						dy=-1
						dx=-1
					elif  direction2==3:
						dy=-1
					elif  direction2==4:
						dx=-1
					elif direction2==5:
						dx=1
					
					newX2=newX+dx
					newY2=newY+dy

					if (newX2, newY2) in ans:
						#black
						total2+=1
				if total2==2:
					#make it black
					newAns.add((newX, newY))
		if total==1 or total==2:
			newAns.add((x, y))
	ans=newAns
print(len(ans))


