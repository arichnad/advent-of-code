#!/usr/bin/python3

#top of first star
data0='''
on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10
'''.strip().splitlines()
#bottom of first star, trimmed
data1='''
on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
'''.strip().splitlines()
#second star, trimmed
data2='''
on x=-5..47,y=-31..22,z=-19..33
on x=-44..5,y=-27..21,z=-14..35
on x=-49..-1,y=-11..42,z=-10..38
on x=-20..34,y=-40..6,z=-44..1
off x=26..39,y=40..50,z=-2..11
on x=-41..5,y=-41..6,z=-36..8
off x=-43..-33,y=-45..-28,z=7..25
on x=-33..15,y=-32..19,z=-34..11
off x=35..47,y=-46..-34,z=-11..5
on x=-14..36,y=-6..44,z=-16..29
'''.strip().splitlines()
#second star, untrimmed
data3='''
on x=-5..47,y=-31..22,z=-19..33
on x=-44..5,y=-27..21,z=-14..35
on x=-49..-1,y=-11..42,z=-10..38
on x=-20..34,y=-40..6,z=-44..1
off x=26..39,y=40..50,z=-2..11
on x=-41..5,y=-41..6,z=-36..8
off x=-43..-33,y=-45..-28,z=7..25
on x=-33..15,y=-32..19,z=-34..11
off x=35..47,y=-46..-34,z=-11..5
on x=-14..36,y=-6..44,z=-16..29
on x=-57795..-6158,y=29564..72030,z=20435..90618
on x=36731..105352,y=-21140..28532,z=16094..90401
on x=30999..107136,y=-53464..15513,z=8553..71215
on x=13528..83982,y=-99403..-27377,z=-24141..23996
on x=-72682..-12347,y=18159..111354,z=7391..80950
on x=-1060..80757,y=-65301..-20884,z=-103788..-16709
on x=-83015..-9461,y=-72160..-8347,z=-81239..-26856
on x=-52752..22273,y=-49450..9096,z=54442..119054
on x=-29982..40483,y=-108474..-28371,z=-24328..38471
on x=-4958..62750,y=40422..118853,z=-7672..65583
on x=55694..108686,y=-43367..46958,z=-26781..48729
on x=-98497..-18186,y=-63569..3412,z=1232..88485
on x=-726..56291,y=-62629..13224,z=18033..85226
on x=-110886..-34664,y=-81338..-8658,z=8914..63723
on x=-55829..24974,y=-16897..54165,z=-121762..-28058
on x=-65152..-11147,y=22489..91432,z=-58782..1780
on x=-120100..-32970,y=-46592..27473,z=-11695..61039
on x=-18631..37533,y=-124565..-50804,z=-35667..28308
on x=-57817..18248,y=49321..117703,z=5745..55881
on x=14781..98692,y=-1341..70827,z=15753..70151
on x=-34419..55919,y=-19626..40991,z=39015..114138
on x=-60785..11593,y=-56135..2999,z=-95368..-26915
on x=-32178..58085,y=17647..101866,z=-91405..-8878
on x=-53655..12091,y=50097..105568,z=-75335..-4862
on x=-111166..-40997,y=-71714..2688,z=5609..50954
on x=-16602..70118,y=-98693..-44401,z=5197..76897
on x=16383..101554,y=4615..83635,z=-44907..18747
off x=-95822..-15171,y=-19987..48940,z=10804..104439
on x=-89813..-14614,y=16069..88491,z=-3297..45228
on x=41075..99376,y=-20427..49978,z=-52012..13762
on x=-21330..50085,y=-17944..62733,z=-112280..-30197
on x=-16478..35915,y=36008..118594,z=-7885..47086
off x=-98156..-27851,y=-49952..43171,z=-99005..-8456
off x=2032..69770,y=-71013..4824,z=7471..94418
on x=43670..120875,y=-42068..12382,z=-24787..38892
off x=37514..111226,y=-45862..25743,z=-16714..54663
off x=25699..97951,y=-30668..59918,z=-15349..69697
off x=-44271..17935,y=-9516..60759,z=49131..112598
on x=-61695..-5813,y=40978..94975,z=8655..80240
off x=-101086..-9439,y=-7088..67543,z=33935..83858
off x=18020..114017,y=-48931..32606,z=21474..89843
off x=-77139..10506,y=-89994..-18797,z=-80..59318
off x=8476..79288,y=-75520..11602,z=-96624..-24783
on x=-47488..-1262,y=24338..100707,z=16292..72967
off x=-84341..13987,y=2429..92914,z=-90671..-1318
off x=-37810..49457,y=-71013..-7894,z=-105357..-13188
off x=-27365..46395,y=31009..98017,z=15428..76570
off x=-70369..-16548,y=22648..78696,z=-1892..86821
on x=-53470..21291,y=-120233..-33476,z=-44150..38147
off x=-93533..-4276,y=-16170..68771,z=-104985..-24507
'''.strip().splitlines()
#real
data4='''
on x=-7..46,y=-33..20,z=-18..35
on x=-30..15,y=-49..0,z=-45..4
on x=-8..43,y=-37..11,z=-35..16
on x=-47..5,y=-29..25,z=-14..40
on x=-42..9,y=-22..25,z=-19..34
on x=-2..43,y=0..48,z=-21..31
on x=-31..16,y=-37..8,z=-20..33
on x=-49..-2,y=-6..42,z=-38..8
on x=-28..20,y=-23..25,z=0..49
on x=-38..9,y=-24..27,z=-46..-1
off x=-26..-17,y=-40..-29,z=19..30
on x=-44..10,y=-5..45,z=-1..43
off x=-7..6,y=-43..-31,z=-40..-21
on x=-31..19,y=-38..8,z=-13..34
off x=-43..-33,y=-8..6,z=-35..-21
on x=-36..18,y=-40..8,z=-5..43
off x=3..18,y=-12..7,z=2..16
on x=-31..21,y=-47..0,z=-13..37
off x=3..20,y=-25..-15,z=36..47
on x=-42..2,y=-37..12,z=-34..14
on x=17182..27777,y=-3224..32211,z=-83520..-69820
on x=-36478..-17600,y=-87666..-59437,z=-29717..5252
on x=-35375..-5332,y=58963..82354,z=-58548..-29438
on x=-79660..-71815,y=12570..33352,z=-13369..9478
on x=-3581..11638,y=3447..15178,z=78271..82991
on x=-28732..-5457,y=-13549..-440,z=69147..93149
on x=7211..14016,y=73958..76098,z=11232..26622
on x=-32794..-27104,y=62586..81224,z=19916..42688
on x=-26418..7728,y=17029..35040,z=-78387..-65296
on x=34675..40291,y=-39100..-18523,z=54280..72153
on x=-66337..-35064,y=-60743..-51833,z=2910..27347
on x=-54043..-42065,y=13429..47844,z=-73994..-38483
on x=-98305..-68993,y=-14308..13072,z=5280..30173
on x=30117..48692,y=21144..41848,z=-71520..-48131
on x=-21081..-2320,y=56156..76713,z=-64122..-39157
on x=-79875..-64249,y=28448..48945,z=1967..18595
on x=56776..76217,y=-41516..-19616,z=28927..47003
on x=6624..27937,y=-45590..-25488,z=51348..72678
on x=-74468..-64170,y=19919..45774,z=-18124..8803
on x=-6934..12496,y=6893..23925,z=-84297..-77488
on x=-13522..4546,y=-96987..-64778,z=2079..19539
on x=38976..56544,y=2517..15251,z=-74977..-45634
on x=26918..43893,y=-72127..-51551,z=-49848..-33134
on x=-13809..18426,y=15753..21701,z=-87709..-64986
on x=-69466..-51406,y=31057..54439,z=-46120..-41440
on x=31687..48030,y=-22591..-11803,z=-70591..-55788
on x=-75996..-55750,y=22812..40769,z=29362..45333
on x=-70470..-57403,y=-2580..11624,z=24192..50897
on x=50230..72839,y=-52817..-27782,z=13647..35032
on x=25548..39751,y=-52598..-16384,z=55090..70945
on x=-70324..-41666,y=9734..44489,z=34448..59651
on x=-47154..-21227,y=43490..52037,z=54633..69702
on x=56594..79815,y=-35549..-27387,z=-27700..-19721
on x=-2302..16784,y=19088..32316,z=-75528..-62618
on x=-55567..-43654,y=48636..61742,z=-49940..-18662
on x=-7703..20434,y=-78193..-58599,z=-35157..-9113
on x=12785..36975,y=-33552..-7422,z=-84933..-70220
on x=-24641..-8516,y=46864..66364,z=31866..60107
on x=-70394..-39717,y=-70527..-54064,z=-20469..-1337
on x=6978..15640,y=-8317..9304,z=-86320..-78697
on x=6443..20493,y=-85309..-62516,z=14278..43203
on x=-61835..-47060,y=-18144..2229,z=-68867..-53043
on x=-45523..-20721,y=-13682..9350,z=69934..77504
on x=37733..56409,y=47339..65015,z=-18477..4468
on x=-16164..7151,y=-13471..10696,z=73653..89080
on x=-41319..-23267,y=15325..36810,z=-77145..-58066
on x=-44967..-8854,y=28744..41940,z=-77425..-47861
on x=-29728..-14932,y=-19748..-3741,z=-92874..-75780
on x=-65558..-35851,y=-75363..-58225,z=13348..44088
on x=-960..12429,y=55983..78816,z=-51429..-32076
on x=-47514..-17615,y=-29997..2539,z=59654..76894
on x=56568..69044,y=33679..50180,z=7652..28576
on x=29866..59131,y=-71033..-58322,z=5414..18583
on x=-57898..-33002,y=-64590..-31574,z=-55650..-43146
on x=11236..22902,y=23098..34629,z=-83121..-53733
on x=-39884..-27624,y=51200..78948,z=-47118..-31319
on x=-92815..-58269,y=-16907..-1704,z=-29286..-24343
on x=22187..50208,y=59504..83740,z=1997..17041
on x=-36904..-15694,y=70204..88777,z=-28255..-2817
on x=23121..40417,y=-16610..-5799,z=-78627..-62157
on x=-2994..16806,y=68203..84975,z=-53466..-23177
on x=2604..27746,y=-91072..-63999,z=-10762..8989
on x=51223..75145,y=-68640..-37800,z=-22437..-683
on x=-15717..6990,y=-73772..-57247,z=-68389..-54529
on x=-45526..-13483,y=-13358..3939,z=-85615..-58166
on x=-96511..-73154,y=-26092..629,z=-21897..-1733
on x=-55811..-38069,y=56217..75310,z=-46041..-32717
on x=61118..77746,y=-46359..-31556,z=-24975..-8394
on x=18510..48713,y=46958..76753,z=39973..53735
on x=34009..47986,y=24340..43235,z=-69086..-44744
on x=-44060..-26618,y=-48990..-21046,z=42113..61150
on x=66647..79443,y=-43972..-31017,z=-16328..-4262
on x=24442..34004,y=60830..92395,z=-27041..-955
on x=-69561..-56114,y=-61232..-34832,z=-3746..14357
on x=-50412..-14776,y=54769..67588,z=-42918..-11247
on x=-15310..-103,y=34031..59275,z=60082..66618
on x=30234..63610,y=-21540..-1233,z=-62390..-46739
on x=46230..72592,y=-33120..-16455,z=-58459..-21529
on x=19995..40731,y=-74178..-43554,z=-54752..-22989
on x=59652..73982,y=-14790..-1765,z=-58396..-34021
on x=42309..74687,y=-63691..-47745,z=5208..21003
on x=39068..69165,y=-65965..-47211,z=-25101..3048
on x=41248..51790,y=-77592..-49712,z=-22340..3260
on x=-11901..22879,y=-86890..-72453,z=6881..34015
on x=-69069..-60091,y=23487..51609,z=-43810..-18500
on x=-48674..-27819,y=52775..74703,z=25413..26302
on x=-4791..19071,y=-43534..-21156,z=69601..77380
on x=20809..36359,y=37662..63446,z=37035..67799
on x=-12057..-2718,y=-22207..6901,z=-96095..-70733
on x=-74355..-52739,y=-39725..-5837,z=-28298..-22197
on x=-98346..-69880,y=6282..27880,z=-4156..3436
on x=-9008..11304,y=68001..80742,z=-20906..2153
on x=-63565..-41030,y=20425..52102,z=49021..59565
on x=-7902..4294,y=-4924..15150,z=68155..94418
on x=52359..77544,y=16232..52370,z=-48563..-28378
on x=-13757..7808,y=33879..45463,z=63305..82942
on x=-16491..9208,y=-80919..-47812,z=34961..49155
on x=36841..57067,y=-571..21963,z=40505..54045
on x=68324..77659,y=-25223..3699,z=28673..50202
on x=1302..36058,y=-87432..-65507,z=-36083..-16460
on x=33264..49226,y=45587..69917,z=-46634..-18202
on x=-56546..-41720,y=-36103..-15538,z=-60749..-44004
on x=-2829..25557,y=-69860..-50747,z=40192..67584
on x=55885..81133,y=9621..18991,z=-47377..-27098
on x=-42249..-32979,y=-41099..-16682,z=-68298..-50327
on x=55206..76112,y=-49835..-39130,z=1519..20458
on x=30367..47813,y=-75593..-53288,z=-42727..-25538
on x=-55278..-29317,y=-59325..-21332,z=-63511..-52575
on x=-21803..4177,y=42516..43627,z=-69116..-61347
on x=-1614..14650,y=-82433..-54921,z=-48812..-25782
on x=-47111..-37497,y=65342..71455,z=-5460..15797
on x=23754..31721,y=37758..52976,z=-71858..-45997
on x=-38581..-15122,y=-78697..-62998,z=-56043..-30425
on x=42157..71556,y=-67782..-42291,z=-32273..-5140
on x=27986..52620,y=35934..56285,z=-49718..-36419
on x=-108..21335,y=-89058..-64818,z=-40166..-22927
on x=-18214..-3768,y=-81820..-66701,z=-34616..-15524
on x=-33261..-13126,y=-14716..5485,z=72825..81925
on x=6485..20487,y=17218..21519,z=-87428..-61474
on x=26033..36018,y=41729..71758,z=31174..57062
on x=-53153..-40128,y=46567..54186,z=-58111..-32668
on x=-69087..-48433,y=34549..65368,z=25921..45656
on x=-93358..-71648,y=1023..8407,z=-38498..-6765
on x=-25312..-10622,y=-47123..-33445,z=-80570..-67688
on x=-31677..-24523,y=12358..37315,z=53512..70844
on x=-44012..-24469,y=-75641..-72368,z=-22193..-15627
on x=33456..56770,y=44076..71278,z=-2981..24210
on x=-4458..27229,y=-47404..-29743,z=-76192..-47479
on x=59149..96559,y=-32143..-1818,z=-4472..-2946
on x=62398..89037,y=-9482..22868,z=-7434..17472
on x=-59815..-39368,y=44008..66200,z=42677..64431
on x=32320..52952,y=-23766..-1371,z=52992..76447
on x=-12864..10818,y=1524..32265,z=71955..84281
on x=20742..40944,y=-21436..5617,z=68065..88332
on x=-24441..-11782,y=-33466..-14205,z=55689..86476
on x=-77127..-52756,y=-52495..-20262,z=5770..20148
on x=12732..49128,y=-39557..-23797,z=-71252..-51598
on x=-84203..-69021,y=-28423..-15185,z=4681..22649
on x=-69456..-63651,y=-44532..-26624,z=-28305..-15187
on x=32317..53966,y=38..12702,z=55404..69365
on x=24880..61956,y=-82234..-61193,z=-21026..-10548
on x=-1061..12744,y=-82133..-63313,z=-27614..-4215
on x=-14054..3095,y=-81132..-71880,z=-22971..8726
on x=-43699..-33307,y=-47003..-29957,z=46904..63739
on x=17412..41045,y=49919..68162,z=28261..52962
on x=61470..79044,y=-47060..-27933,z=-33939..-22872
on x=58351..75872,y=20582..50923,z=15105..35525
on x=14507..37547,y=-9858..15365,z=58243..83999
on x=-34092..-10984,y=-38413..-9135,z=70859..77030
on x=-60878..-39819,y=56642..78685,z=-229..22087
on x=-34750..-5350,y=55713..90558,z=20209..33089
on x=-44471..-10325,y=-88305..-56912,z=14271..31356
on x=45779..77191,y=33171..40355,z=27638..33807
on x=-24060..-16636,y=-62641..-48339,z=28289..61692
on x=40641..63374,y=17751..35713,z=46084..63175
on x=47371..66302,y=-64709..-41736,z=4564..29478
on x=49408..68868,y=-35982..-15014,z=-46381..-23458
on x=-15382..9867,y=-81650..-73896,z=28044..39913
on x=27738..54131,y=-8128..9269,z=60847..74673
on x=-78556..-55048,y=-3481..6203,z=-45616..-20226
on x=-13209..12365,y=22498..50456,z=67047..81521
on x=-15153..-6795,y=-59212..-52714,z=-73671..-51795
on x=57296..74764,y=10632..40873,z=-42501..-23656
on x=58047..85893,y=-36494..-33138,z=-1226..18046
on x=22298..38077,y=55987..85711,z=-30418..-5219
on x=73540..88814,y=1369..15648,z=7563..27864
on x=67040..93226,y=-22490..2342,z=10842..20866
on x=226..19647,y=64201..72346,z=30655..44876
on x=-27779..1609,y=-67071..-52549,z=46634..54706
on x=5829..18497,y=-54327..-31877,z=-70018..-49794
on x=-23415..-4742,y=-64568..-56745,z=49515..67395
on x=-55266..-36457,y=17775..38943,z=-68636..-62342
on x=2630..15492,y=-9238..15357,z=79129..98406
on x=-39108..-20386,y=-73809..-55499,z=39081..43959
on x=6784..22043,y=41440..68472,z=34432..55724
on x=-76809..-59369,y=26029..29781,z=35484..55857
on x=-25794..-7227,y=-11719..18176,z=-83988..-74929
on x=50084..59497,y=41170..74864,z=9910..19884
on x=-32039..-5643,y=38964..49536,z=-67378..-60755
on x=745..27265,y=-82137..-59824,z=-21560..8852
on x=6287..18493,y=-55848..-29680,z=-62740..-57893
on x=-64509..-39018,y=-4218..10719,z=48009..64204
on x=-41883..-16748,y=-79063..-59658,z=-22206..-11066
on x=47544..85654,y=-702..20825,z=37459..55666
on x=-29..5311,y=18141..37208,z=-81625..-71631
on x=-41865..-19390,y=23515..55131,z=-61821..-51754
on x=28744..44562,y=186..17932,z=65483..76912
on x=14096..31855,y=69666..75601,z=-43400..-12004
on x=71393..86894,y=-20769..12842,z=-34842..-18657
on x=-63837..-42971,y=-4175..3950,z=-67678..-53473
on x=1348..21274,y=63670..80764,z=-24853..-9847
on x=-31280..-3068,y=-39466..-6496,z=63779..85540
on x=-974..12100,y=41578..51260,z=-70442..-60355
on x=-44572..-25319,y=18821..31784,z=64602..71923
on x=75077..93916,y=-10647..6085,z=-12286..4544
on x=38548..65005,y=-65881..-48510,z=-7182..13905
on x=-25504..8575,y=-35235..-33764,z=-83283..-69233
on x=3422..12071,y=36160..47301,z=66275..78894
on x=-25900..6751,y=61333..80663,z=28797..48512
on x=1852..12603,y=-446..23209,z=77219..94923
on x=-36473..-15442,y=-64055..-39900,z=-67808..-46265
off x=-60472..-46531,y=15867..24753,z=-66777..-52378
off x=-30272..-8137,y=-67428..-48297,z=-73430..-42993
off x=-9301..14801,y=-271..21859,z=-83994..-68351
off x=-76950..-50595,y=-22980..-18508,z=33206..37639
on x=38817..42972,y=59836..69308,z=14244..23211
on x=50995..69892,y=-51441..-25446,z=27917..38990
off x=28846..52680,y=-20614..11792,z=64516..82317
on x=20530..48749,y=58214..80086,z=-39596..-30073
on x=-705..19215,y=29573..35467,z=-79099..-60409
on x=52399..78552,y=-22208..-10356,z=34173..53622
on x=46301..72685,y=-60452..-46126,z=2165..20407
off x=15160..31733,y=-58733..-48899,z=-75205..-51952
off x=-56198..-32552,y=-32638..-19543,z=-68768..-50289
on x=31070..54471,y=-55815..-26128,z=-59517..-50367
off x=29143..49895,y=-50445..-28074,z=56045..64123
off x=-63817..-36474,y=42696..55629,z=-46684..-14834
off x=-29936..-11819,y=59590..83212,z=16015..29258
on x=-64096..-37567,y=-64655..-42170,z=-23895..-11223
on x=-31675..-1925,y=67937..83417,z=-17305..-4914
on x=-37460..-27355,y=53562..73812,z=-38699..-20364
on x=-14501..4990,y=-11118..21439,z=-93235..-78372
off x=-4948..5139,y=-24052..-1844,z=-90630..-72155
off x=71278..90193,y=-10302..-4245,z=-21676..-729
off x=2062..24465,y=-90904..-67695,z=-18872..7057
on x=63511..78569,y=-25734..-11639,z=-11933..-124
off x=-58584..-38674,y=-28068..-4798,z=-72514..-59657
on x=27716..42112,y=57178..88151,z=2259..34728
on x=-32865..-12200,y=-72880..-65048,z=21687..40726
off x=63618..84337,y=-33711..-3403,z=14460..33990
on x=-75090..-62281,y=-43893..-21745,z=-949..12353
on x=-24390..-16065,y=14934..22095,z=-81173..-68902
off x=-16076..14313,y=-52917..-46105,z=-76264..-55664
on x=10901..24562,y=-81592..-64181,z=-17893..-6228
off x=-72452..-52842,y=25333..55715,z=-29901..-8246
off x=5095..20327,y=18626..46134,z=68692..78197
off x=28454..44029,y=55326..64383,z=-44477..-18272
on x=71576..84867,y=3816..22755,z=-38259..-22117
off x=53125..77783,y=-52338..-25340,z=-1655..11640
on x=24854..37185,y=-64424..-49729,z=47988..53011
off x=24368..54577,y=53812..83310,z=19342..39205
on x=49067..65941,y=-59534..-37177,z=-51376..-17156
off x=-81708..-63718,y=-13225..2506,z=-11775..5530
off x=17312..52223,y=-44045..-27002,z=-68420..-45989
off x=-83213..-73359,y=4971..25263,z=-12422..13852
on x=5505..24012,y=-75124..-69159,z=23345..29615
on x=-17845..5789,y=63235..74123,z=23401..55913
off x=28381..52968,y=-27731..-12148,z=-64226..-61405
on x=-30949..-4597,y=-549..11255,z=-88519..-66064
on x=-27457..1298,y=77383..89419,z=-26797..-4916
on x=19789..41544,y=-4838..29792,z=-92622..-65581
on x=57413..72558,y=-33603..-18448,z=13316..31770
off x=20324..47850,y=-18636..-2250,z=56469..74162
off x=-79506..-75288,y=17658..31052,z=4926..12163
off x=-49517..-21198,y=63734..86245,z=13261..29495
off x=-26956..-3920,y=-91186..-70602,z=-10417..14805
on x=7720..26486,y=-1467..24361,z=67482..84362
off x=-33017..-15305,y=-31540..-19470,z=-76086..-69014
off x=-49278..-31203,y=-1260..17309,z=54444..86573
off x=-65442..-44645,y=26172..37910,z=51101..61603
off x=-37979..-19040,y=-59723..-43276,z=37325..50633
off x=-36502..-15520,y=57666..75891,z=46005..62685
off x=-60972..-50707,y=-37306..-27216,z=36729..69758
on x=-50859..-36895,y=14096..41836,z=53335..74455
off x=23990..43682,y=-68570..-57678,z=9391..17661
off x=-28201..-8862,y=11150..29387,z=-89663..-72480
off x=41213..57481,y=38034..59144,z=-41989..-31178
off x=53337..85593,y=37988..50798,z=812..30567
off x=-84299..-69433,y=-18222..855,z=-25937..-13835
off x=26906..44928,y=-37113..2,z=52060..77646
off x=-7547..4802,y=-43368..-10965,z=71671..82983
on x=-23996..-8142,y=-48337..-26483,z=-66740..-62222
on x=-39770..-15536,y=43939..70538,z=-46718..-21003
off x=-67699..-36417,y=51652..78789,z=-15413..1404
on x=-82025..-58819,y=-27493..-14994,z=-28241..-7991
off x=-32839..-11809,y=25055..57585,z=59394..76524
on x=36694..45443,y=-21409..7272,z=65712..82453
on x=-62687..-38073,y=20067..49092,z=-69417..-50954
on x=-16000..-774,y=-7430..5970,z=68096..90000
off x=-20016..-2552,y=-20464..2097,z=-80825..-60531
off x=-27092..-8022,y=68833..89545,z=-8571..15742
off x=21272..41787,y=12143..24604,z=-89683..-59529
off x=30298..35641,y=-78813..-55757,z=-14812..2414
off x=73709..76840,y=9430..41381,z=-32382..3151
off x=-75658..-61517,y=27614..49093,z=-40522..-9068
on x=70350..95139,y=-32582..-10102,z=6364..20052
off x=27887..49873,y=7864..21619,z=-70233..-47311
on x=15223..33406,y=-36174..-9285,z=65044..78680
off x=4285..10841,y=-47821..-36121,z=64575..77802
off x=-78527..-43558,y=-8165..25534,z=-63172..-34865
on x=2843..12059,y=-17419..11657,z=-81286..-67046
off x=-46514..-19698,y=-11948..4910,z=66899..85255
off x=15133..37295,y=60308..67449,z=15392..40924
on x=52699..74553,y=-18491..5133,z=-65670..-53922
on x=-45047..-33438,y=-63743..-62643,z=-35938..-14466
on x=-44287..-21601,y=-41650..-19897,z=46481..78707
off x=32999..40604,y=-37256..-8001,z=-79041..-61372
off x=-54412..-32287,y=18493..40369,z=54118..74531
off x=-38905..-20481,y=49190..59444,z=40556..59026
on x=16411..40024,y=33912..58879,z=38564..75902
on x=-12591..-2987,y=-78201..-61933,z=-28888..-17148
off x=-4940..1183,y=-88892..-57486,z=-52721..-22774
on x=24099..52912,y=-29333..-5858,z=-82672..-56239
on x=-45132..-32466,y=31259..64105,z=52811..74733
off x=-16721..9718,y=70198..81586,z=-35202..-8603
off x=-17967..1365,y=-72607..-68264,z=-47127..-19316
off x=-38072..-10455,y=-83783..-59061,z=-38568..-12696
off x=-58205..-48576,y=-13344..-7550,z=54334..62877
on x=-37756..-7175,y=37997..57347,z=-80100..-50822
on x=-60364..-51525,y=-25414..5891,z=-61245..-45908
off x=-58279..-33228,y=30140..54997,z=-50309..-32144
off x=53554..71771,y=48625..54563,z=-42551..-18852
on x=43054..56610,y=-14714..4347,z=43183..61907
off x=53063..66718,y=23357..33629,z=-51176..-36914
on x=60145..88796,y=27922..44298,z=-11383..5474
on x=61722..81040,y=29286..36795,z=-8858..28939
on x=8669..30711,y=-14307..7547,z=71165..83446
off x=49048..66832,y=-18738..10802,z=38491..73031
on x=-5685..22511,y=-80543..-66450,z=-21723..-587
off x=-49575..-27204,y=70694..91253,z=-3763..6993
off x=6050..35866,y=-49013..-27124,z=-82444..-68183
on x=-37642..-29807,y=11714..45553,z=-76962..-58273
off x=-86180..-49725,y=-44211..-38021,z=79..15928
on x=-81422..-53495,y=-3439..18777,z=-49139..-26530
on x=21885..39275,y=25066..31796,z=-74538..-66054
on x=41718..58815,y=34134..45049,z=-62295..-48833
off x=54545..70379,y=31847..50351,z=-45744..-15371
off x=-17384..9760,y=66878..95608,z=1325..11213
on x=21546..40994,y=-46135..-34466,z=45991..74186
on x=-74288..-57598,y=-7914..15756,z=37963..71414
off x=58733..80360,y=29101..50184,z=-29236..-10844
on x=46200..52718,y=-51447..-45541,z=-59618..-34940
off x=-52392..-39862,y=-64723..-44522,z=-19127..-685
off x=1098..24830,y=4164..15065,z=-98345..-59655
on x=-59480..-23102,y=51538..68470,z=20149..47380
on x=38105..56989,y=-77417..-49521,z=-9791..7967
on x=-64861..-57166,y=-20289..565,z=34943..56325
off x=-37998..-18718,y=-59668..-34843,z=43312..62116
off x=30540..47369,y=14648..33270,z=46213..77350
on x=-41723..-31099,y=48521..70007,z=-37438..-15586
on x=23470..42466,y=16599..47935,z=-73273..-60442
off x=-41000..-21199,y=-52255..-39493,z=-79003..-49446
off x=-40458..-33831,y=39028..67160,z=-65818..-33660
off x=3635..27361,y=-81879..-53342,z=-63866..-35558
off x=46245..80999,y=-12869..6515,z=31744..52617
on x=34719..47447,y=-22651..-13022,z=-86624..-49801
on x=65042..78064,y=2046..30954,z=-27153..-7213
on x=-24061..5009,y=-21454..2042,z=72307..97852
off x=-16876..16318,y=-63069..-56073,z=40007..75916
off x=-27569..-3747,y=6580..30388,z=74693..77472
off x=-10202..-135,y=-63045..-55195,z=51474..68696
on x=14250..44319,y=-4495..10809,z=70141..78539
off x=35145..50822,y=47602..71060,z=-43832..-11075
off x=-89696..-54720,y=34477..38698,z=-12817..6903
off x=4301..31548,y=-57644..-42340,z=-78475..-48203
on x=49259..78614,y=20709..44619,z=16835..31940
off x=76331..89539,y=-16535..9174,z=-30533..-4900
off x=-38488..-27528,y=-82711..-59253,z=-8606..17299
on x=-28991..-12928,y=7269..39601,z=-81384..-64525
off x=41549..66947,y=40215..62294,z=-43058..-38937
off x=66587..96927,y=-17567..1669,z=-5679..24786
on x=-74535..-52098,y=-45300..-17488,z=33210..62090
off x=-82019..-61602,y=2563..23312,z=18180..41093
off x=8378..29629,y=15579..26382,z=69483..72248
off x=16302..28535,y=67418..85212,z=-30472..-19862
off x=-74874..-42672,y=35507..52617,z=-49244..-16365
off x=74689..94541,y=-6846..7658,z=-38475..-17424
on x=53913..72102,y=29412..52834,z=19941..38822
on x=-84908..-59907,y=-27067..3251,z=-39025..-19466
on x=-69095..-46356,y=-66601..-34938,z=-14725..2276
off x=-63448..-46232,y=33878..50209,z=-51904..-30419
on x=17054..27898,y=-66481..-35676,z=-76609..-55829
off x=60926..73343,y=-42913..-23960,z=7012..26246
off x=-24015..4495,y=-80370..-55754,z=-52787..-38226
off x=-73908..-68848,y=21372..47329,z=235..17213
on x=7296..32641,y=62899..83109,z=13177..38536
off x=-94051..-74068,y=8148..22442,z=13394..24688
off x=-57425..-32207,y=-58427..-51376,z=27946..49656
off x=-44008..-39198,y=58943..79932,z=-40099..-3474
on x=-16233..-756,y=30800..44345,z=-73944..-48670
off x=12905..36117,y=-67891..-64128,z=-46740..-32973
on x=27883..38622,y=32026..44785,z=-74444..-52112
on x=15410..19169,y=57309..76387,z=-49601..-32276
off x=28408..52958,y=34782..52888,z=39715..68829
on x=-6966..17792,y=57831..84759,z=16489..36509
on x=-27080..-7039,y=-59222..-54707,z=51840..63768
on x=52262..79638,y=-32198..-14135,z=-48892..-34773
on x=-9821..10032,y=-98762..-66259,z=6595..29220
off x=-51487..-19071,y=37244..68274,z=33759..52673
on x=62279..83948,y=-23483..-13180,z=-2206..16513
on x=-6908..6080,y=-58172..-42296,z=-73584..-47498
off x=17860..35846,y=-62930..-31349,z=-55124..-50926
off x=27535..54509,y=-71552..-52959,z=31499..49839
off x=50033..84920,y=13263..38473,z=-49519..-25291
on x=-21712..4307,y=-73449..-37771,z=43587..68101
off x=-71649..-42306,y=-69299..-43642,z=-14160..14968
on x=-11970..15871,y=71712..89382,z=6018..33164
on x=-34532..-23477,y=-93938..-67702,z=1501..5872
off x=40856..50257,y=-51627..-35234,z=35027..44178
on x=51262..63306,y=22093..24413,z=-54610..-25093
'''.strip().splitlines()

