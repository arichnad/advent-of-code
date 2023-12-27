#!/usr/bin/python3

import math, re, sys, itertools, functools, copy, json, threading

#import lmfit

sys.setrecursionlimit(100000)
#from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
#from astar import AStar #python3 -mpip install astar #see astarExample.py
#from collections import defaultdict, deque, Counter
from z3 import * #python3 -mpip install install z3 z3-solver #s = Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')
#from shapely import Polygon #print(Polygon([(0,0),(1,0),(1,1)]).area) #sudo apt install pypy3-dev libgeos-dev && python3 -mpip install shapely

data1='''
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
'''.strip('\n').splitlines()
data2='''
331197478571816, 419588808460341, 308994415019000 @ -91, -24, -6
330866855164228, 209537825210093, 231185943543128 @ -150, -212, 72
328989866463373, 203709410146568, 262849170484878 @ -105, 72, -7
231834394469732, 93189176593161, 440265961238428 @ 50, 315, -239
278604695259636, 333958305417908, 213735598362658 @ 34, -326, 121
309178963923996, 154974454192289, 239566456910847 @ 10, -35, -10
314911993188598, 431909804031529, 263788657919382 @ -73, -215, 20
466494146694868, 408627100057213, 377911552080153 @ -318, -191, -166
218868631041947, 282017930176092, 210285072168131 @ 115, -38, 112
310581719228680, 143497051406425, 235960869715068 @ 20, 17, 11
290561547963936, 262309234710127, 256044911885116 @ -20, -22, 19
329596278591676, 234083430680617, 297618259938492 @ -107, -8, -96
278526934431232, 337079660291621, 295419397973852 @ 6, -183, -65
189890296114417, 179015572024965, 135414476214217 @ 81, 201, 190
249541145328072, 520365120654784, 184991465960146 @ -10, -124, 117
216223506991339, 371677631403715, 358526761210614 @ 71, -93, -115
323855008930129, 286862419599879, 235206098518482 @ -87, 15, 65
310538271311878, 338599533323418, 194858814995523 @ -60, -242, 158
348224263467355, 261637864413773, 303260436080684 @ -135, 9, -65
321683767764618, 175966592206863, 259894655468958 @ -95, 24, -64
343993250757898, 351264535701116, 283168005629568 @ -108, 6, 11
289221802256383, 429641739863593, 263026313525898 @ -47, -59, 37
308101817235764, 279019046716025, 183915047302864 @ -62, 21, 147
319225945052508, 138375169549613, 291518583634828 @ -82, 219, -141
372087777574468, 281858384933233, 242702722400268 @ -178, -23, 50
314422788737589, 132767369885491, 238202315368618 @ -19, 131, -39
126272771766250, 171163501386697, 15404835333551 @ 216, 197, 402
303867887720968, 410071000835863, 211451111726208 @ -58, -133, 99
318910997533499, 468611225037133, 242844173521142 @ -79, -151, 57
337521203403244, 324966997793465, 191693268408457 @ -102, 21, 120
290870407080268, 212152928569033, 190675851373188 @ 112, -345, 355
260746047436776, 288955999780002, 152219577741455 @ 214, -570, 474
163017555358402, 379655339912083, 378369371187996 @ 95, -16, -93
233568373481356, 368363930266881, 110128996531012 @ 21, -17, 213
302384172461193, 332145243059234, 233876469811072 @ -53, -62, 67
289899623517183, 171285693017158, 238284608531263 @ 89, -10, 30
308200350597668, 171415193911433, 235319623087028 @ -38, 78, 55
247790721293004, 339374882043765, 246795142410444 @ 86, -233, 35
164585196688084, 229265960235983, 287100591693526 @ 90, 154, 10
188132539253044, 180342488222753, 283507190096588 @ 84, 199, 6
313330201405628, 253679749297361, 471304679405844 @ -73, 133, -181
204282103491236, 283767406627297, 335275803955572 @ 106, 11, -97
365507214549349, 491796932287123, 361358562784584 @ -167, -421, -173
329695716694936, 193816275262921, 280131073705389 @ -162, -235, -282
281083323889059, 360793701899023, 425501707836788 @ -17, -121, -249
158892836071597, 366815751472018, 253497882710166 @ 109, -16, 45
213764687848339, 239306247664945, 25000170639387 @ 241, -83, 702
325364209117108, 435483484049905, 145538827002756 @ -88, -159, 189
276132577469801, 433567366348501, 93861278690980 @ 5, -343, 343
356585763245712, 486849366355517, 443084907280550 @ -116, -89, -138
319981948110538, 164087866014790, 220773748867116 @ -88, 58, 127
182198409828161, 357960789218767, 309287775488926 @ 65, 23, -11
237019037054328, 126669416112403, 271485706768063 @ 118, 263, -26
228304530086234, 269090445244055, 267811335912902 @ 124, -57, -11
117069719009499, 62121162773694, 157254180402148 @ 139, 336, 151
247576865486350, 262227890258344, 270205886200773 @ 40, 38, 6
304530618798868, 193966782859138, 210457889542158 @ -30, 22, 145
179878433235932, 418946951628501, 121357512994812 @ 118, -149, 227
294020625493696, 257086494650035, 341728345610886 @ 16, -250, -360
188108439394184, 367124351648801, 41214311894048 @ 151, -159, 406
312220823994436, 141064210488205, 237539239413075 @ 18, -7, -30
103429181089434, 257736733508054, 87163120363876 @ 184, 106, 247
304705408852603, 348172200054254, 326846851856545 @ -63, 18, -36
251942832632778, 174380409126923, 161558849965608 @ 121, 118, 281
217589410981576, 426677523315935, 331864917147600 @ 24, -38, -31
272631235944748, 280771052813593, 290629373081780 @ 57, -196, -105
282063364738412, 372485786178553, 323866624007068 @ -41, 14, -24
296130749334781, 297429137819866, 385084730816517 @ -51, 56, -118
246875180878223, 337834904504848, 183060523174194 @ 37, -76, 149
262222200625956, 97059051912749, 115059710211296 @ 130, 370, 504
296729329822504, 260943822339059, 306547882224346 @ 24, -384, -288
341866884173767, 208264870251837, 251004383045955 @ -147, 25, 14
343263161367794, 505745484621265, 209503300975767 @ -116, -307, 104
315940002602614, 236036437388521, 222042652268674 @ -72, -43, 97
304142294488924, 273184532653333, 257992621685292 @ -34, -201, -13
293539547315653, 493202515103393, 159197167996373 @ -45, -227, 168
302816714425384, 364922721210763, 351896960039610 @ -32, -456, -292
274314688466758, 190840498464265, 406468398277548 @ 77, 33, -549
317359443676559, 466528528897525, 383514900467780 @ -77, -199, -137
248101793573284, 197457512190790, 227718118677938 @ 114, 68, 81
379320680973109, 369810371773420, 326375051741013 @ -165, -80, -64
251663300114935, 202757951453023, 132793338523530 @ 15, 159, 209
258599682646372, 383785842871441, 237673065742900 @ -12, -19, 64
351044574689860, 328246660415425, 356840683013316 @ -130, -53, -127
299111784080044, 253175599306365, 212032763657128 @ -24, -98, 126
108737746677391, 211343244935806, 93891117335151 @ 155, 172, 224
422625006836929, 266965858926889, 313800820557787 @ -201, 101, -26
317270512767851, 559835194121740, 451238243716064 @ -77, -262, -197
287763841167874, 363525819065017, 278083514080542 @ -41, -23, 14
289502310148404, 347698739700977, 126105244681836 @ -34, -75, 233
319831024921342, 215251997294519, 185541185775026 @ -84, -45, 229
288037082902828, 84735479060833, 234874834168068 @ 213, 651, 37
221495736731188, 298595631442813, 158022583292588 @ 30, 74, 153
326941276586638, 251239102464509, 195175349331524 @ -123, -377, 255
302559961842508, 279842550961401, 289000577364604 @ -33, -182, -96
250254404092720, 287862989153098, 358754093362665 @ 94, -146, -252
288549899880362, 182582705076183, 306933492846328 @ 8, 99, -149
320507215846308, 167529547108493, 269872761759408 @ -94, -18, -184
441607398581020, 272968810257187, 340843882982970 @ -210, 110, -46
98938777168828, 270850994529949, 143702521122852 @ 182, 95, 175
320800676256661, 465614222816431, 379495562318592 @ -81, -109, -93
358749912302080, 308920773806611, 187168853134608 @ -124, 60, 121
298352202067364, 285798550906277, 252335797266256 @ -46, 7, 37
285009717308626, 235656964963798, 228486758614200 @ -32, 114, 75
306500805898046, 134219421026327, 197469545334684 @ 41, 166, 419
316686408011350, 214545933835371, 293631030959606 @ -75, 76, -62
101117385575860, 242856007991041, 248215701801396 @ 231, 100, 47
377673686778931, 354121036736638, 542473292513394 @ -227, -306, -707
296848971806388, 262260425082633, 321158985267228 @ -56, 126, -22
232846467521218, 403169537435113, 411151731568908 @ 32, -91, -161
354709312583660, 397993171752935, 267149522325782 @ -122, -60, 28
300749577870604, 191958468860593, 148344100763520 @ 96, -411, 904
332722763012353, 292265984916433, 277134726385938 @ -117, -179, -51
167910771002623, 298242589769759, 429293149746155 @ 117, 43, -186
273582225482888, 181380169922993, 205303879579928 @ 115, 21, 184
249104929389895, 368138158130661, 270355480500771 @ -9, 25, 32
30080132751109, 20799127733779, 6459841623423 @ 351, 423, 406
315012088837323, 308303002692584, 380995618346355 @ -73, -30, -172
318317450926774, 175605299669575, 252655288091472 @ -80, -185, -117
376649498970196, 212025459571705, 249995655128076 @ -144, 170, 50
246627493765638, 132507248363935, 218563963344828 @ 257, 230, 131
199462818730446, 310483900177556, 330777095173487 @ 64, 46, -48
394169310319819, 512587717397326, 380405805555343 @ -249, -604, -264
263520954389704, 533462525239843, 34305100586838 @ -24, -136, 266
276885882297140, 316232630441731, 278454882837940 @ -22, 8, 7
312944572330204, 188803145116761, 194195166175468 @ -69, 156, 136
255683812306414, 300904839987157, 343819797521736 @ 23, -17, -111
275090226680851, 175205420175523, 134429572393029 @ 99, 59, 470
322103505857873, 355373071203678, 338467993577903 @ -91, -480, -276
314490621164170, 184993030512257, 289368545154398 @ -69, 117, -74
309044750883893, 191041176971338, 360657718653658 @ -37, -34, -515
383951497804900, 393527809270417, 246108287492148 @ -145, -5, 56
346785682749368, 262788638240913, 279278190844758 @ -184, -243, -106
252420367525238, 228569272027247, 375147379981780 @ 112, -33, -345
265835825900479, 35686184838964, 238008545979354 @ 95, 562, 49
284045256648308, 163634786635308, 256733969131933 @ 130, 28, -84
243703144605026, 219896762870325, 272110842326224 @ 79, 67, -15
375568859304604, 260115131827813, 221265914715576 @ -152, 94, 84
322873295102682, 191140575823109, 263000496307816 @ -104, -95, -101
290060756460076, 221125345828552, 283919983437693 @ -6, 20, -64
328452627139614, 206885606027599, 216896127370240 @ -131, -154, 145
206480404222884, 220049434143633, 355299013894516 @ 85, 129, -110
278127874991212, 322978260851489, 508030769194788 @ -39, 75, -199
284010095446298, 227536681771148, 277615963358653 @ 76, -198, -138
297836578997278, 313393007921083, 281258279387298 @ -37, -114, -30
139073348509043, 341054649866045, 288649016496124 @ 97, 57, 15
277501189138300, 204317392553755, 241510824840750 @ 154, -189, 13
253027944648777, 252168682546692, 341469996573262 @ 13, 90, -83
315105951815881, 360996791916015, 272158243599397 @ -75, 31, 30
267270042237412, 81491153471185, 167059392009780 @ 216, 516, 443
285451561997016, 174402052880193, 385772758290654 @ -26, 189, -175
247069436926813, 289904466751308, 254360826314482 @ 27, 24, 37
308089566178215, 159148182312608, 236496835988006 @ 35, -126, 13
318890512821982, 141245148105745, 252285507275991 @ -84, 141, -86
309060131524332, 327380843942173, 277338418571764 @ -56, -226, -41
298925542932718, 173053785141113, 174091348279958 @ 93, -167, 582
127786384216516, 310318834695145, 242214085223100 @ 150, 46, 58
288901515441928, 315790008496273, 306956515394568 @ -39, 13, -30
10800822803488, 70007523277156, 191739134663829 @ 302, 336, 120
411958970827586, 427965261864487, 227667795078538 @ -205, -142, 76
101239733278868, 65380515853713, 249740607812708 @ 158, 333, 51
306588060794824, 108850449065921, 437319724143572 @ -57, 297, -305
221161118358373, 449133315400241, 246133645530532 @ 27, -83, 55
314036930408933, 176773936324367, 221402102792422 @ -43, -185, 157
291444027110197, 282666639323830, 303824293902673 @ -21, -70, -84
258363540093396, 298618783578471, 232720827728096 @ 10, 12, 69
78630985458154, 149299528609689, 114772397036248 @ 189, 241, 201
308689864136095, 166080142587319, 244557881109828 @ -21, 15, -9
166784624016718, 373338692313928, 15499707411678 @ 72, 22, 285
282156004576403, 362011568240325, 164720413159242 @ -23, -95, 173
205322749799991, 400336501615974, 388528504131735 @ 49, -42, -106
365162478811040, 231121876730282, 281504807141926 @ -170, 60, -27
265803064401396, 255841027554955, 419039516511270 @ -22, 128, -130
337318027903252, 182555564481493, 358399494450888 @ -162, 14, -484
394419093266743, 254454335748369, 375878021108242 @ -153, 141, -71
261697323218993, 85478414867888, 122506019410258 @ 209, 466, 625
210266944582223, 213489706327138, 362339775488478 @ 85, 134, -127
213889601418481, 315329958314764, 283144420738677 @ 85, -30, -10
286191715634736, 486174488718637, 182127625378426 @ -32, -253, 142
298967860681213, 114790370429998, 232151967436368 @ 213, 412, 59
293060200509010, 213583126086463, 255293875276014 @ 13, -56, -16
285131184851668, 434136102394213, 207277410896508 @ -26, -220, 109
267762193825828, 293260759299388, 332020881815988 @ -14, 54, -57
300002817407875, 205732444122688, 245300138015919 @ -17, -6, 24
358233870957043, 417294728275613, 344145903338133 @ -141, -191, -106
293911618776968, 404667764837513, 225560349375948 @ -53, -21, 77
291878943721964, 472174488032873, 357000202952572 @ -20, -501, -207
46104370610735, 110938993604424, 257081314681869 @ 271, 286, 38
268370173938174, 332921033436668, 425555817957894 @ 28, -176, -343
518299952806428, 340777371893997, 549877723217008 @ -298, 31, -279
256194036301578, 227075856000003, 285881852816578 @ 73, 18, -62
318376038006034, 185768503318369, 187458499985544 @ -81, -379, 533
269678085234921, 178329811310920, 288656707623308 @ 91, 80, -129
46231231855237, 38110670253433, 211996072394805 @ 301, 389, 98
315611808181344, 140792049850897, 255289904469928 @ -35, -19, -344
368527333049833, 305045391382038, 205381003181823 @ -177, -86, 122
257797741834321, 492022879013754, 197243979319369 @ 51, -518, 144
313551426696452, 200366353210444, 218170422362349 @ -46, -268, 164
305925916032343, 314773019586738, 177837275443758 @ -63, 34, 137
324228468809476, 169196157911505, 206301816284092 @ -90, 181, 120
272870379386419, 158902397955989, 477107450732146 @ 21, 193, -467
206568398379753, 355147212090226, 264460399539746 @ 77, -52, 25
377684946955978, 337590919430625, 308551813114340 @ -183, -107, -65
268074520148888, 291768415769613, 293755004975648 @ 19, -56, -50
310172758668286, 134913671989395, 236080601998476 @ 63, 78, -13
218628610042237, 296649830601064, 182088470368722 @ 31, 80, 125
19182646333197, 168874909752808, 167808134696564 @ 223, 224, 135
106865227799358, 46511070403279, 46029857491876 @ 232, 383, 343
199854261594314, 316079939430199, 334093616732350 @ 44, 71, -35
334984924895828, 236929105231393, 152065096623508 @ -127, -58, 301
307638012223417, 148067892078010, 242326214886981 @ 45, -12, -58
269494206787810, 273687501169267, 226911777518892 @ 53, -134, 83
340635965017420, 241078669807375, 306105041378538 @ -170, -208, -234
233413242414052, 338528048526541, 199609249694052 @ 18, 26, 107
150433333787074, 447383011174993, 260652968832819 @ 88, -51, 42
330059923043404, 273799894435813, 299852559880064 @ -96, 44, -32
248772553813924, 328532453014175, 244360584451560 @ 18, -14, 53
346761719713282, 463788049736134, 499286867465694 @ -136, -418, -471
304368692804038, 146836710758898, 222731649809373 @ 108, -38, 188
202375570634813, 71889217147728, 344443855653 @ 203, 396, 632
287645772009343, 283179062953988, 340965996375558 @ -33, 34, -91
298794651016796, 316408361328461, 403545669661012 @ -52, 10, -161
253876111366387, 169929693789157, 290007067130508 @ 141, 113, -129
261429881602139, 396978498349532, 297954735346806 @ 19, -198, -43
117567907565632, 49354751824830, 309828921745296 @ 198, 372, -37
457471830312128, 298003790550089, 496187075840662 @ -248, 57, -252
53602655983968, 55949645502652, 44105680759722 @ 422, 398, 425
248402890040372, 221875337890194, 369495059899434 @ 34, 112, -151
299854943781744, 140837881762861, 248410080158950 @ -32, 227, 28
158799653740712, 96839420132932, 61996445459359 @ 254, 326, 424
420416769577594, 417083571845281, 221036927060154 @ -187, -43, 82
285880336232074, 281936996850299, 327995202109890 @ -39, 78, -46
254597169532978, 434818691341741, 266529168098364 @ -13, -49, 35
308078222421788, 245341522015941, 366535092165888 @ -68, 148, -64
397968419439819, 462741172692753, 487394508651992 @ -229, -371, -413
170648022116830, 419073461567389, 267035060795943 @ 108, -103, 26
297163926466952, 171225408844493, 243650808366644 @ 31, 24, 7
321138958312204, 164356132527991, 293194588257924 @ -106, -100, -497
409313928490660, 379458671205457, 374713795172724 @ -197, -64, -116
300193693260508, 151611923410873, 231363386790708 @ 185, -134, 71
258357201611452, 179467531380255, 271971850201618 @ 150, 58, -84
297031916086138, 275029013303593, 287194290948048 @ -35, -39, -43
289708982173813, 223870601653633, 185675354964678 @ -37, 125, 137
307185576204588, 198655687895465, 200828364415844 @ -43, 30, 169
256911055373884, 280357332033709, 275369971431900 @ 36, -22, -11
306709264263570, 238442150683666, 281267663196030 @ -52, 8, -43
286464292265568, 186356579015985, 179134234893176 @ 97, -75, 360
283557175542224, 200258505822133, 234019830313496 @ 65, -46, 60
279561532140463, 356064613024834, 57630778043340 @ -23, -62, 319
301460992753401, 347607367158274, 241485964190314 @ -55, -40, 57
357340427865232, 210688918673389, 480578573086860 @ -181, 42, -583
202788612975133, 491908562228803, 204355634201098 @ 33, -85, 97
327616003378718, 459068751697113, 245400320323708 @ -97, -399, 43
295425019303712, 142143743177621, 213554448049114 @ 76, 147, 192
298023310169294, 111008880266745, 291266763415108 @ 56, 357, -329
239353086932013, 140443180162865, 427954029728115 @ 77, 237, -316
310713620350860, 171430851756295, 263000744102950 @ 26, -397, -375
297485479746376, 227479103669087, 317483649342272 @ 78, -513, -581
311356855893788, 164423783656076, 256279502936024 @ -38, 30, -77
264066237011308, 14766158486881, 283673021139228 @ 237, 907, -234
258092796009004, 170028902701681, 248890934864484 @ 11, 201, 45
210074236661468, 216649922327625, 40389852921772 @ 172, 55, 513
239367977902503, 188834295084773, 175058220889488 @ 73, 145, 179
320309866946626, 237986807885359, 358634619887199 @ -92, -449, -732
350498989422628, 464935100123281, 266549267567796 @ -113, -99, 33
233990390695054, 249869486910925, 283261867856904 @ 191, -133, -95
265539301213518, 363388191968713, 282102901394108 @ -20, 5, 15
272467604038088, 306168350558213, 240590578604268 @ 11, -86, 53
306960548670948, 230204613282241, 231363386790708 @ -38, -112, 71
305142746347068, 186338959082833, 232010796540278 @ -38, 77, 69
215095836844361, 238852123693907, 332329031097739 @ 125, 43, -128
133789998000940, 378603055774831, 165255439723986 @ 106, 15, 137
241004824955696, 288978861717896, 306089724100538 @ 118, -150, -119
135753022324588, 258915085506591, 202999710499660 @ 102, 136, 99
316511527152200, 308189375824335, 450112251588826 @ -74, -197, -483
201422022564550, 304603476898213, 384115476319446 @ 116, -31, -183
296792644588708, 205371718970257, 232866795973044 @ 7, -55, 65
238866855133236, 328974411994241, 306850487797580 @ 28, -5, -30
278130632017764, 192869404769073, 236982805288932 @ 50, 49, 53
224327989074201, 356955791332608, 266770375757634 @ 65, -86, 17
260685225900868, 227517910911793, 281440713023508 @ 157, -154, -134
302044151543518, 189027090832163, 148128818586008 @ 45, -228, 709
175403394981328, 391330418248314, 226607135245470 @ 102, -68, 77
376761503791780, 418312416475585, 320913192640500 @ -154, -112, -45
215462196262294, 360053686369355, 415014825348072 @ 36, 7, -133
367608961555108, 422327369845133, 267470276532008 @ -126, -20, 36
256319169806893, 269600675363038, 351453849457683 @ 83, -110, -242
229940425526428, 321858476763233, 183281287256868 @ 54, -27, 143
329778101182308, 222359765812369, 186075642395828 @ -118, -67, 226
281939375837623, 250297735336363, 296940645141078 @ -35, 119, -7
336952119813664, 111066803315281, 192000927364212 @ -101, 285, 119
270499391495361, 239479828377837, 490100545092670 @ -7, 97, -315
299094264870244, 100781003904337, 261780684230900 @ 90, 476, -198
284722201505403, 258006590083518, 276084378319558 @ 19, -120, -59
217898593927156, 251354833300009, 303296354162932 @ 78, 71, -41
306656387348308, 184831596964783, 219112078944108 @ -22, -28, 131
322591991113804, 291851727255379, 232488649234542 @ -86, -29, 69
247550679827482, 199839497788069, 290998873575358 @ 129, 47, -104
311396653848556, 158724060856159, 228929100430740 @ -34, 42, 87
192308807793543, 64973264870656, 41722631599898 @ 247, 422, 561
'''.strip('\n').splitlines()

