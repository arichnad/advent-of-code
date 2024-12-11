#!/usr/bin/python3


data1='''
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
'''.strip().splitlines()
data2='''

'''.strip().splitlines()

data=data1

#data = [int(line) for line in data[0].split(',')]
#data = [int(line) for line in data]

s=[[]]
for line in data:
	if line=='':
		s.append([])
		continue
	if line.startswith('---'):
		continue
	s[-1].append([int(a) for a in line.split(',')])


forwards=[[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

def mul(matrix1, matrix2):
	res = [[0 for x in range(3)] for y in range(len(matrix2))]
	for i in range(len(matrix1)):
		for j in range(len(matrix2[0])):
			for k in range(len(matrix2)):

				# resulted matrix
				res[i][j] += matrix1[i][k] * matrix2[k][j]
	return res

def connect(first, second, rotation):
	count={}
	for f in first:
		for s in second:
			mulAns=mul([s], rotation)[0]
			xDifference=mulAns[0]-f[0]
			yDifference=mulAns[1]-f[1]
			zDifference=mulAns[2]-f[2]
			key=(xDifference, yDifference, zDifference)
			if key in count:
				count[key]+=1
				if count[key]>=12:
					return key
			else:
				count[key]=1
	return None

def remove(first, second, key, rotation):
	for f in first:
		if f[0] is None:
			continue
		for s in second:
			if s[0] is None:
				continue
			mulAns=mul([s], rotation)[0]
			xDifference=mulAns[0]-f[0]
			yDifference=mulAns[1]-f[1]
			zDifference=mulAns[2]-f[2]
			if (xDifference, yDifference, zDifference)==key:
				s[0]=None

def cross(a, b):
	return [a[1]*b[2] - a[2]*b[1], \
	a[2]*b[0] - a[0]*b[2], \
	a[0]*b[1] - a[1]*b[0]]

out={}
for first in range(len(s)):
	print(first)
	for right in forwards:
		for down in forwards:
			if right==down or [-x for x in right] == down:
				continue
			forward=cross(right, down)
			rotation=[right, down, forward]
			for second in range(len(s)):
				if first==second:
					continue
				key=connect(s[first], s[second], rotation)
				if key is not None:
					out[(first, second)]=(key, rotation)

for i in range(20):
	print('linking', i)
	moreOut={}
	for (first, second), (k1, r1) in out.items():
		moreOut[(first, second)]=(k1, r1)
		for (secondAgain, third), (k2, r2) in out.items():
			if second!=secondAgain or first==third or (first, third) in moreOut:
				continue
			k2=mul([k2], r1)[0]
			moreOut[(first, third)]=((k1[0]+k2[0], k1[1]+k2[1], k1[2]+k2[2]), mul(r2, r1))
	out=moreOut

for (first, second), (key, rotation) in out.items():
	print(first, second, key)
	remove(s[first], s[second], key, rotation)

output=0
for f in s:
	for n in f:
		if n[0] is not None:
			output+=1
print(output)

best=None
for (first, second), (key, rotation) in out.items():
	distance=abs(key[0])+abs(key[1])+abs(key[2])
	if best is None or distance>best:
		best=distance
print(best)