#0: 39:  27, 46, 38, 39
#1: 590784
#2: 474140
#3: 2758514936282235
data=data4

#data = [int(line) for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

##d=[[[False for i in range(101)] for j in range(101)] for k in range(101)]

def size(input):
	(xStart,xEnd,yStart,yEnd,zStart,zEnd,on)=input
	if xEnd<xStart or yEnd<yStart or zEnd<zStart: return 0
	answer=(xEnd-xStart+1)*(yEnd-yStart+1)*(zEnd-zStart+1)
	return answer if on else -answer

def intersection(a, b):
	if a is None:
		return b
	if b is None:
		return a
	(xStart1,xEnd1,yStart1,yEnd1,zStart1,zEnd1,on1)=a
	(xStart2,xEnd2,yStart2,yEnd2,zStart2,zEnd2,on2)=b
	#TODO:  on1 is weird here.  order matters.
	return (max(xStart1,xStart2),min(xEnd1,xEnd2),max(yStart1,yStart2),min(yEnd1,yEnd2),max(zStart1,zStart2),min(zEnd1,zEnd2), on1)

def negative(input):
	(xStart,xEnd,yStart,yEnd,zStart,zEnd,on)=input
	return (xStart,xEnd,yStart,yEnd,zStart,zEnd,not on)

