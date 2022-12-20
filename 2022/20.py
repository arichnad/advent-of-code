#!/usr/bin/python3

import math, re, sys, itertools, functools, copy
from sortedcontainers import SortedList #python3 -mpip install install sortedcontainers #SortedList('bat') + 'cat'
from astar.search import AStar #python3 -mpip install python-astar #print(AStar([[0]]).search((0,0), (0,0)))
from collections import defaultdict, deque, Counter

data1='''
1
2
-3
3
-2
0
4
'''.strip().splitlines()
data2='''
9038
7675
-2761
-5405
7871
9909
-2608
-7534
6480
2961
7036
-231
8168
8311
-231
-7918
-7099
4294
-1739
5725
1252
-9869
-8387
1083
-9944
-7411
-2344
1874
1179
-2107
3938
1433
1500
-7134
-739
-3543
-587
2413
-613
3407
5369
-907
2060
-8616
-7009
413
-3223
8695
8923
4909
8732
8298
2306
-6986
558
4723
1199
-4441
-3777
6190
2179
-4790
-6632
-4097
2126
-6569
9360
7066
-3011
5107
-4441
1353
5369
732
4478
822
5640
-6903
9984
-7846
-8515
5426
5380
-1083
-5498
2027
-4036
1933
-9083
-6522
3981
1528
1353
-7795
-1310
-2890
-821
-3249
1604
-7785
4864
-6274
-5087
5425
-22
3086
6103
-1216
1176
8260
5389
6865
-3520
7655
-6844
6825
7500
4738
-6575
-9354
-8543
8159
4385
4712
5582
-5921
2998
-7734
-5237
4524
6572
-919
3876
7742
6590
-1526
-9100
-8373
7952
9058
6316
-7539
-280
5690
-8328
-4869
9227
4072
-2835
1195
-4958
7685
4327
-5703
-1972
1361
-3380
1193
8975
43
203
-3897
8452
-9387
-4461
-3753
-7224
6621
-4199
-1719
-231
-7542
1440
-2286
-5739
-5238
-5396
1803
-2433
-8295
-5034
243
9301
2898
-7467
6900
2603
-1846
2649
4535
-134
8294
6417
-6390
6338
3080
8181
-6373
-4641
6499
-4658
-3790
4664
-8103
-7813
7925
4712
-4881
-7862
4722
6398
3127
9904
-4368
9680
8097
-6016
-4343
-3232
-8007
-7260
2946
-2295
9569
-9512
1188
-6007
-5746
-5659
-9550
5001
-8800
-4727
4731
-2889
9851
8625
-8211
3884
5218
-4444
8038
5600
-8563
-8559
-8648
9264
-9777
7048
-5153
4331
-5012
9264
8980
-3580
-3764
-7871
-210
4983
9218
1785
7817
8329
-9806
-503
5831
-1577
7145
-4185
8099
-1409
-3827
-1179
-1839
-4642
6705
5465
-3348
-8275
-3857
-3389
-3562
-6806
-2545
3333
-4815
-4745
7157
-2783
1039
6648
8397
518
-7325
7611
-3372
1182
-5605
-8894
6968
-8781
7045
-7504
-1993
-1019
-9723
-4018
2742
8584
-6303
516
9807
-8906
8982
-2421
-7231
-7254
-110
7723
-3099
-3946
-9669
4715
9283
-162
-6734
1857
7870
-9645
-1791
-3594
5464
-1760
-9795
7299
4427
7051
-5751
-514
3430
-6159
6061
8761
-8098
-8497
-3539
-9312
-449
-8256
-919
-2957
8584
-7785
6170
-216
-2598
-3432
498
-9040
6568
-2154
4254
-4006
8920
-5672
818
-9151
-9758
5184
-9407
8558
-1512
9767
-7108
5072
-310
-4097
6656
2520
8939
3068
4477
-2890
833
-4868
6274
5613
7527
6502
3196
-4278
-2394
7652
-3892
6479
-1218
9759
4863
6444
9229
3853
-1812
3052
-5848
-142
-9832
-3608
9604
-22
-6968
4563
5062
-1015
-4809
532
3514
-4047
3258
-241
315
7169
4427
-4895
-4057
-4867
-3296
-3678
-8223
-2099
-5339
-3784
261
-8220
-8629
7723
-3214
398
-2134
2577
-5395
-1010
-590
9894
302
-291
-4839
557
-4
-6814
-7066
8420
-3389
4447
7432
-3110
-5103
-7346
1158
-522
-2393
6833
-9793
-4097
8677
7843
1162
6083
5959
8948
-9258
339
548
-7908
-3389
3312
-6665
6145
4233
-9928
-6654
68
-6658
-1954
-9553
-3850
8605
-4962
-3731
-6643
4712
2760
-4255
-590
6690
-1156
-9081
-9856
9175
-916
-6986
9586
4150
-7064
5425
-4971
-4463
-4242
-1083
-7502
-1547
-7104
4876
3557
8075
-573
1582
374
-300
-2674
1676
-9850
-2781
8821
5571
-4962
-5602
-5744
-7374
-609
3756
-6247
-5223
-1904
-2870
-7067
-4656
5315
3213
-7414
-1218
-6989
1485
9009
8519
-1074
-2754
8239
-1954
-6290
445
6916
-5352
-6295
-5849
8287
-9793
-264
-3306
5318
5092
-9944
1875
4516
-357
4279
6823
1236
-919
-9723
-283
5333
4894
-7841
-9397
5059
-6411
-4727
6473
-5588
-3458
5038
-4811
-7022
-4463
-208
-4050
-1214
2177
-4235
-9271
-5718
-5905
-4908
-2711
3798
8139
1962
2777
1349
-4709
4358
-8225
-7301
-6543
4225
7055
7968
-34
4067
3588
-9382
4455
-3979
5975
9440
-6159
-8602
7181
4155
7008
5682
-6339
-3560
5657
1267
-6966
7195
8875
-5850
532
-4068
-8218
-9806
-5729
4833
-9089
3759
-6323
6758
-1464
3630
-5687
-6761
-2288
-1070
-2488
4606
-4857
7011
6882
7072
-2291
4076
-9844
-5053
-5288
-2819
-4962
9597
6488
-2216
-8454
2108
4363
5460
-161
3051
-3874
-4216
2384
-2699
9216
-6565
-2344
5562
-575
5114
-6744
9611
-4327
6128
-4595
3183
7766
2110
-6029
-7788
6256
-4721
-7453
1243
3591
-8088
9175
5803
8627
-7414
-6662
9181
-9829
105
6251
-4374
-2574
-6190
-6429
-6069
-765
7666
4986
-7815
-9862
-1494
1126
-4831
7677
-937
3461
-329
125
-4078
-8525
9340
-4887
-446
8322
4909
3017
6605
688
-9600
4434
4434
-9665
-1582
5869
8416
118
-9818
-6270
-8789
-6234
-2667
-5624
-843
-6098
7809
1097
1636
-4768
8574
-5701
-5939
7232
9627
2246
-9861
-8347
7128
-6706
-8264
7606
3876
7752
8607
-7305
5657
-5445
3201
-1790
2957
-7315
893
9063
-7992
-7587
-9876
9715
-7706
6723
2021
-3597
-5299
3069
-3891
-5954
-4167
-5174
-1969
-8442
-4032
4704
-7275
-5797
3864
-8994
-9335
5236
1951
-8209
-1415
7854
-6219
6395
-7607
9531
-3153
1377
-2586
6869
-1719
4504
6098
5333
-8268
9673
-7642
-6927
2090
456
5501
3313
-2756
6807
9924
-6366
7215
-7548
-8775
-6189
-5574
756
5992
-3438
3303
-2401
-5955
-422
929
-3895
-8858
-8617
2440
6476
-6699
-305
-3581
7001
-1385
7023
52
6170
-4416
-4368
9756
-4100
-2128
1336
2700
-2956
7145
-3483
-4814
5850
-6986
3226
-2394
7649
1372
1440
5926
8480
-8833
588
-6098
-3744
2512
-5459
9438
2568
-7635
-5832
-4956
-7254
-1887
-1002
8018
-2839
1931
2805
11
-6543
1352
2397
-6896
-4404
-4611
-2934
728
732
-5860
-9295
-6393
-8178
4268
5467
6917
2436
94
-3872
8740
458
-8374
9597
-2974
4187
6829
8156
1500
1325
-4150
4322
-5003
-331
-7634
-4980
5199
6177
6495
-2124
-7693
2830
-2524
7873
-1252
-3146
3499
9220
-1268
-5255
7185
4007
8905
-5030
9181
281
4563
1447
4022
1109
-9407
5401
1489
7918
1381
8570
-3332
-6028
-9003
7353
-6219
1905
-6234
-7496
7882
2993
4576
-4763
-9389
-8817
3643
7014
8282
-9552
-7661
9563
-5426
657
-3720
8541
-9561
-5222
88
30
382
-9458
8773
5816
-958
1718
-1
9851
-1437
-8874
3131
8659
8469
-9746
-463
5351
2196
4666
1351
5121
9537
-3278
270
-6881
-417
-4790
8198
4659
-7564
-1406
-8017
1418
-7394
7526
46
4376
6913
8439
1287
-1703
-8019
-1848
3178
-1835
9406
4822
2682
-5699
-8369
9218
-8020
-9109
-3200
4328
4100
9762
6714
8064
-3389
-1754
-8594
7899
-305
-5590
6447
4037
-7711
5307
8316
8042
-1825
6759
5885
-1735
-6328
-7057
7084
6397
7648
1672
1377
-4806
7889
-9765
5894
991
-9162
-9618
-5448
-6636
9263
-5689
-1984
-5736
-1879
-8834
-9083
4817
-8560
5635
2190
-1569
3190
-1070
6142
9297
-1680
-5313
-6883
224
-2902
-4275
-2243
5774
9820
9009
4502
1372
-9462
-8957
-4474
2454
6886
4591
-5829
8010
1171
8187
-8096
-7156
-1494
6078
-5321
-6959
6866
-2598
-3765
-2526
-7278
2991
-8807
5744
7490
4418
5494
6366
3223
-3996
6065
6083
-9757
-7795
-8860
-3590
1208
3797
9262
-1705
-1023
6829
-1719
8761
4015
-9660
5564
1323
-4007
4296
8471
1640
8857
2828
-7115
1801
-2177
913
-3227
-2167
-8681
-6531
-8639
-5034
-8595
-5591
-3640
-9872
5487
6480
-4470
-6821
4385
9654
-5418
2940
3007
-2800
-461
9769
-3557
-96
1933
-5065
-6178
-3162
1252
8921
-7346
637
8063
-7104
3313
-5226
-7253
355
4133
-765
-4150
7724
-9781
2534
8933
-5766
7355
7359
-8351
-5564
-8944
-924
-9922
3897
1886
-1630
4076
-3583
6583
4399
-3740
3238
-2214
5766
4757
-3873
446
-88
319
5758
-3715
5659
9665
-3634
-9931
-7137
8150
-6096
-5354
5264
2894
2141
4322
-8363
-3552
-9102
-8405
1985
-1724
-722
827
-7542
-3087
-1438
2230
-6732
8314
7862
3204
-6210
-5321
9213
-6308
6067
-3672
-6813
-5564
-3294
7269
-5603
-8833
7420
1325
-613
4196
6374
-3848
-4349
2563
5458
3293
-608
1292
-6961
-2927
1083
3482
-2694
165
5690
6652
-6532
-2079
7873
98
5072
-3443
919
-9681
-5477
-614
1179
-2303
-4740
-4169
-5000
144
-7938
5605
-2437
-2796
7672
-5441
-3718
-5036
2742
-9526
-9353
-4822
2975
3325
-7013
-894
6389
7915
-8858
724
497
-2821
9525
2632
-6295
7315
-4996
-6800
9171
7966
-9441
4462
-9757
-1522
7871
8879
3021
1190
2266
-9806
-1809
5396
-8588
-6777
1340
-6402
1347
2048
-1695
4831
-2745
-6047
-588
-2209
497
-3859
-1005
1336
557
-1643
5236
-47
-3441
-7315
642
-2956
-4392
-7778
5264
7310
3716
-7305
4565
8584
-8332
-2475
-7006
1788
8019
2848
-4043
4418
6093
8493
-1050
-2766
4900
270
716
2632
-4101
5425
-7913
-8688
195
-151
-87
-5405
-2637
-3211
-5659
847
789
-9003
-4975
251
5701
-3521
-7385
4927
5197
-9462
2603
4079
568
-1241
148
4169
-6575
-468
5697
-1602
-7019
4475
9652
-8218
-1301
-6608
-8116
-8032
7652
7917
4179
3387
-8892
3804
-3640
-565
-7020
-1915
-5849
1030
-1854
9262
-4426
8075
-2931
-4735
-4967
4516
-3703
-4037
-3830
5120
-7493
-3685
3990
-7728
7652
-958
4264
7649
8730
4906
-943
-1703
-4518
-213
3762
3751
7925
5271
6755
3827
8646
7616
-241
7705
5644
-1997
-1698
-8342
7359
6681
-424
6428
4070
-4152
-1544
9540
-457
-9883
-4506
-3850
1326
7539
-2719
-7629
446
-3895
3525
-5565
3153
-9765
-4774
7207
1004
-3939
1044
4216
-2091
-316
5708
924
-844
-9431
-1316
2563
268
-2196
2842
7495
680
-9158
4044
7591
2724
-9678
8478
7888
-9931
6742
-2594
-2584
-3731
4891
5578
-1743
1794
7269
-3956
356
-3543
1702
-8795
-4240
9678
-2034
7637
-2330
7297
-7251
9554
-2608
-6407
6621
614
-4932
3680
-8232
3744
-7013
2611
271
-8405
1894
-2900
5564
-8012
1868
-398
-2974
2262
5021
6476
-2694
-9387
-8860
-9147
1372
6647
3438
37
-46
628
-6190
949
9190
-1675
6989
9846
6705
-8247
568
-6769
-7168
7210
7732
4072
6233
3513
-6774
4114
4681
-6248
-5598
3864
-3720
5131
-5617
-6047
-5162
-972
-1495
7643
-2339
-155
6886
9254
6263
9437
4076
-7448
-774
-5093
666
7487
1985
3309
-7231
-9550
8240
-9863
-2913
-4334
-9141
-919
3370
9160
-6565
-6998
-4304
8271
8745
353
-8019
-3180
-5598
-3422
-5277
3967
753
-5396
-9445
6908
8230
-5911
-6019
3844
8586
-4641
-1219
-7596
4046
4484
1763
3844
-3076
9376
9712
6545
8687
499
1679
6876
4819
9112
-7275
-8469
-2412
2177
5869
6531
6866
9447
9909
8470
8950
5299
4152
7205
5214
9809
6065
-1602
1162
-8089
7526
6316
-4839
-2728
-8199
-2956
-1770
-3175
2434
-4434
3252
-2735
-2473
-1415
-9850
-5695
-9367
-8858
-4176
299
9485
-3461
9876
3428
-1072
5758
7975
5216
1665
-702
24
4244
-333
4927
-1218
-9921
-1713
-213
8207
4595
3019
-8639
9075
-1817
3699
-9959
-5238
-844
6888
-252
-4649
2081
2733
6417
1704
-5105
7952
-4178
6255
7259
5404
-8237
9604
5707
746
-2173
-5014
7066
-6534
5869
2336
8271
-163
7929
8420
7157
-1966
6367
-3429
8819
-2311
3465
-3441
-5766
-3581
5114
3744
3418
-9690
261
-3944
3883
-5729
6583
1938
5776
-8645
3204
4651
-2649
-5505
5548
9354
5922
5303
-953
-1271
-3419
-2486
4555
1393
-5358
9532
-5494
-6930
9964
7882
-9530
-3895
5622
-3628
2197
2276
-9181
-2435
3309
-6663
-4162
6531
-8469
9269
-4133
-6966
-5863
-6195
-5429
8867
6342
-8027
-6325
4311
-2326
3716
-1739
-3476
2324
7934
3014
-8606
1848
-3444
-5282
-4461
-1050
0
827
6083
8029
1340
-3376
3259
5635
-1710
-6600
7067
-8296
9458
5041
-1625
-7288
5343
-9719
5307
-9983
7181
-9167
2783
-1019
-1993
7655
-6549
4731
-4192
382
-7562
-138
7065
520
-2754
-7086
1193
7378
5949
5516
7668
3967
4968
-9093
-4765
6648
-7254
-2728
-3521
-3387
1400
4174
-573
4418
5428
5268
1953
3961
1352
-8565
-473
339
-7743
7487
-3301
908
-4044
3066
639
5734
-2154
6476
-1674
3005
-758
-3857
-398
4824
2898
-9364
7543
3953
8565
9074
-3935
-840
-4746
-5412
224
1980
-4382
-985
-8616
-9353
-3728
-5724
6327
-8100
-1036
5126
436
1928
5816
1068
-7790
-723
-2488
-8857
-6498
6036
-3161
6805
1739
-7898
-5766
-522
-9463
7934
5040
2629
-7718
-7554
-1503
5369
-6776
7723
6564
-2426
9005
-7560
-5345
7157
-9826
8397
7528
3303
8801
1908
-6390
8631
305
7687
8228
1236
-2457
-6737
-3918
2754
6279
7978
-9903
-7236
631
1867
-3358
-7237
603
1997
6092
-7718
2533
-4151
4100
-3185
-4901
7649
-2298
-2432
8707
-9830
-9767
-3211
9933
2283
-9099
6706
-6406
-4649
4770
2118
3144
8427
8156
-3570
-1691
515
-9339
2196
8206
-6405
4273
-9903
-4022
-681
-7319
1399
-3500
5424
1619
-7567
4294
-2703
-8387
5271
-6257
5333
-1079
1627
3196
322
-7137
-596
4388
2374
8018
4938
-2226
-3779
988
6087
4097
-4214
-2304
4035
4536
-8304
283
9545
9074
5176
-3644
-4019
-2793
7441
6443
-9981
5315
8099
1026
4952
-121
-6558
-2469
-1706
-1188
-969
-1044
5320
-6924
-2490
-8370
-7465
-6080
-8586
9117
-2655
7903
-5612
2344
7583
5578
7752
1764
1185
-1002
-5440
-2965
-9657
7853
4986
5833
-6432
7589
-9058
-1019
4044
-127
-6243
-8781
-303
2358
-6159
-1858
-5982
-5453
1892
5776
-8384
4536
3749
-239
-3422
-3360
4988
8225
-2052
6294
2092
9181
324
9932
8633
-7411
-6448
3938
-9550
9659
4993
88
4590
-8220
-5526
-2081
5819
-8137
-5547
-1865
-9808
-6939
-1544
3896
9540
9416
2950
-4656
-5494
1637
7953
-514
-6234
561
-6998
-2741
7084
8222
8586
-6173
3182
-6381
-5832
-5665
6810
-3406
-9084
-665
9767
-3897
5803
-9418
9063
6435
-2226
-1120
-4392
-8203
-8304
885
991
-1673
6575
8565
3853
-2644
220
3722
-9278
-1809
9328
9227
-3244
847
8190
9930
-7564
936
-8019
7449
-9083
-2843
5071
9634
7746
8306
-5853
-7784
-7352
-1319
-9723
6917
-5325
5033
4017
-5695
5790
-1972
3130
-5078
-3521
9464
1636
-5447
6679
-7608
5330
-3604
-8552
8840
5337
3430
1370
-101
7616
-9372
52
-5695
-7007
1500
2085
6524
-1425
-3508
-5089
6092
5099
7084
7175
-9676
3772
6569
6322
9190
3232
7346
3140
-9551
910
-6290
-4857
-450
-7598
7342
6621
8571
370
2513
-7918
-4513
-8099
6917
-9530
-1965
225
898
9754
1701
896
4209
5072
-9903
-4710
9724
-9374
-1618
-8093
470
7295
725
5036
9672
4288
-9511
5232
4433
189
8287
-9681
-5416
2486
-1684
-106
9707
9788
4600
-8008
5635
8753
9483
5259
-6546
9692
648
-3109
7558
-7645
8580
-7657
4496
-745
-5490
-6968
-2313
972
-3491
8512
-2819
-6712
3418
4117
-9511
-9985
8563
-394
5062
-4939
7513
-1607
-7285
-7783
4418
-3465
5318
-8325
5748
4894
-6369
9123
-4089
7885
6712
8839
1422
-9244
-6528
4833
-7070
3853
-8199
2046
-7303
-9471
-7321
2876
-4618
1227
5908
-660
-7108
3375
-9642
-1924
-5222
-2429
4474
-3914
-6599
-1044
4563
-6248
7256
2499
-5294
3742
-4775
-41
-3895
-161
8863
8355
-3683
-6075
-7547
-3472
9540
-6258
9204
5320
1200
9547
7236
2317
-1441
9692
8019
-9920
-1098
-8129
-3734
2671
-5495
-6269
-5347
8707
-8175
9855
-838
-7952
-5534
4299
8691
9830
4640
-8587
8383
-3836
8407
-6858
7919
-1259
-6720
676
-1975
6862
8770
5368
-2209
7655
-5968
4952
3716
4490
7014
5381
6480
6846
-894
5933
-4932
809
-6631
3182
558
-2719
-4501
3574
5916
7666
1658
3884
-1636
6003
-6176
-6791
-7480
7543
3806
-8849
3545
107
5526
7842
-1889
5401
-8017
4136
7560
-154
2060
-5637
5410
1367
-1982
6146
738
-2052
-3252
5953
-8685
9532
7527
-7728
6725
-9387
-8199
-8554
7287
8045
-6992
-7254
3068
8321
-4326
-5803
-2994
8935
-9867
2774
9518
-8107
-8014
4302
8581
-8499
2197
1874
7250
-3636
-3658
-6494
-8658
-5858
7616
-6565
6807
-9681
-1719
-7575
712
7592
2295
9301
7649
640
5406
-3447
-9757
-9307
-2196
-3659
7237
7214
3643
7838
-7526
-5685
-8310
-9564
8383
-5337
-8770
22
398
-6159
2625
5108
6004
-4591
929
8809
-9528
-3971
-3805
595
2472
49
-9757
-6272
8618
5088
2874
6617
8978
-7120
-108
1051
5213
2196
-1658
6984
169
4289
-8185
-2807
-5665
1186
929
-7574
2566
-9573
3484
-1293
2485
6931
9208
-5591
386
2206
1323
-2129
3325
7695
-2599
2949
-1817
926
-2728
-5590
8732
-5709
-5637
-4765
-7066
-155
-4947
-44
3756
4940
9520
-3310
-6471
5202
-1639
1643
1353
-9555
-3402
1737
8121
3765
4201
7934
3222
4444
5229
-8675
3426
632
5002
-5106
2442
-3080
1610
4113
7009
2603
-282
-8107
-8020
-9407
-5238
7566
5933
-8503
7628
638
-5627
2568
-2857
2161
2989
979
4076
6644
-3350
3092
1837
1203
2576
45
2443
9340
-2807
-451
4384
6003
-4883
7296
4009
2948
7275
-4649
4406
6347
-969
-908
2419
-6657
-7540
5072
5587
2971
9815
-4273
3077
-5448
-9666
-1431
-7312
-2457
-9131
7607
477
86
-8026
8541
-2111
6697
6357
5114
-1783
6939
9418
4795
5361
-3438
-4073
5621
640
3236
-6643
-6598
438
-513
-6946
-6257
-7089
-6657
2576
-3562
7096
-5044
5146
8168
8287
1764
-6510
6711
-8347
-8364
-7070
-2445
856
-3649
387
-7016
-5664
-7301
9676
8691
-2116
-9879
2419
-237
-6412
-4765
3510
-2083
-6111
-8030
5557
2721
-6220
-601
4148
-2272
-511
-9580
8559
9546
-6145
6454
-5547
-4680
7443
-6045
70
-5926
-7459
3288
7643
-8495
8225
-3302
952
8329
1489
3898
-8088
-748
-4117
6946
1360
7335
2410
1455
8029
-1085
2179
-317
3045
8121
7310
3483
5789
-5590
7901
4418
4952
7485
676
9713
2354
9773
7078
-8362
8954
3672
8565
5001
-150
2040
-1474
-821
-9806
-7096
144
7209
6569
9813
3222
1340
8726
9811
-5999
-7060
-3153
-7728
4626
1181
4289
8853
9038
9671
-1889
-6814
-8389
6065
-7279
5850
-6256
7558
-7357
-4503
-8258
5802
3716
-4658
-702
9218
-9478
-8857
9839
-2469
-2298
-3347
-373
8820
2451
-8518
-1321
-1220
8584
6414
9376
-802
-2028
-1188
-8020
-2124
9087
-974
2948
-8536
7609
-7583
-5739
4286
-700
-5725
5662
-310
-5671
7834
7968
5426
7047
7772
-3083
-4343
330
-8277
7611
-6051
-9676
-9952
-5345
9485
5959
3272
6659
-5319
4927
-109
3525
5803
-6303
870
3902
2028
-220
-6704
9493
-6973
-8594
-2655
-8786
9198
-1389
-1682
-5146
4037
-186
-1941
-2009
-4528
-3468
-3915
-2146
372
6065
-3716
3080
2893
-2320
718
4148
5831
-7567
-1448
-1602
-934
-801
-1705
-5251
-6643
-8553
-6987
-2254
-8669
1611
4366
3659
-6163
8206
5399
8222
-1526
-2610
-9441
8075
2115
-8882
-231
-5178
-2650
6725
2163
139
-7348
1933
5621
-9828
3483
-5162
-8860
-564
-4733
8411
-8213
2935
261
8373
1077
-1854
6692
5528
-3861
1706
1979
-3644
-5902
4209
4418
-142
2577
-4603
3052
-8050
8732
-539
-2274
8857
-3136
630
-6390
3281
-5535
-8820
4498
4167
8465
8588
8156
-5695
7153
8839
-6546
-6791
4148
5466
5854
2735
8559
2820
4171
-3216
418
-1155
7666
-8617
-1770
4958
3113
9540
-5153
4704
8329
9651
-7158
-5836
-3824
-501
5326
-1505
5522
-5813
224
-4900
-5761
-8349
-9244
-2667
-4813
949
-1039
-896
-8479
8346
-9162
1388
2496
-8830
-4251
4929
-9223
-6208
9651
-6707
1370
6505
-8175
9761
9092
-7007
4433
4404
3219
-2154
-7705
6812
-7048
-2843
4018
-9700
-9618
2649
-1252
-3956
201
-2728
-3542
-485
1433
2865
70
-9660
-333
3996
9840
4619
-4104
-7113
-5008
4018
-957
-2727
-3372
-4101
9991
3718
8691
9811
-3581
-2209
5808
-8674
1890
7177
7225
-58
2719
-4004
-4956
-3609
2525
8469
-6882
-8503
-5943
2243
1400
-9738
-9688
-2155
-6292
105
-5096
5850
7881
-6715
9915
8466
-4470
4322
-2281
7452
-2439
5197
9804
9056
-8798
-1835
3836
-1882
-5922
4440
4796
2401
3088
8150
-8351
-9700
7167
4681
2848
-4374
-686
-670
-2273
-6369
5010
-4367
-1064
1325
-8824
-840
-5971
3311
5059
-8503
94
-191
1533
9213
-8747
9782
1146
2287
2626
-3544
-7558
-8860
7308
-1603
771
-1335
-1117
7505
7275
-6494
-1631
7235
2749
-7120
-3143
7975
5685
7442
-3299
-700
1691
-2311
118
-9814
7329
-8408
-4444
3132
-6502
-6032
-186
-3657
3031
8093
1815
5566
4373
8519
898
-4586
-5531
-2364
9493
-9552
455
1955
-3868
5079
-2254
-3162
3853
-540
3264
-4733
7338
-5645
-193
4669
6853
-5863
597
-4487
9404
6764
-2077
3243
-5186
7793
-1685
908
-3946
692
1497
-6219
-6987
-8629
4329
8842
-3372
1328
-1139
747
7487
-4242
1121
8748
-7690
-1618
5420
6169
2499
-7134
-6083
-2364
-4765
7069
4255
-7108
2291
2011
-3272
-707
-6791
-7790
-9536
4322
-3468
-9757
-4768
-4007
5685
-5475
-9615
-6359
5099
-8541
2231
-3800
1115
-1245
-7405
3772
-2391
1134
6677
-4733
2039
6374
-7052
-6959
-271
-4252
-8019
-291
-6091
170
-1227
-8333
8190
52
4563
-4416
738
-5468
-9364
-9808
-6367
3220
2898
-9132
3657
2454
5975
-1675
-280
1197
-3325
123
6793
224
6647
7100
8712
3342
6710
-4779
6206
-3440
-1719
7903
-4293
-1183
-707
737
-9188
4958
8699
1097
-4656
-4586
6331
929
-2435
-9977
9433
-5609
-1485
799
7371
1243
754
7169
-8196
7388
-4228
6185
5248
-8359
6702
-9546
-5989
5318
4458
6190
-333
6491
5025
-7892
5676
7798
-4568
7845
-5359
570
4206
-689
7632
-9962
5696
-2084
773
-8791
5177
-9122
6150
-7172
3383
-3892
5327
-8395
-6411
-5746
2046
-9121
356
4958
6331
-2917
-9345
5034
-7976
391
-6359
1709
-1373
5707
-2263
-6580
5684
5099
1481
9512
-8861
3403
8724
-9180
-258
-5412
-5443
-7007
2304
-6851
-6212
9593
-614
9198
6488
-6402
-4028
-4939
1592
-8089
5259
-6209
6647
32
1224
-1190
-7785
709
5296
-2280
7388
9474
-3874
5240
-7536
6420
7597
-6715
4619
4958
-1448
5405
1647
2519
-5223
-4203
9830
-2415
9391
-7271
7085
-3737
7728
-6568
142
4218
2955
-4345
-5066
-8052
-6237
5213
-1252
4159
5156
-8786
8368
4940
-6694
2585
7160
-900
8692
-6776
8990
-9865
-7083
8892
-6543
-1809
5998
-2619
1296
-1779
9117
-4445
-1426
6331
-4049
5381
2214
-9463
-3807
-9767
-6303
195
-3935
9915
-5616
-4694
-1230
-6819
1375
-3874
5123
-6016
7978
-2647
-8008
2314
8757
2734
-2179
8450
-3379
-6973
2197
1670
-838
-294
2943
3716
-8800
-2294
6150
-4304
7116
-9471
-3615
6055
6124
5701
1691
135
-5976
892
751
-6761
-6358
-2155
-3903
8399
-2965
6304
9583
-4265
6516
-8995
-9563
8419
-231
3987
4906
-6272
-1743
-4262
4531
2984
3518
3440
-4182
-974
-8467
-6047
226
3053
3961
-2177
8673
6661
5441
-10000
-803
-2312
-5375
-7357
-4620
208
-5287
4123
-1889
-3966
-9022
3281
5750
8514
-6365
3756
3545
-3257
8326
-7385
-1448
927
-3543
483
1403
-6813
4675
-9286
-702
-351
6338
2087
9015
-3704
-1824
8860
603
4039
-7156
6551
-3996
-9777
-7364
-1044
1744
-5545
9213
-7224
-1634
-7032
4037
-4736
6482
9074
-7008
8872
-142
-7315
-4423
-7938
-9538
-2264
-9854
-7657
-8107
3279
9983
8876
1763
8551
4669
4178
7732
4757
559
-5508
1917
-9645
8190
5953
8709
19
2819
4063
-5477
-7912
4119
-2225
8226
-5209
-5050
-4380
107
-8503
-8747
-4133
3836
-9431
-2970
3836
-9089
-6585
9422
-1526
5254
-2190
-9460
5904
4409
-2648
9833
4241
6371
1692
-8305
-9988
-1766
3813
4389
2039
7008
-1972
-5494
-2116
-9962
597
29
-1470
-2890
-5092
-435
-6016
-9834
-9481
-8586
5132
-7783
1133
-8860
-5405
-4062
5121
-7060
-7647
4311
-1739
6368
4940
8967
4872
-9120
1693
-2532
5466
2160
-1171
-5664
-1209
929
5804
2011
-9777
-5591
-7661
-3722
1883
1771
1049
-9916
9707
1238
-2196
9163
4744
6209
7443
2479
-8062
-853
1877
-2812
3041
-4345
3879
2218
1250
1068
-5093
-5646
3664
-5726
-7435
-6144
9192
2384
6322
4254
-6665
-6083
4521
7204
-3650
3404
-6882
3008
929
6181
1000
8726
-2711
1195
-8675
4399
-444
-3790
751
3180
-3869
1190
-9793
-4586
-6950
-3768
-5197
-5180
-2277
9194
-1007
-2066
-156
5416
-7426
-2526
-1636
-5534
5505
9922
8755
-7151
30
-3294
495
7924
7145
-1147
4148
-9445
-58
-1707
-978
-517
-6858
-587
-3848
-5179
6303
-3141
2413
-4474
9554
3356
9056
8081
4455
2295
-4515
-7477
-7861
9869
-5646
-1387
4536
8147
-6871
7631
2908
-1979
5150
-9765
137
5099
4159
-8528
-4958
9932
6567
2629
9258
5776
-9750
4783
6185
9593
2314
271
118
4339
-1083
5969
-5784
8075
-9513
-9036
-6051
7838
-1928
-5598
-3302
6603
5443
-3312
-8185
-9804
3598
-840
6729
-9862
-298
-2989
-9293
7555
9651
6498
-9902
-2618
-8341
1966
-8557
-1050
2051
-4
2709
-4097
-6219
3017
1760
-7027
4481
-9082
7978
5430
5894
-9353
1030
2472
-2445
8385
7496
-1691
-1334
1730
3691
9104
-3068
8450
-4216
-4044
160
3328
7683
-22
6255
-3801
-1915
-7156
-2433
-9356
-9131
-9348
492
-21
60
8412
7446
4148
-9527
-5063
-8969
-6694
2563
4629
-8099
7838
-3299
6453
-8131
6477
236
2321
907
5284
-8180
-3939
5833
1640
-7756
-3163
7978
-7901
19
7472
4117
9512
-5222
-4595
-9161
-5472
5039
-187
-3087
-7240
-3360
3383
-8098
-2718
-203
8519
-8798
-1551
-5801
2512
6371
-2870
-5105
3226
-8810
7047
5922
8180
-3181
-888
3655
-6162
7486
-6904
-1622
-3877
726
-5940
-4060
-1072
-2500
7206
-7489
-4831
6632
-8583
-110
8633
-2974
676
-3124
2606
9624
-4078
-218
4831
-2716
-711
-6625
-3934
1413
-2968
-8586
-4662
8206
-5178
8568
4675
148
-492
3463
1886
6997
-1905
3550
9009
-5227
-6781
7613
3846
-8442
-3258
1438
7566
5644
8733
2196
9218
-7965
6477
-7385
6490
4474
-318
8294
5708
2359
-2113
-1389
-2342
-6777
5199
-1984
4241
-2881
6939
4169
363
-6290
-4214
-2974
-1690
-1132
-9933
6939
-4102
-271
-3716
-4586
-1936
8580
-2154
-9830
-9464
-1992
-237
4995
-3221
-6497
3164
9070
-3472
9745
3844
3146
2499
19
3348
-2363
-9265
-4721
-4204
3080
6428
-5412
8265
3279
7817
4942
-2716
8919
-7436
-3232
-1511
-47
-9145
-9099
7082
-1529
-6231
-8008
-4005
3967
-6580
-8020
-6208
-5443
9815
-6970
-494
-6078
-485
-7313
-6723
1500
4293
444
-2521
-2699
-9147
-8173
-9714
7666
-127
370
-9846
-393
-7861
-8834
-9022
-2463
5450
-9960
-3493
-4416
1437
-3861
-6665
3438
7664
-5770
-3465
4600
-5055
4289
-1431
-4632
5736
-2124
3248
748
-6441
-4694
-2330
106
-4214
296
6759
117
7339
9739
7585
2725
-2964
1185
6487
-3302
9858
-3659
-8041
-9293
-2137
4210
737
3277
377
4714
6381
-2093
-9953
-1740
2296
4622
604
-9300
3067
-5103
-7412
8659
2948
-7412
6941
1377
1044
-3257
7335
-7231
-8669
-5773
2218
7172
2297
7072
-3081
2701
-6288
6340
-8837
8427
-9083
8088
7619
-7007
-2683
-4399
5931
-9733
4109
2856
-3979
4998
5950
5404
-8433
-291
7472
-9743
-5396
-8220
4022
3404
-6708
169
4795
2484
5787
2153
2844
-9240
929
4268
4155
-5832
2868
-6887
-6724
-6096
-6482
-5861
359
711
1497
1451
-440
-5659
-3857
-4947
9283
3698
8448
5792
9485
76
9269
7420
-2716
-6667
-7632
-4939
643
6710
7606
4537
-2794
9892
3756
9088
-1737
-1524
3279
6590
-8822
-52
521
6590
-232
-8071
1678
1030
-1958
-3953
315
-3096
3427
2842
-1220
1610
-1133
2754
1411
-4054
6373
2882
-5014
-584
6140
614
6342
4929
-109
-7221
7854
3516
5259
-8387
4133
-8903
9211
-7663
-3371
-907
-3928
5001
-5634
4143
3938
6790
4838
8166
9869
847
-9095
-8207
-6272
-6883
-8334
75
-8396
107
-7057
8532
-7108
-379
-7305
-5730
3890
-9983
3554
-4349
-2397
-7027
32
-1227
9955
3404
-5494
-864
-8226
-8019
-5379
-6539
8253
-4285
712
8563
-8469
8136
8820
-5370
9148
946
3756
1709
-8543
2495
2889
-5943
-1356
3813
2236
9673
7834
-7610
2462
-8332
5544
-7727
9909
-9810
-3708
9772
9522
-7672
-6816
-2440
1731
818
3732
3029
-2079
-8226
8181
-3458
7842
-6861
1924
3815
4418
4825
-9599
-7900
1533
-1188
-1303
-6753
-2645
-2931
-8268
-8629
233
-3891
-4815
3262
-8591
737
-4215
8580
-1577
-1385
-440
5775
7236
-3432
3981
-9083
-8178
-5911
-8088
9540
-7540
-785
4286
6094
-2870
8853
7631
6315
8631
-1332
7582
3712
3068
-6715
-7224
-2181
-6116
3938
2384
4347
4100
8025
107
985
4254
-9035
7508
-333
7918
-1537
985
-3163
-9259
-5905
-9029
-2647
-1286
5279
900
262
-122
4175
-8981
-821
4313
4046
8514
649
-8247
-3001
7566
2496
-1435
-1817
5713
-2439
201
244
-5921
-7013
7478
6647
-9029
-2817
-4101
5303
1992
-2052
-6369
2060
3974
7496
-7960
3942
-3703
2053
4441
-2900
6983
7595
-9569
1324
-609
-7303
-4101
30
619
4699
-9358
4125
-4269
-3719
68
-9398
-7760
6507
4560
-4133
-9037
7059
6196
3641
4866
6552
-1739
-9080
7652
-9665
-9050
-5508
9717
6679
-6776
-2400
748
2161
-3292
-772
7838
9838
-1036
-9516
9424
107
-110
991
6417
7685
5368
9820
2051
-1630
5210
2819
-3429
-8102
9872
5859
-1462
-2628
-1123
-1828
-6031
-1812
459
8674
4484
6718
9753
-6323
1657
-7928
-9983
5369
8399
-9013
-9802
9260
-9271
9850
6479
1296
6853
119
-6372
7449
670
6805
5345
-9944
7055
2854
-4902
4686
-5339
-9538
5587
-2759
-1618
-6992
2947
3035
1636
9103
8639
6417
-8144
-9322
7649
-9833
-6102
5111
7326
-5550
-4214
-7465
7973
-198
-7938
-6323
-4298
-7782
-8310
-985
-8016
7044
-7066
1433
2498
3756
-4258
-4836
-8293
5177
4511
7311
-398
-6800
2
-9720
8047
-8797
-1133
-9498
832
-6871
9535
8361
-2939
-3444
4080
7705
3066
8577
4531
-7896
7171
5803
-5026
4044
-7255
-8183
5966
7051
8498
9300
2499
7065
-6098
738
8156
-688
-7698
-206
4124
-889
9637
-725
7259
5303
-9325
-938
-8588
7240
7725
-305
-7938
4045
1393
9220
3627
1179
5679
-203
5403
-4658
-8273
-9188
-4152
-3947
-6308
518
4980
-7970
-7540
-7920
8498
-2096
-8944
-7632
-8744
1083
-7864
6294
401
1490
7269
-3845
619
-4947
-1680
8707
-1008
-6502
-5414
7306
6308
2472
-8980
-6070
-4240
5501
-1484
-9286
7643
1573
-5523
-8894
-3979
-3608
3151
2078
5975
6984
-7271
8469
-3824
-1132
3236
-9496
6656
4969
-8847
-2457
6827
-5271
-2025
-5278
-2192
-5561
-1039
9753
8641
4600
7051
3498
2072
1260
2578
-2728
-3127
-7293
7262
-9130
-6237
-3350
-2116
1971
-4953
-6892
765
-5122
-2116
-9445
-9461
-3310
-95
1725
-3947
2039
3972
3746
7088
-9122
8058
4482
6498
9540
8306
5099
3515
7809
-3988
5216
6366
8558
-1739
-668
239
6823
-7718
5463
-3570
459
2689
8341
-8271
-6665
8550
9932
7920
-4013
7606
6112
-7970
-1335
-394
-984
-9387
2495
-8256
4929
3458
-4765
-6830
8329
3039
3041
-9429
5432
2231
6255
2338
-8175
387
8799
-7629
-446
3068
-941
-7278
-5772
-9280
201
-4939
3617
-2298
7346
3045
'''.strip().splitlines()