# data=data1;start=7;end=27
data=data2;start=200000000000000;end=400000000000000

#data = [int(line) for line in data]
data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]
#data = [[column for column in line] for line in data]
#data = [threading.Thread(target=lambda line: print(line), args=(line)) for line in data] #line.start() line.join()
# W,H=len(data[0]),len(data)


# answer=0
# (x1, y1, z1, dx1, dy1, dz1) = data[0]
# (x2, y2, z2, dx2, dy2, dz2) = data[1]
# (x3, y3, z3, dx3, dy3, dz3) = data[3] #skipped one
#
# p1=[x1, y1, z1]
# d1=[dx1, dy1, dz1]
#
# d2=[dx2, dy2, dz2]
#
# p3=[x3, y3, z3]
# d3=[dx3, dy3, dz3]

# x0 + dx0 * t1 = x1 + dx1 * t1
# (x0 - x1) / (dx1 - dx0) = t1
# (x0 - x1) * (dy1 - dy0) = (y0 - y1) * (dx1 - dx0)


# planeNormal = numpy.cross(d1, d2)
# distance=numpy.dot(numpy.subtract(p1, p3), planeNormal) / (numpy.dot(d3, planeNormal))
# print(distance)
# print(p3 + numpy.multiply(d3, distance))

# import z3
# s = z3.Solver(); x = Int('x'); y = Int('y'); s.add(x < 10); print(s, s.check(), s.model() if s.check()==sat else '')
x0,y0,z0,dx0,dy0,dz0=Reals('x0 y0 z0 dx0 dy0 dz0')
equations=[]
# equations=[
# 	x0 >= start, x0 <= end,
# 	y0 >= start, y0 <= end,
# 	z0 >= start, z0 <= end,
# ]
for i, line in enumerate(data[:3]):
	(x1, y1, z1, dx1, dy1, dz1) = line
	tVariable = Real('t' + str(i))
	equations += [
		tVariable > 0,
		x0 + dx0 * tVariable == x1 + dx1 * tVariable,
		y0 + dy0 * tVariable == y1 + dy1 * tVariable,
		z0 + dz0 * tVariable == z1 + dz1 * tVariable,
	]