def add(d, input, currentState, remaining=None):
	if len(d)==0:
		if input[6]!=currentState:
			d+=[(input, [])]
		return
	
	remaining=intersection(input, remaining)
	
	subtractNodes=[]
	for current in d:
		currentRemaining=intersection(remaining, current[0])
		if size(currentRemaining)==0:
			continue
		add(current[1], currentRemaining, not currentState, currentRemaining)
		#TODO for subtract nodes we might need to recurse too
		newSubtractNode=(negative(currentRemaining), [])
		subtractNodes+=[newSubtractNode]
	
	if currentState!=input[6]:
		newNode=(input, subtractNodes)
		d+=[newNode]


def answer(d):
	return sum(size(current[0])+answer(current[1]) for current in d)
	

d=[]
count=0
for line in data:
	on,coords=line.split(' ')
	on = True if on == 'on' else False
	x,y,z=coords.split(',')
	dummy,x=x.split('=')
	dummy,y=y.split('=')
	dummy,z=z.split('=')
	xStart,xEnd=[int(a) for a in x.split('..')]
	yStart,yEnd=[int(a) for a in y.split('..')]
	zStart,zEnd=[int(a) for a in z.split('..')]
	#TODO:  at the highest level ignore offs, or add a dummy root node?
	add(d, (xStart,xEnd,yStart,yEnd,zStart,zEnd,on), False)
	total=answer(d)
	print(len(d), line, total)

				
	#for x in range(xStart, xEnd+1):
	#	for y in range(yStart, yEnd+1):
	#		for z in range(zStart, zEnd+1):
	#			d[z+50][y+50][x+50]=on





