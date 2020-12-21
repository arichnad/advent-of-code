#!/usr/bin/python3


data='''
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
'''.strip().splitlines()
data='''
tksps nmzblnq pzz gkmdkp fdpp htdps njvzpr lsfn vxbnd qvft rggkbpj nmpt ptq dckbmh bh xxlb pbjp zlpbptr mmphj ddc zxmkkpp jrgrcz xzhmdb mqkf bmcj nmtzlj dxzq lsv bsbz fvqg mklt dlkxsxg nkmj crbt zxcqtf rjbsr hbcgjtx vvqpqgl rnbfzg hxndkq vrntfjx clmk zdslsk ljczhn fkntrq kbkkrlfq bt mrz nhpsk lsc vqjj gpxmf lfd bsllxjtm zdpcb qpjplfl gkcskhp vrbxt mxf ftnhrx fbjbkp sffzz (contains fish, soy)
pzvvt phth fvqg mlftm gpxmf kbkkrlfq nmtzlj dtqq jdnlg dlxp ljczhn zrngn qnlrbn lbxc chjdk fkntrq xxlb pcvh xmgc vkzh pzz sgv xlc xmjr bqtpqsp vrntfjx xxx dlkxsxg xzhmdb vpsd clptg qpjplfl fcrvj nmzblnq cxgmp jqcfq sbr xbdmll jtknrjp fcdtf bbxvmgs mgjdd dckbmh lmxt dxzq ns fdpp pbjp xbtpfxjz fbvdlb mrz ftnhrx fsddds hsmkqgx gkmdkp xxdmj cksrd zgbbl zdslsk zpqbb bgkf rnbfzg bhgzdg ndmjr nhpsk mxf fjndll cfnc pmqmmxs rqpd mqkf snpxpkvj (contains shellfish)
bh dxzq zbsqdm lxkbkkx lcpcmk xbdmll ttszmr pzvvt jbhhjx qfqnpf dckbmh zgbbl vrbxt rggkbpj dzbxmn bsllxjtm dblf mlftm fvqg htdps ldprd tllqrt sfprzmk zrngn lmxfpn hxndkq gkcskhp bqtpqsp chjdk kzfsztx nkmj tjxxdmq ztlp dlkxsxg vvzf vplt bhgzdg gsshb lmxt bmjx fjndll clmk qbrgtl ndmjr nmtzlj xzhmdb bpzlm kspf gvhrgz ddcrr fdpp tlgbjhs gpxmf xvqmjsc lsc mqkf lsv krrsrp zsbzn bkxnht mgjdd jbtjxtf slbrp kchnq vpsd zdpcb ftnhrx sm mcdsfh xplxv fkntrq gntk tksps sbr vbxdp vtdd lrbpxs dgnrq ktm (contains sesame, eggs, peanuts)
xlc dlkxsxg jrgrcz lkdrpt rqpd xgzbl fjndll ddcrr xbhsqv pqjgdkl fvqg mxf lxkbkkx kttchg vvzf xxdmj xzhmdb pbjp fcdtf kbkkrlfq bpzlm qlbxr lmxt rggkbpj ptq kzfsztx dgnrq jbhhjx vqjj qnlrbn kckgz cnmm nmtzlj zgbbl lrbpxs ztlp hnlcp zhlgsj bgkf zdpcb xbtpfxjz bsllxjtm krrsrp pzz nhpsk mrz ndmjr zmqvhh xxlb dxzq bqtpqsp zsbzn (contains dairy, sesame)
qlgb ztlp gvhrgz sfprzmk vcvmq xxlb lmxfpn njrdhq lcpcmk ttszmr qbrgtl tnzvgg hbfmpsg hshl vvqpqgl pzz dckbmh zlpbptr slbrp xgxk dlkxsxg mxf qlbxr bmcj bqtpqsp hsmkqgx ftnhrx qmxfh fvqg lbnr hbcgjtx krrsrp nmpt fxznf zpqbb lmxt vbxdp dtqq dxzq zdslsk nmtzlj mgjdd gpxmf vtdd kttchg rdtkzbf qfqnpf ndmjr zrngn (contains wheat, fish)
ttszmr bqtpqsp qvft nhpsk qfqnpf pcvh dxzq qmxfh cksrd xxlb mcdsfh bhgzdg nklz fcdtf mqkf pkzjrp phth zpqbb xvqmjsc pbjp dlxp fcrvj sfprzmk hnlcp xbtpfxjz hxndkq gkmdkp vxbnd pzz clptg mlftm nmzblnq pmqmmxs cpjsfp gpxmf cfnc xmjr nmpt sbr vvqpqgl fxznf mcrxr hgvszq ftnhrx dlkxsxg vpsd vqjj bsbz pmvs gntk fvqg bt kckgz fzpcbck ddc tjxxdmq vjpcxq nmtzlj mxf lmxt prjcx pzvvt mgjdd (contains fish)
njrdhq xxx sffzz cksrd gvhrgz nkmj xvqmjsc mxf dxzq jglfn cxgmp fkntrq vxbnd bkdpdr ddcrr hxndkq jclqn mrz vrntfjx fbjbkp nmpt slbrp mcrxr tnzvgg krrsrp jtknrjp hsmkqgx gpxmf pmqmmxs xxlb pbjp ndmjr xlc sbr gxnxkkh bsd kzfsztx vvzf qmxfh jrmj tksps kchnq dgnrq nmfd mcdsfh zmqvhh bcv qvft gsshb kspf lsfn zxmkkpp pqjgdkl fvqg tlgbjhs hgvszq nmtzlj xbhsqv rggkbpj rqpd xmgc kfghxt tjxxdmq bmcj rjbsr fmfj zhlgsj zsbzn xmjr ktm fcrvj pzvvt vbxdp zpqbb pkzjrp fcdtf ddc crbt kckgz dmrxd pmsjc lmxt nmzblnq phth qpjplfl fsddds vplt bsbz (contains dairy, wheat)
dlkxsxg vplt nkmj bmjx vvzf rdtkzbf qpjplfl tlgbjhs hsmkqgx dxzq mgjdd bsd mklt xmjr gpxmf xxdmj bkdpdr fbjbkp fvqg ktm crbt mxf nmtzlj vpsd pzz fzpcbck krrsrp zpqbb cvrqg vcvmq xxlb vtdd htdps vvqpqgl lsv clptg kttchg jbtjxtf ljczhn vjpcxq dblf sfprzmk bqtpqsp dgnrq fcdtf dzbxmn pzvvt chjdk jtknrjp rggkbpj vf ptq ddcrr lsc njvzpr jrgrcz gkmdkp nklz lsfn ttszmr jrmj mqkf jglfn jdnlg pmvs dtqq (contains fish, wheat, shellfish)
bsd jbtjxtf nmtzlj njvzpr dlkxsxg dblf hqvv bkxnht dzjjxr xbtpfxjz fxznf cvrqg qpjplfl kspf fcdtf hbcgjtx mxf lsfn zhlgsj dmrxd lsc lkdrpt nmpt dlxp hshl jclqn fkntrq sffzz lxkbkkx lsv dxzq mcrxr mgjdd bt zxcqtf zgbbl bh rggkbpj pthjxs htdps gpxmf pkzjrp fbjbkp lmxt vbxdp kbkkrlfq pmvs pcvh zdpcb ns (contains peanuts, fish, dairy)
vrntfjx dxzq zdpcb vbxdp lmxt jbtjxtf zhlgsj xbdmll qlbxr xmjr qpjplfl pqjgdkl gsshb rggkbpj fkntrq mcdsfh ddcrr bt fbvdlb jqcfq bgkf dtqq fmfj ddc bsllxjtm kbkkrlfq cpjsfp jbhhjx qlgb vrbxt fbjbkp gntk zrngn kckgz nmtzlj zlpbptr qvft hnlcp lrbpxs bkxnht dlkxsxg cksrd vqjj sgv dmrxd slbrp rkzkd pthjxs cvrqg fcrvj vtdd kchnq qbrgtl mlftm mxf fdpp zmqvhh jrgrcz pzz kttchg xvqmjsc pcvh ttszmr fvqg pzvvt bmjx gkcskhp gvhrgz (contains eggs, fish)
cnmm lmxt krrsrp kbkkrlfq fvqg dlkxsxg gpxmf gsshb vbxdp sgv kzfsztx zbsqdm kttchg gvhrgz rkzkd jtknrjp hsmkqgx rjbsr hbcgjtx bsllxjtm dmrxd dzbxmn jglfn vpsd tsnzbdtb vcvmq xxx zlpbptr fbjbkp lbnr dxzq hnlcp mcrxr rggkbpj tllqrt lsc fjndll bbxvmgs tksps bmjx xmjr mlftm nmtzlj (contains eggs, dairy, shellfish)
qlgb ljczhn tjxxdmq gpxmf mrz kttchg pzz xmjr vvzf ktm zhlgsj zsbzn dckbmh lmxt nmtzlj vcvmq jglfn zxmkkpp fxznf xmgc hgvszq zlpbptr mxf hbfmpsg tsnzbdtb dxzq lkdrpt vbxdp pqjgdkl mlftm nhpsk ptq vjpcxq gsshb cfnc ddcrr kckgz bh kzfsztx tnzvgg fvqg dblf xbdmll vkzh pmqmmxs dlkxsxg vplt nklz xplxv gvhrgz lsfn jclqn lxkbkkx prjcx mklt hsmkqgx vtdd sm (contains sesame, peanuts, fish)
vrntfjx rjbsr bmcj lxkbkkx pmqmmxs zpqbb zmqvhh cfnc nmtzlj dgnrq qpjplfl fcdtf zsbzn fvqg zrngn vqjj dlkxsxg nmzblnq ldprd qvft fzpcbck xxx cpjsfp xlc lmxt clptg tksps sffzz vvzf mxf rggkbpj gvhrgz jrgrcz nhpsk lmxfpn dzjjxr sgv tjxxdmq pbjp jdnlg tllqrt vxbnd htdps tlgbjhs lfd gpxmf pmsjc jglfn nmpt xbtpfxjz vplt gntk (contains shellfish, peanuts, fish)
vtdd zdslsk rqpd zdpcb vkzh clptg ldprd jglfn ztlp mxf vrbxt vplt zbsqdm zhlgsj crbt bcv nhpsk jbtjxtf tllqrt xbtpfxjz pzvvt lkdrpt kttchg tlgbjhs vvzf kbkkrlfq fbvdlb sffzz ddcrr rggkbpj dlxp dckbmh gvhrgz bgkf dxzq fvqg hxndkq lbnr slbrp bsd hsmkqgx zpqbb gntk lcpcmk lmxt ptq gxnxkkh nkmj vf xgxk hgvszq ns jdnlg dlkxsxg qmxfh ddc mqkf fkntrq njrdhq gpxmf gkmdkp (contains shellfish, dairy)
gpxmf qmxfh bh lbnr fvqg lsc xlc rggkbpj fzpcbck fbvdlb njvzpr qlgb gkmdkp xxx nhpsk bcv nmtzlj cpjsfp lmxt rjbsr vvzf tsnzbdtb lbxc ptq xvqmjsc mxf lrbpxs qpjplfl rqpd tjxxdmq ktm qlbxr sfprzmk dlkxsxg xgxk ldprd phth fcdtf dmrxd vtdd zmqvhh nmfd xxlb qvft mlftm bpzlm zlpbptr fjndll vqjj zpqbb kbkkrlfq vf (contains eggs, fish, soy)
gvhrgz xplxv lsfn mmphj nmpt dzjjxr qnlrbn tjxxdmq slbrp chjdk kchnq ftnhrx xxdmj gkcskhp rkzkd mcdsfh nmtzlj tlgbjhs hgvszq bqtpqsp bmjx ndmjr hxndkq xxx dzbxmn htdps ldprd xmjr jclqn rggkbpj mxf qbrgtl pbjp zxcqtf zlpbptr xlc hbfmpsg hshl lrbpxs lsv vplt vf mklt gpxmf tsnzbdtb sm bcv lmxt bhgzdg pmvs fbvdlb clptg sbr pmsjc tllqrt fkntrq kckgz fsddds lsc xbhsqv zmqvhh bpzlm qvft fbjbkp lcpcmk vrntfjx fvqg mqkf vxbnd dlkxsxg rdtkzbf ljczhn ptq fcrvj vpsd (contains soy)
rkzkd qfqnpf zrngn ftnhrx lmxt lkdrpt qnlrbn fvqg ljczhn hxndkq vrntfjx xplxv lxkbkkx bqtpqsp tksps mxf mgjdd pmqmmxs crbt zgbbl dzjjxr fsddds pzvvt lrbpxs lcpcmk pthjxs qlgb gpxmf zmqvhh rggkbpj dgnrq nhpsk lsv bkdpdr fdpp vkzh vvzf dxzq dlkxsxg sbr vtdd nmzblnq bt zdslsk tjxxdmq xxlb njrdhq xbdmll clmk pcvh mcdsfh (contains shellfish, dairy)
hsmkqgx crbt lbnr jtknrjp bt nhpsk htdps hgvszq xplxv zxcqtf cnmm jbhhjx gkmdkp nmtzlj xzhmdb ddcrr gkcskhp pbjp fjndll xbhsqv lmxfpn dgnrq kttchg dxzq mcrxr sffzz vbxdp dmrxd hbcgjtx fvqg qlgb xbdmll mxf dtqq rggkbpj bgkf gpxmf cpjsfp vpsd lmxt qpjplfl fxznf ftnhrx jglfn (contains peanuts, wheat, sesame)
dmrxd fmfj jglfn mqkf zdslsk pmqmmxs xmgc lxkbkkx ndmjr dblf kckgz crbt zmqvhh dzjjxr pkzjrp nmtzlj mgjdd fvqg cpjsfp sm vxbnd kzfsztx sffzz fbvdlb zhlgsj gsshb fjndll hshl rjbsr lsv jqcfq jbtjxtf bkdpdr htdps bsd mrz kttchg kbkkrlfq xzhmdb bhgzdg fkntrq lmxfpn qnlrbn bkxnht njrdhq mklt kchnq cvrqg mcdsfh nmfd xxlb lbnr bh pzz dxzq vvqpqgl fsddds mxf jrmj dlxp lmxt tjxxdmq gpxmf ddc vrbxt hbfmpsg lbxc pzvvt qlbxr sbr hnlcp rnbfzg ttszmr fbjbkp fzpcbck dlkxsxg vkzh lsfn rdtkzbf gkcskhp fdpp (contains shellfish, peanuts, dairy)
sgv bpzlm vvqpqgl rkzkd dzbxmn phth zsbzn tllqrt bh cpjsfp lmxfpn dlkxsxg mgjdd fbvdlb xzhmdb zbsqdm nhpsk zrngn slbrp zdslsk qnlrbn zmqvhh xxx lxkbkkx pqjgdkl cvrqg jglfn vpsd lsc dxzq hsmkqgx mxf zdpcb gntk xbdmll dgnrq xxdmj dckbmh ldprd rqpd bqtpqsp fvqg gpxmf rggkbpj xbhsqv bcv qlgb gsshb nklz lbxc sffzz lmxt ftnhrx kfghxt nmzblnq kttchg bmcj cnmm snpxpkvj bgkf pmsjc zxcqtf bhgzdg jdnlg zgbbl fsddds ztlp fkntrq (contains wheat, eggs)
bbxvmgs dlkxsxg bsbz cksrd htdps jrmj fvqg lkdrpt bqtpqsp hshl tnzvgg zxcqtf mklt zsbzn cfnc ns clptg zhlgsj hnlcp jtknrjp tksps vrntfjx fbjbkp gxnxkkh lmxt sffzz rggkbpj sfprzmk bkdpdr xmgc rjbsr lcpcmk vjpcxq nmpt kzfsztx qmxfh nkmj xgzbl jqcfq bh fmfj dblf mxf gpxmf sbr sm gkmdkp nklz vcvmq zdslsk dxzq xbdmll pmvs mrz xlc xxlb lbnr fjndll dzbxmn mqkf xzhmdb nmzblnq zdpcb nmfd lsv qlgb snpxpkvj kchnq qfqnpf lsfn mmphj pkzjrp vbxdp (contains fish)
vqjj vtdd nmzblnq lbxc zxcqtf xplxv zdpcb lbnr qvft xbtpfxjz bmjx dlkxsxg zmqvhh pzz xxdmj nkmj vvqpqgl bsd tllqrt bpzlm lrbpxs dtqq fvqg lmxfpn lkdrpt fbvdlb vcvmq cnmm dckbmh pmqmmxs tksps njrdhq clptg rggkbpj gpxmf ztlp chjdk tsnzbdtb sgv htdps xmjr kckgz cxgmp dmrxd dblf vpsd rqpd rdtkzbf nmtzlj sm vrntfjx bhgzdg lmxt dxzq ktm cpjsfp ttszmr fdpp kfghxt (contains soy)
mmphj vvzf fjndll zxcqtf gsshb crbt dtqq cfnc bkdpdr qlbxr fcdtf mxf lcpcmk zdpcb lrbpxs hnlcp zmqvhh snpxpkvj vtdd qpjplfl rggkbpj vrbxt nmfd pzz dlxp jrgrcz vpsd xzhmdb bmjx lkdrpt kzfsztx bqtpqsp jbhhjx pcvh fkntrq chjdk xlc jglfn fsddds tnzvgg mrz ktm gpxmf hbcgjtx lmxfpn jbtjxtf dxzq fvqg zgbbl dlkxsxg ddcrr sgv zxmkkpp kbkkrlfq hxndkq clmk pmqmmxs rdtkzbf mlftm lmxt sffzz tjxxdmq jqcfq xgzbl (contains peanuts)
qlgb rggkbpj zgbbl lmxt bgkf nmtzlj crbt pcvh clptg hnlcp fzpcbck mqkf kzfsztx hbfmpsg zmqvhh zdpcb pqjgdkl ptq mmphj pmvs vplt xbhsqv mcdsfh rnbfzg sfprzmk cfnc zhlgsj fvqg jbhhjx lfd ztlp lcpcmk lxkbkkx cvrqg njvzpr hbcgjtx ktm mxf xbtpfxjz zlpbptr vbxdp ljczhn nmpt fcdtf tnzvgg qlbxr gpxmf hgvszq xgzbl xzhmdb jrgrcz bbxvmgs mgjdd nklz cnmm bmjx bpzlm dmrxd dckbmh kckgz vqjj lbxc dlxp hshl nkmj fxznf fkntrq clmk bsbz xxdmj vvqpqgl vxbnd chjdk pzvvt dlkxsxg vjpcxq (contains dairy, peanuts)
qvft zmqvhh gpxmf dlxp zdpcb tlgbjhs fmfj pzz ns bhgzdg vxbnd phth clmk vkzh clptg rggkbpj xmgc lrbpxs dckbmh bmjx fjndll mmphj fcdtf cxgmp lfd vvzf ftnhrx ljczhn lmxt njrdhq dtqq bkxnht zdslsk lsv bsd mlftm bqtpqsp ndmjr mcdsfh kttchg cpjsfp hqvv fbvdlb pmqmmxs sbr tnzvgg kbkkrlfq lkdrpt xlc nmtzlj xvqmjsc fbjbkp ldprd fzpcbck cfnc fkntrq mxf rdtkzbf pmsjc xxx nhpsk jglfn zxmkkpp nmpt hshl xmjr dlkxsxg fvqg zpqbb fdpp vpsd pmvs (contains shellfish, peanuts, fish)
lbxc tksps mxf ddcrr nmtzlj fdpp zhlgsj xbdmll xlc xvqmjsc vxbnd fxznf clptg pzvvt crbt jbtjxtf rjbsr ddc lmxfpn jclqn mcdsfh xxlb nklz jrgrcz dlkxsxg bqtpqsp zrngn dgnrq clmk mklt ttszmr nmzblnq xzhmdb fkntrq zdslsk xmgc dblf ftnhrx kspf rggkbpj hshl lmxt fvqg dmrxd qvft dzjjxr lxkbkkx nmfd xgxk nhpsk gpxmf vjpcxq (contains soy, sesame, fish)
nkmj xplxv fvqg jglfn cxgmp zpqbb lsc tllqrt jclqn fxznf lmxt rggkbpj dlkxsxg pcvh xmgc vxbnd vvzf fsddds lmxfpn slbrp hxndkq gpxmf dmrxd snpxpkvj tsnzbdtb gntk phth bqtpqsp cksrd nmtzlj mklt lxkbkkx tnzvgg clptg gvhrgz mqkf rkzkd mrz hshl pthjxs bhgzdg bkdpdr sfprzmk mxf bbxvmgs (contains soy, shellfish)
clptg tllqrt xbtpfxjz mrz clmk ktm bmjx jclqn xgxk gpxmf nmzblnq lmxt bgkf kzfsztx jrgrcz fkntrq prjcx qbrgtl sffzz kckgz pmqmmxs zgbbl mxf xxlb tlgbjhs cvrqg rjbsr rggkbpj dxzq pmvs xmgc xplxv fsddds fxznf ddc fmfj qlgb xlc lfd hgvszq zmqvhh zhlgsj fzpcbck bhgzdg krrsrp gxnxkkh cksrd lxkbkkx chjdk vrntfjx bsd gkmdkp dblf bsllxjtm nmtzlj vplt mgjdd jglfn njrdhq qfqnpf nmfd sgv vf crbt dlkxsxg (contains wheat, sesame)
cnmm bbxvmgs nklz prjcx bmcj xxdmj cksrd pmvs vcvmq nmfd tllqrt dckbmh nmzblnq pkzjrp gxnxkkh vbxdp bh lmxt jrgrcz zhlgsj gpxmf rnbfzg ddcrr fcrvj qlgb pmsjc mgjdd zpqbb mxf vrbxt zdslsk dzjjxr qfqnpf vpsd sffzz mklt xbdmll hbcgjtx bt xplxv jglfn kzfsztx dlkxsxg fvqg htdps mcrxr dxzq ldprd nmtzlj vvqpqgl hnlcp kspf bpzlm qnlrbn (contains sesame, soy, fish)
njrdhq fzpcbck zsbzn xlc nklz clmk dzbxmn phth nmtzlj dxzq fcdtf chjdk bh slbrp kttchg vkzh bsd gpxmf kchnq lfd bbxvmgs cxgmp bgkf pbjp dlkxsxg xzhmdb hqvv rnbfzg kzfsztx sgv hgvszq zdslsk bkdpdr fsddds pzvvt bmcj sbr mxf ddcrr vbxdp cvrqg mcrxr ldprd ljczhn sffzz pkzjrp jclqn zmqvhh xgxk rggkbpj vvqpqgl cnmm kbkkrlfq xbtpfxjz hxndkq ftnhrx crbt vcvmq nhpsk gsshb bmjx xxlb dckbmh ns lsfn bkxnht bpzlm kfghxt xbhsqv bsllxjtm krrsrp qfqnpf tlgbjhs jbtjxtf tksps hbcgjtx vqjj xvqmjsc tsnzbdtb lrbpxs zhlgsj fjndll bqtpqsp bhgzdg ttszmr hsmkqgx jbhhjx hshl lsc mqkf lmxt jdnlg mgjdd xxx pmvs (contains shellfish, wheat)
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