data=data2

#data = [int(line) for line in data]
#data = [[int(column) for column in re.findall('-?[\d]+', line)] for line in data]
#data = [[int(column) for column in line] for line in data]
#data = [[column for column in line] for line in data]
#data = [[int(column) for column in line.split(',')] for line in data]

#data=[(i,int(d)) for i,d in enumerate(data)]
#for originalPos in range(len(data)):
#	for i, (originalPos2,d) in enumerate(data):
#		if originalPos!=originalPos2:
#			continue
#		del data[i]
#		data.insert((i+d)%len(data), (originalPos2,d))
#		break
#
#for i in range(len(data)):
#	if data[i][1]==0:
#		pos=i
#print(data[(pos+1000)%len(data)][1]+ data[(pos+2000)%len(data)][1]+ data[(pos+3000)%len(data)][1])

data=[(i,int(d)*811589153) for i,d in enumerate(data)]
print(data)
for n in range(10):
	for originalPos in range(len(data)):
		for i, (originalPos2,d) in enumerate(data):
			if originalPos!=originalPos2:
				continue
			del data[i]
			data.insert((i+d)%len(data), (originalPos2,d))
			break
print(data)

for i in range(len(data)):
	if data[i][1]==0:
		pos=i
print(data[(pos+1000)%len(data)][1]+ data[(pos+2000)%len(data)][1]+ data[(pos+3000)%len(data)][1])