s = z3.Solver()
s.add(equations)
print(s)
print(s.check())
if s.check() == sat:
	print(int(str(s.model()[x0])), int(str(s.model()[y0])), int(str(s.model()[z0])))
	print(int(str(s.model()[x0])) + int(str(s.model()[y0])) + int(str(s.model()[z0])))

# x0 + dx0 * t1 = x1 + dx1 * t1
# y0 + dy0 * t1 = y1 + dy1 * t1
# z0 + dz0 * t1 = z1 + dz1 * t1



# answer=0
# for i in range(len(data)):
# 	for j in range(i+1,len(data)):
# 		line1=data[i]
# 		line2=data[j]
# 		(x1, y1, z1, dx1, dy1, dz1) = line1
# 		(x2, y2, z2, dx2, dy2, dz2) = line2
#
# 		if dy1/dx1 == dy2/dx2: continue
# 		x = ((y2 - dy2/dx2 * x2) - (y1 - dy1/dx1 * x1)) / (dy1/dx1 - dy2/dx2)
# 		y = (dy1 / dx1) * x + (y1 - (dy1 / dx1) * x1)
# 		t1 = (y - y1) / dy1 if dy1 != 0 else (x - x1) / dx1
# 		t2 = (y - y2) / dy2 if dy2 != 0 else (x - x2) / dx2
#
# 		if t1<0 or t2 < 0:
# 			continue
# 		if start <= x <= end and start <= y <= end:
# 			answer+=1
#
# print(answer)




