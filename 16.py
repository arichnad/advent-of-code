#!/usr/bin/python3


data='''
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
'''.strip().splitlines()
data='''
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
'''.strip().splitlines()

data='''
departure location: 31-538 or 546-960
departure station: 39-660 or 673-960
departure platform: 35-731 or 745-968
departure track: 43-179 or 185-953
departure date: 29-250 or 263-949
departure time: 43-903 or 928-954
arrival location: 46-372 or 384-968
arrival station: 36-215 or 225-950
arrival platform: 25-631 or 655-950
arrival track: 26-768 or 781-962
class: 29-462 or 478-974
duration: 34-441 or 455-963
price: 39-683 or 693-956
route: 36-342 or 348-971
row: 37-501 or 520-963
seat: 46-356 or 369-973
train: 43-414 or 423-954
type: 35-160 or 178-950
wagon: 29-878 or 889-959
zone: 31-188 or 201-971

your ticket:
137,149,139,127,83,61,89,53,73,67,131,113,109,101,71,59,103,97,107,79

nearby tickets:
390,125,294,296,621,356,716,135,845,790,433,348,710,927,863,136,834,139,115,323
819,227,432,784,840,691,760,608,352,759,85,712,578,575,901,151,440,494,283,274
455,784,136,934,493,390,140,53,397,355,802,100,420,126,902,870,588,498,60,607
84,785,235,760,316,787,318,70,809,586,228,388,458,152,408,245,983,765,485,348
71,303,390,394,68,796,372,829,153,656,769,103,827,588,873,595,619,149,235,785
494,323,586,945,847,75,839,606,586,457,355,840,114,376,753,207,205,823,273,840
499,500,425,68,402,319,931,287,822,631,386,897,311,757,570,752,651,565,135,494
239,238,456,392,227,850,352,703,786,939,334,298,336,740,833,148,353,712,319,267
855,845,557,145,78,693,559,560,203,398,563,480,180,892,349,935,816,274,370,582
274,369,868,128,878,982,84,313,682,612,120,59,64,598,426,608,391,897,789,238
440,365,720,81,497,281,717,414,531,154,595,693,849,73,488,594,215,301,131,263
943,311,275,550,680,409,168,875,406,935,531,575,141,809,622,303,143,131,814,408
521,558,250,699,125,716,781,88,386,396,783,69,738,898,585,84,233,131,228,340
554,435,108,821,939,616,622,586,371,705,706,627,159,186,839,498,829,932,367,83
393,850,936,532,673,716,597,534,874,128,380,108,333,401,818,137,426,152,83,275
121,424,681,767,498,819,811,334,941,413,295,55,205,432,334,311,764,128,714,223
483,188,293,866,245,814,894,870,272,572,687,98,758,239,310,788,78,624,841,589
846,748,338,875,699,232,562,120,868,837,149,423,311,521,638,435,940,460,786,760
659,141,95,240,538,229,328,730,563,761,559,246,206,589,238,277,553,543,409,226
459,819,942,720,875,902,417,573,796,285,948,398,401,583,701,139,528,437,185,100
746,69,65,806,868,271,559,412,243,342,564,230,813,978,285,205,694,824,108,555
329,342,768,826,125,601,622,111,768,247,622,658,60,524,59,102,161,727,84,549
358,185,693,698,800,942,717,386,486,126,790,300,623,321,792,401,140,330,483,497
607,772,754,459,99,424,491,610,332,828,614,579,868,947,228,399,799,700,71,703
89,275,51,112,131,929,812,115,160,677,872,721,577,353,612,351,479,176,876,500
438,141,810,937,598,697,324,310,406,339,839,729,787,203,802,602,657,982,825,557
571,188,613,707,249,522,730,300,695,491,808,686,556,209,93,279,107,804,118,58
77,59,449,604,656,306,91,713,852,694,122,551,837,901,99,600,758,701,538,388
799,525,133,859,231,844,232,614,286,371,847,230,309,801,774,53,351,480,895,782
763,556,266,716,108,456,67,62,93,903,327,308,947,416,329,947,890,763,152,160
616,307,849,655,876,857,492,489,873,398,853,329,460,16,698,890,858,53,751,293
508,937,332,803,790,604,845,718,570,178,710,570,79,310,716,486,51,61,850,554
525,493,610,807,695,440,566,403,699,497,215,107,641,395,208,385,551,143,399,318
729,949,68,304,399,53,832,68,892,487,532,568,342,410,896,440,53,375,488,767
50,178,179,603,786,928,863,128,60,416,315,409,277,721,931,74,326,799,679,760
825,154,847,112,854,202,658,287,128,667,93,550,730,494,329,819,683,394,557,836
597,849,749,896,703,101,159,982,947,409,712,928,618,229,146,682,555,297,407,892
700,62,789,354,585,53,877,411,414,700,486,802,863,619,700,101,388,155,154,977
834,689,441,804,109,758,480,678,935,659,626,791,573,499,273,82,843,434,804,436
556,711,629,497,684,106,341,581,493,787,844,50,660,791,548,290,674,478,589,799
487,759,287,890,330,107,250,82,129,706,448,936,552,80,751,898,630,526,399,730
104,302,612,722,523,60,891,353,597,588,839,363,355,77,855,521,264,293,429,813
153,152,729,412,945,82,341,746,150,757,278,74,722,893,546,143,180,627,237,391
123,564,719,682,602,597,598,898,70,389,203,785,578,649,138,88,524,89,819,53
946,701,213,127,708,86,67,497,55,772,210,764,583,719,77,87,559,290,584,97
479,631,283,91,706,800,547,408,943,697,658,283,330,170,524,67,403,591,800,604
562,532,909,877,92,534,706,725,414,278,583,721,760,225,231,761,133,561,795,713
330,873,285,701,616,496,768,207,290,719,150,835,937,248,252,897,683,229,573,576
399,416,673,747,326,440,696,179,892,321,575,554,243,626,522,281,852,127,806,339
490,531,673,460,874,715,682,117,604,390,557,717,155,555,249,408,82,618,978,607
802,709,270,823,565,452,831,563,702,527,847,116,144,334,92,707,299,410,371,428
118,439,478,681,279,489,145,98,404,437,274,579,539,303,818,413,675,76,571,939
356,251,332,824,136,146,439,232,315,932,398,848,623,947,934,483,621,756,102,618
875,604,80,606,839,104,726,114,683,231,154,940,83,940,898,787,285,691,548,96
867,319,946,877,314,897,377,757,462,725,97,570,459,128,339,303,817,525,349,900
727,710,147,428,770,287,283,328,60,930,596,301,179,527,494,496,107,839,763,864
667,52,178,306,932,729,439,572,868,86,784,113,701,56,110,560,271,235,351,406
839,657,898,705,630,317,394,805,128,799,277,853,821,495,759,97,221,557,819,94
554,281,701,726,610,250,58,241,83,594,240,933,845,370,536,618,426,562,431,998
402,768,462,120,829,751,138,383,95,280,559,520,702,106,235,579,697,581,697,154
794,630,586,683,313,854,796,62,304,84,486,141,325,575,767,51,585,300,754,771
821,533,292,872,623,717,85,270,776,238,551,392,626,538,796,931,325,553,188,947
298,790,296,323,855,721,460,439,704,892,576,295,93,306,713,850,310,438,778,122
720,544,287,423,71,705,241,803,265,680,108,66,588,498,831,370,605,707,206,101
206,574,747,846,241,596,206,619,301,99,54,700,561,701,934,760,203,353,753,688
558,136,727,810,116,557,478,549,787,191,761,408,721,813,435,763,836,296,334,316
220,626,768,901,813,695,334,244,206,615,70,143,114,752,76,91,146,388,122,356
369,699,225,498,591,105,659,61,424,141,718,60,777,496,495,673,705,837,623,573
928,811,759,319,405,698,82,315,412,583,289,720,383,353,601,341,325,70,248,154
552,695,108,556,329,304,185,134,681,370,891,697,270,303,445,831,339,433,424,746
202,306,246,767,76,128,123,403,355,794,856,774,875,139,627,615,714,901,293,431
822,750,877,112,861,204,99,571,827,623,522,94,874,541,699,89,587,350,847,440
764,85,337,895,337,711,81,811,155,277,303,523,278,301,813,614,542,115,750,124
822,824,588,587,931,524,274,129,864,93,755,95,527,790,854,659,124,420,91,563
693,631,798,150,694,852,793,597,824,593,621,300,400,77,122,71,723,634,576,874
96,644,524,315,387,705,188,328,942,558,87,699,75,154,69,495,532,356,817,484
571,682,137,782,157,156,305,395,484,855,711,487,96,844,289,499,496,852,340,997
369,211,462,595,817,247,770,600,561,547,226,235,946,348,105,440,245,432,315,51
77,878,560,244,392,282,878,759,227,498,827,759,53,570,204,616,557,913,147,728
398,547,673,309,459,52,808,269,64,832,284,615,787,860,599,99,22,114,455,500
976,238,749,316,797,703,571,77,70,484,896,828,896,674,713,656,597,355,143,612
238,435,526,656,82,295,488,123,135,390,138,393,72,135,983,624,531,719,592,494
707,757,396,822,574,115,323,676,299,757,605,21,300,892,626,656,840,283,478,130
338,62,366,118,333,622,594,355,931,390,549,835,144,98,837,591,294,85,298,605
107,72,210,400,828,658,850,987,478,335,432,931,601,411,567,827,829,493,722,390
711,337,154,356,799,393,628,21,494,126,328,763,80,130,107,423,286,929,854,213
938,657,385,246,839,401,120,625,64,288,440,196,765,301,339,225,397,761,565,226
522,826,158,819,717,185,938,407,616,808,590,315,497,663,441,711,100,673,495,944
92,897,757,843,103,850,526,311,605,457,571,757,691,73,617,802,944,91,307,693
294,530,490,500,139,283,702,897,693,787,339,127,876,656,868,428,986,138,800,146
790,56,355,50,932,613,600,456,342,579,332,123,321,862,865,154,198,459,371,240
234,232,725,96,492,207,88,287,412,851,322,242,615,571,615,112,255,94,935,498
143,280,616,74,107,646,66,821,833,280,585,532,520,240,897,492,825,731,411,298
826,938,144,606,107,870,281,283,679,431,402,634,352,872,557,617,554,878,234,123
549,812,138,621,877,317,848,719,861,576,715,586,669,122,462,110,795,273,584,593
527,857,596,304,85,285,152,595,150,366,559,186,813,97,77,302,432,781,658,572
864,53,95,605,407,532,115,424,187,261,612,628,356,212,711,781,585,52,119,556
592,150,112,784,118,567,282,458,801,552,276,104,342,51,726,577,328,993,600,308
205,460,237,496,871,290,453,598,313,715,156,792,103,616,425,144,83,591,124,683
324,119,76,207,553,618,748,523,839,605,370,801,388,631,245,820,391,902,14,558
695,161,119,400,186,527,215,836,158,412,834,130,723,708,579,731,394,144,152,889
487,7,900,80,942,143,704,460,396,63,328,116,336,59,491,624,550,150,932,117
593,567,215,155,157,556,709,832,371,620,291,520,504,831,674,405,132,798,394,594
159,704,526,304,706,826,948,773,860,845,121,833,62,873,529,589,707,285,203,752
237,55,352,81,94,549,286,745,52,65,423,90,840,479,489,229,389,7,394,679
125,445,530,731,559,141,709,95,327,599,319,306,855,120,86,731,150,813,578,370
782,120,771,701,99,845,339,273,492,535,83,501,818,51,602,304,938,562,267,80
949,875,854,63,761,409,66,902,872,573,788,87,849,60,428,531,557,241,141,375
546,457,754,288,936,718,696,936,142,144,227,76,577,77,327,561,690,615,479,809
590,230,490,430,237,53,21,149,860,546,625,725,592,521,768,809,814,554,143,566
85,794,406,226,837,625,749,105,615,201,144,339,159,198,526,872,855,592,660,874
236,794,314,69,566,54,134,535,93,827,266,558,593,775,606,493,593,939,877,683
410,619,314,57,889,67,74,706,943,601,789,718,723,928,150,147,233,218,798,494
603,121,706,79,455,349,309,876,85,433,123,278,89,521,995,709,533,895,124,242
824,751,392,85,152,394,730,845,138,864,438,493,611,490,2,529,858,808,89,403
604,156,408,319,205,889,493,841,858,858,315,412,849,298,689,352,869,330,57,489
903,131,330,789,84,723,130,677,553,786,398,873,564,700,225,333,846,763,983,557
205,585,749,863,747,559,495,889,332,564,535,236,51,687,326,712,336,530,580,573
416,564,763,937,322,233,311,829,268,456,439,310,114,570,604,389,308,111,153,939
286,799,300,595,553,340,224,348,292,802,577,87,80,215,725,624,621,522,54,430
227,899,753,994,83,430,297,726,290,869,847,713,898,51,682,138,98,153,101,817
180,429,353,120,409,554,710,97,403,115,586,425,354,302,289,871,528,284,795,478
946,530,149,59,289,305,761,788,429,630,135,216,521,250,266,746,838,531,458,247
546,867,552,244,125,205,139,617,758,77,940,315,423,137,539,111,105,616,489,899
628,134,633,247,188,710,613,898,425,589,278,115,340,784,893,707,752,854,934,428
213,291,106,840,903,609,197,570,160,563,812,211,479,248,186,527,814,201,825,674
492,279,417,323,559,893,567,426,485,185,660,725,827,240,840,127,248,939,113,248
545,758,145,808,839,397,160,342,399,427,354,337,820,269,126,314,830,214,553,283
326,854,727,140,695,704,605,54,285,221,570,230,948,92,313,603,876,85,427,867
528,658,333,353,644,805,555,867,520,478,440,747,570,838,837,867,269,267,298,318
235,301,377,286,709,436,209,676,758,753,187,873,325,225,594,297,528,126,836,821
834,877,604,614,895,95,583,100,834,275,679,659,869,127,753,56,269,117,894,359
423,622,839,118,546,94,424,674,233,289,305,711,612,704,867,581,381,428,307,719
613,234,763,128,100,659,52,599,628,65,284,206,86,977,499,457,292,457,433,822
432,131,187,859,93,432,311,142,696,737,495,55,433,680,50,840,397,339,67,230
148,207,781,146,376,307,798,103,101,340,758,877,817,903,621,144,212,317,538,812
677,794,241,877,53,576,600,717,704,293,309,402,166,830,610,120,871,807,727,863
154,571,755,779,595,523,723,233,57,801,283,293,592,759,615,409,627,50,599,893
330,61,207,248,389,763,455,52,594,610,980,838,405,295,237,697,547,307,432,302
150,312,893,621,138,601,709,265,640,210,609,628,487,104,856,831,53,814,819,824
899,584,484,608,897,838,299,66,673,723,896,247,345,898,349,71,286,402,483,799
900,984,83,844,214,727,423,215,876,809,411,110,109,588,423,228,273,850,268,589
601,91,895,869,890,677,899,629,139,136,703,674,746,841,292,555,67,548,589,641
774,51,501,132,390,79,323,595,356,801,90,594,553,599,214,434,674,316,424,304
191,593,69,695,820,111,857,338,945,786,95,68,481,75,315,764,839,202,610,847
830,659,227,353,60,841,580,745,397,488,615,289,457,840,917,278,102,401,866,401
128,697,89,411,231,801,875,759,893,52,792,275,251,532,609,948,481,582,837,683
168,110,488,799,811,721,230,116,901,939,763,154,157,439,208,901,538,809,434,896
559,893,768,314,59,214,406,614,427,587,228,783,712,948,898,868,447,101,891,413
382,292,900,580,878,90,458,699,790,796,490,204,431,763,462,321,547,427,867,233
213,525,616,90,588,365,683,535,411,789,555,794,706,392,486,354,62,490,895,396
390,130,534,768,534,58,708,388,830,139,155,59,107,560,781,794,96,774,266,397
436,947,800,680,311,933,117,315,700,487,113,659,679,443,936,604,67,480,457,825
146,678,631,329,576,930,606,641,758,231,435,555,393,609,933,90,299,339,110,341
333,205,893,746,728,566,945,497,459,848,934,848,328,125,484,990,710,265,756,61
812,813,392,428,456,566,386,498,611,582,810,553,440,364,210,316,129,792,842,495
447,323,339,202,57,300,108,824,681,293,150,301,892,803,100,657,76,767,293,238
354,425,947,82,520,531,314,751,318,289,413,386,617,483,220,801,341,392,523,626
126,707,241,765,159,822,645,478,441,423,930,55,525,797,340,804,154,682,547,272
935,434,621,428,137,546,602,828,334,840,859,229,847,934,363,727,716,158,724,423
945,796,432,730,836,872,606,359,111,100,762,328,938,596,121,439,430,623,424,405
369,863,384,767,68,295,498,136,307,111,493,602,75,16,433,123,294,138,70,695
250,158,312,730,368,579,731,436,201,572,125,929,557,483,755,270,352,76,308,784
91,439,242,229,565,225,499,725,557,452,121,902,928,394,399,202,821,874,110,578
478,745,179,783,616,91,441,481,132,389,930,446,751,321,719,627,486,250,722,817
532,428,853,141,789,809,295,63,944,424,727,929,361,457,274,147,82,747,397,432
572,194,701,314,266,560,844,898,209,462,631,283,109,716,901,69,320,931,289,153
822,583,223,249,845,157,595,844,945,93,676,892,696,557,610,866,411,369,799,935
529,267,371,558,490,64,83,122,211,242,291,487,862,949,676,243,878,862,479,997
749,201,700,656,584,790,842,411,598,826,135,620,317,298,713,623,756,405,648,75
501,224,297,621,784,812,702,867,573,877,290,60,499,243,283,349,495,384,897,209
941,904,67,723,232,435,809,675,241,695,487,154,394,564,602,934,423,590,602,157
569,80,314,857,132,757,309,123,395,919,598,461,141,723,245,795,213,54,227,480
386,298,54,248,289,889,689,125,108,399,699,494,353,554,291,497,323,124,142,828
57,392,748,371,749,379,302,814,891,295,731,599,863,865,840,857,132,801,813,590
353,708,745,292,406,461,107,271,945,658,561,403,408,497,419,225,71,945,274,435
554,265,329,139,117,778,844,52,66,555,459,866,839,728,796,413,696,369,75,898
912,714,326,210,536,461,313,356,70,227,762,108,948,494,561,603,215,525,207,353
734,581,51,621,655,405,278,148,398,822,719,102,126,868,835,61,484,125,279,137
295,299,486,299,808,712,809,280,266,172,495,832,788,269,903,59,315,331,211,325
546,489,981,818,245,482,401,807,330,590,270,596,847,401,94,66,762,895,839,356
293,439,944,603,351,723,423,336,240,342,390,931,385,458,855,622,367,484,836,562
302,90,531,622,790,585,797,282,228,412,100,441,474,104,209,118,656,678,556,714
249,662,494,535,481,319,72,63,277,385,146,523,237,564,703,839,386,862,88,586
65,75,727,754,804,80,292,232,55,147,602,826,320,781,200,414,709,623,403,596
99,290,484,538,525,302,202,837,300,689,797,307,440,616,334,322,939,784,726,601
759,484,324,225,855,128,674,933,60,183,893,902,146,948,615,890,823,656,835,278
580,108,441,60,624,352,125,626,84,381,127,273,226,548,657,409,396,806,560,941
128,487,404,980,340,112,298,843,249,756,178,711,899,930,402,231,123,818,248,277
637,145,557,792,54,69,817,348,708,130,897,225,145,57,941,554,280,204,140,603
793,818,172,311,319,213,695,185,599,58,714,942,459,159,614,394,384,610,263,461
501,140,704,795,330,223,432,314,333,761,340,481,570,120,730,620,388,249,825,61
858,842,458,900,332,317,802,875,250,613,938,377,675,827,585,228,484,891,356,414
684,328,570,67,369,497,565,314,814,325,53,781,214,71,430,746,866,307,188,729
428,823,677,67,337,122,489,676,815,84,129,270,270,502,835,930,58,765,613,841
762,782,186,572,109,607,398,204,210,750,833,618,62,396,558,579,242,408,485,20
860,398,675,413,412,869,178,83,113,758,82,98,197,546,438,749,97,108,899,81
571,484,104,571,125,585,811,411,273,813,659,461,848,463,682,630,214,317,107,528
611,461,595,206,102,696,460,620,434,600,834,244,698,262,233,386,713,604,859,617
597,804,584,138,606,596,327,245,128,601,105,580,220,536,598,388,621,572,605,297
325,314,866,929,854,876,124,285,249,76,595,857,179,434,6,272,304,179,621,570
149,694,698,609,729,870,862,316,596,501,975,562,411,384,674,408,55,799,58,676
832,702,8,85,354,398,723,157,226,560,799,945,609,789,233,390,492,590,305,731
756,704,397,946,203,352,812,394,568,719,828,599,922,612,234,311,695,717,696,61
265,401,396,813,898,978,603,430,391,78,131,524,322,716,370,751,658,424,606,680
947,280,941,533,151,599,895,89,407,316,524,270,127,213,375,550,600,764,631,69
873,411,244,814,123,393,305,264,247,235,132,553,327,827,696,622,225,0,766,88
245,373,102,58,933,660,237,858,128,585,126,615,614,407,627,693,674,548,835,731
598,875,206,130,275,334,622,800,412,624,932,99,284,871,593,759,930,359,675,325
730,891,101,58,487,326,61,153,819,305,558,894,558,578,731,323,270,138,980,461
560,94,685,595,858,897,459,304,428,116,750,355,91,563,709,424,534,938,399,265
808,263,832,567,386,758,564,929,869,589,418,406,114,434,209,85,309,849,295,835
938,855,937,459,385,706,326,846,696,839,318,479,75,801,71,399,858,444,943,570
864,627,81,233,796,751,156,285,533,147,216,893,847,703,133,797,291,124,135,604
868,599,337,765,119,564,850,566,489,731,198,104,532,493,396,677,571,722,113,81
405,727,561,245,703,551,340,658,783,640,750,848,588,320,583,725,571,370,280,284
579,215,849,126,568,484,151,53,828,833,639,934,289,461,785,493,891,807,111,501
283,841,600,760,211,844,338,731,628,853,947,934,525,150,821,79,774,396,74,148
349,188,314,551,335,249,790,808,341,248,141,298,446,279,242,352,807,301,579,431
58,803,935,263,712,535,128,891,831,870,758,850,178,726,61,841,663,870,785,234
699,818,574,844,616,933,492,54,624,137,369,719,298,934,169,786,529,933,273,292
388,680,840,211,329,397,160,798,395,821,272,275,948,930,158,794,978,529,932,861
616,706,497,433,275,858,439,126,561,492,328,990,530,389,789,584,231,938,625,899
593,594,196,584,715,134,768,317,306,816,298,613,87,840,705,531,594,530,457,701
400,813,838,803,565,349,529,822,248,541,610,302,500,802,811,534,929,348,72,98
597,13,124,58,146,265,857,939,531,745,201,298,159,538,411,601,678,395,246,125
458,87,435,932,244,597,58,722,234,308,789,551,240,223,768,153,311,440,697,876
725,815,491,68,391,96,305,816,65,490,483,146,548,583,715,682,920,494,151,783
535,928,117,838,561,856,367,244,591,898,71,318,590,325,496,716,129,318,69,96
489,764,761,51,500,267,858,869,786,626,499,522,753,624,73,584,281,196,237,147
793,791,577,870,411,814,336,712,816,874,367,60,521,135,66,298,855,616,582,558
259,102,136,423,310,752,486,486,229,456,371,246,725,585,869,406,430,703,456,549
390,82,485,86,899,23,264,946,529,819,901,868,846,67,932,873,149,385,761,746
334,892,658,657,584,725,998,703,436,609,308,756,683,556,794,403,753,764,622,349
602,391,715,479,116,762,148,269,403,151,768,263,857,184,762,749,95,231,934,629
303,337,657,69,622,839,603,95,294,675,803,787,628,424,55,459,421,766,323,399
'''.strip().splitlines()



