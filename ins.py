import json,os,collections
WD=os.environ["WD"]
F="docs/zaiko_hoju_tracker.html"
s=open(F,encoding="utf-8").read()
def rec(iid,title,site,url,np,status,note):
    return {"id":iid+"-qty0-20260717","category":"","workDate":WD,"ebayTitle":title,
            "ebayUrl":"https://www.ebay.com/itm/"+iid,"origSite":None,"origUrl":None,
            "origPrice":None,"newSite":site,"newUrl":url,"newPrice":np,"status":status,"tries":1,"note":note}
items=[
 rec("307066410273","Uma Musume 7th EVENT THE STAGE Attendee Bonus Merchandise Set","メルカリ","https://jp.mercari.com/item/m95513654942",13000,"listed","Qty0版 自動出品 Price$177 利益率13% New(未使用/完品)仕入をeBay Used枠へ(品質上位) 画像メルカリ入替済 メルカリ¥13000(m95513654942) tries:1"),
 rec("307065659119","Hatsune Miku x Seiko Happy 16th Birthday Watch Limited w/ Box Excellent JAPAN","メルカリ","https://jp.mercari.com/item/m46212358067",199800,"pending","Qty0版 高額品(¥199,800>=¥100,000)につき自動出品せず要承認。メルカリ唯一在庫m46212358067。eBay Used。tries:1"),
 rec("307063525441","Hatsune Miku Face Plush Backpack Ita Bag Mouth Official New Bemoe Bilibili",None,None,None,"skipped","Qty0版 メルカリ該当在庫なし(フェイスリュック/ビリビリ/公式/リュック各検索いずれも該当なし)。Bilibili/Bemoe官製フェイスリュックはメルカリ流通なし。スキップ。tries:1"),
 rec("307062411478","Demon Slayer Kimetsu Talking NEZUKO Plush Doll Stuffed toy W/ Box Anime Bandai",None,None,None,"skipped","Qty0版 eBay New(W/Box)。メルカリのおしゃべり禰豆子は中古のみ(¥900傷汚れ/¥1200中古/¥3100中古くし欠品)。New一致在庫なし・Used->New不可でスキップ。tries:1"),
 rec("307050401732","New RIBOSE Miss Kobayashi's Dragon Maid Iruru 1/6 scale Figure Anime Auth Japan","メルカリ","https://jp.mercari.com/item/m99576523936",21500,"listed","Qty0版 自動出品 Price$226 利益率13% New(未開封)一致 画像メルカリ入替済 メルカリ¥21500(m99576523936) tries:1"),
 rec("307044154703","Shimano 05 Dendou maru 4000HP Electric Reel Big Game Electric Reel Japan Used",None,None,None,"skipped","Qty0版 メルカリに05電動丸4000HPの一致在庫なし(4000HP=0件、4000は別モデルEC4000/部品/ボートのみ)。スキップ。tries:1"),
 rec("307044154004","Age13+ Yu-Gi-Oh OCG Artwork Series Mini Scroll Egyptian God Cards Set Limited","メルカリ","https://jp.mercari.com/item/m61308863882",5600,"pending","Qty0版 三幻神ミニ掛軸(表示グッズ/非TCG)。ARTWORK SERIES系が¥5600〜¥68500と版違い多数で対象版特定できず、eBay売価$556と仕入¥5600の乖離大->版/同一性不確実につき要承認。メルカリ最安New候補m61308863882。tries:1"),
 rec("307044153379","Age13+ KATO 10-2117 OUIGO Espana 5-Car Basic Set N Scale",None,None,None,"skipped","Qty0版 メルカリに型番KATO 10-2117(5両基本)なし。存在は10-1763(10両A&B ¥32500)の別セットのみ->型番不一致でスキップ。tries:1"),
]
block=",\n".join(json.dumps(it,ensure_ascii=False) for it in items)
marker="\n];"
idx=s.find(marker, s.find("var items = ["))
assert idx!=-1,"marker not found"
new=s[:idx]+",\n"+block+s[idx:]
open(F,"w",encoding="utf-8").write(new)
print("inserted",len(items),"; status:",dict(collections.Counter([it["status"] for it in items])))