# fit_params = lmfit.Parameters()
# fit_params['x'] = lmfit.Parameter('x', value=24, min=0, max=end)
# fit_params['y'] = lmfit.Parameter('y', value=13, min=0, max=end)
# fit_params['z'] = lmfit.Parameter('z', value=10, min=0, max=end)
# fit_params['dx'] = lmfit.Parameter('dx', value=-3, min=-500, max=500)
# fit_params['dy'] = lmfit.Parameter('dy', value=1, min=-500, max=500)
# fit_params['dz'] = lmfit.Parameter('dz', value=2, min=-500, max=500)
# LARGE=1000000000000000000
#
# def myfunc(params, *args, **kws):
# 	# x1 = params['x'].value
# 	# y1 = params['y'].value
# 	# z1 = params['z'].value
# 	# dx1 = params['dx'].value
# 	# dy1 = params['dy'].value
# 	# dz1 = params['dz'].value
# 	# x1=24;y1=13;z1=10;dx1=-3;dy1=1;dz1=2
# 	(x1, y1, z1, dx1, dy1, dz1) = params
# 	residuals = []
# 	for line in data:
# 		(x2, y2, z2, dx2, dy2, dz2) = line
# 		residual=0
# 		tx = (x2 - x1) / (dx1 - dx2) if dx1 != dx2 else None
# 		# if tx is None and x1 != x2:
# 		# 	residuals.append(LARGE)
# 		# 	continue
# 		ty = (y2 - y1) / (dy1 - dy2) if dy1 != dy2 else None
# 		# if ty is None and y1 != y2:
# 		# 	residuals.append(LARGE)
# 		# 	continue
# 		tz = (z2 - z1) / (dz1 - dz2) if dz1 != dz2 else None
# 		# if tz is None and z1 != z2:
# 		# 	residuals.append(LARGE)
# 		# 	continue
# 		if tx is not None and ty is not None:
# 			residual += (tx - ty) * (tx - ty)
# 		if tx is not None and tz is not None:
# 			residual += (tx - tz) * (tx - tz)
# 		if tz is not None and ty is not None:
# 			residual += (tz - ty) * (tz - ty)
# 		residual = math.sqrt(residual)
# 		residuals.append(residual)
# 	print(x1, y1, z1, dx1, dy1, dz1, sum(residuals))
# 	return sum(residuals)