all = []
mode = None
answer=0
for line in data:
	if line == 'your ticket:':	
		mode='your'
		continue
	elif line == 'nearby tickets:':
		mode='nearby'
		continue
	elif line == '': continue

	if mode is None:
		type, ranges = line.split(': ')
		ranges = ranges.split(' or ')
		for r in ranges:
			all.append([int(value) for value in r.split('-')])
	elif mode == 'nearby':
		for ticket in line.split(','):
			ticket = int(ticket)
			for r in all:
				if r[0] <= ticket <= r[1]: break
			else:
				answer += ticket

print(answer)

all = []
keyedRanges = {}
outputTickets=[]
mode = None
for line in data:
	if line == 'your ticket:':	
		mode='your'
		continue
	elif line == 'nearby tickets:':
		mode='nearby'
		continue
	elif line == '': continue

	if mode is None:
		type, ranges = line.split(': ')
		ranges = ranges.split(' or ')
		keyedRanges[type] = []
		for r in ranges:
			all.append([int(value) for value in r.split('-')])
			keyedRanges[type].append([int(value) for value in r.split('-')])
	elif mode == 'nearby' or mode == 'your':
		for ticket in line.split(','):
			ticket = int(ticket)
			valid=True
			for r in all:
				if r[0] <= ticket <= r[1]: break
			else:
				break
		else:
			outputTickets.append([int(value) for value in line.split(',')])

N=20
#N=3
possible=[None for value in range(N)]

print(outputTickets)

for ticketRow in outputTickets:
	for index, ticket in enumerate(ticketRow):
		this = []
		for type, ranges in keyedRanges.items():
			valid=False
			for r in ranges:
				if r[0] <= ticket <= r[1]:
					valid=True
					break
			if valid:
				this.append(type)

		if possible[index] is None:
			possible[index] = this
		else:
			for possibleThing in possible[index][:]:
				if possibleThing not in this:
					print('removing', index, possibleThing)
					possible[index].remove(possibleThing)
			if len(possible[index])==1:
				for index2 in range(len(possible)):
					if index2 != index and possible[index][0] in possible[index2]:
						possible[index2].remove(possible[index][0])
			for type, ranges in keyedRanges.items():
				count=0
				for index2 in range(len(possible)):
					if type in possible[index2]:
						count+=1
				if count == 1:
					for index2 in range(len(possible)):
						if type in possible[index2]:
							possible[index2] = [type]

print(possible)
answer=1
for index, ticket in enumerate(outputTickets[0]):
	if possible[index][0].startswith('departure'):
		answer*=ticket
print(answer)