# result = lmfit.minimize(myfunc, fit_params, method='basinhopping', args=(data), max_nfev=0)
# print(lmfit.fit_report(result))

# from scipy.optimize import basinhopping
# x0 = (end//2, end//2, end//2, 10, 20, 30)
# minimizer_kwargs = {"method": "BFGS"}
# ret = basinhopping(myfunc, x0, minimizer_kwargs=minimizer_kwargs, niter=100)
# print(ret)
# print(myfunc(ret.x))
# from sympy import *
# x0,y0,z0,dx0,dy0,dz0=symbols('x0 y0 z0 dx0 dy0 dz0')
# tVariables=symbols('t1 t2 t3 t4 t5')
# equations=[
# 	x0-24,
# 	y0-13,
# 	z0-10,
# 	dx0--3,
# 	dy0-1,
# 	dz0-2,
# 	tVariables[0]-5,
# ]
# for i, line in enumerate(data):
# 	(x1, y1, z1, dx1, dy1, dz1) = line
# 	equations += [
# 		(x0 - x1) + tVariables[i] * (dx0 - dx1),
# 		(y1 - y0) + tVariables[i] * (dy0 - dy1),
# 		(z1 - z0) + tVariables[i] * (dz0 - dz1),
# 	]
# print(equations)
# print(nsolve(equations, [x0, y0, z0, dx0, dy0, dz0], [0, 0, 0, 0, 0, 0]))
# t2=symbols('t2	')
# (x2, y2, z2, dx2, dy2, dz2) = data[1]
