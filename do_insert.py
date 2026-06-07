import json
F="docs/zaiko_hoju_tracker.html"
s=open(F,encoding="utf-8").read()
wd="2026-06-07 23:01"
def rec(id,cat,title,iid,site,url,np,status,note,origSite=None,origUrl=None):
    return {"id":id,"category":cat,"workDate":wd,"ebayTitle":title,
            "ebayUrl":"https://www.ebay.com/itm/"+iid,"origSite":origSite,"origUrl":origUrl,
            "origPrice":None,"newSite":site,"newUrl":url,"newPrice":np,"status":status,"note":note}
items=[
rec("306981382432-qty0-20260607","フィギュア","ROUND1 Hazbin Hotel Rubber Figure Complete Set All 8 Types Japan Limited 2026 FS","306981382432","メルカリ","https://jp.mercari.com/item/m29492473062",9999,"listed","Qty0版。eBay New。新規Qty0。メルカリ即決『ハズビン・ホテルへようこそ ラバーフィギュア 全8種セット(ROUND1)』m29492473062 ¥9,999(新品未使用/送料込/1日前)。元価格不明・有効仕入で自動出品。$112.39で利益計¥1777/利益率10.15%。Qty0→1。SKU 306981382432_AI在庫補充。保存済。"),
rec("306970488416-qty0-20260607","プラモデル","Bandai Space Battleship Yamato 2199 Expansion Set 1/500 Plastic Model Kit","306970488416","メルカリ","https://jp.mercari.com/item/m14517827009",15500,"listed","Qty0版。eBay New。メルカリ即決『1/500 宇宙戦艦ヤマト2199 拡張セット』m14517827009 ¥15,500(新品未使用/未組立/送料込)。最安¥9,800は開封済(目立った傷)のためNew不一致で除外。元価格不明・自動出品。$165.77で利益計¥2650/利益率10.26%。Qty0→1。SKU noji_AI在庫補充。保存済。"),
rec("306970490418-qty0-20260607","フィギュア","Nendoroid Idia Shroud 1604 Disney Twisted Wonderland Figure from japan","306970490418","メルカリ","https://jp.mercari.com/item/m52270225967",16500,"listed","Qty0版。eBay Used(#conditionid3000維持)。メルカリ即決最安『ねんどろいど イデア・シュラウド 1604 特典缶バッジ付』m52270225967 ¥16,500(新品未使用/送料込/21時間前)。仕入は新品のためCondition Descriptionに英訳記載。元価格不明・自動出品。$171.00で利益計¥2723/利益率10.22%。Qty0→1。SKU noji_AI在庫補充。保存済。"),
rec("306981147027-qty0-20260607","Game","Final Fantasy VII Advent Children Advent Pieces Limited Box","306981147027","メルカリ",None,None,"skipped","Qty0版。eBay New。メルカリにAdvent Pieces:Limited完品BOXの在庫なし(キーホルダー/Tシャツ/ガイド等の同梱単品のみ)。試行KW:アドベントピース リミテッド/アドベントピーシズ/アドベントチルドレン 限定BOX。完品見つからずスキップ。"),
rec("306980666122-qty0-20260607","フィギュア","ASSASSIN'S CREED Shadows NAOE Hidden Blade Pure Arts 1/1 Scale Replica","306980666122","メルカリ",None,None,"skipped","Qty0版。eBay Used。公式Pure Arts AC Shadowsナオエ1/1ブレードレプリカの在庫なし。試行KW:アサシンクリード シャドウズ ナオエ ブレード/ブレード レプリカ。出てくるのはコスプレ自作品・他作品(Syndicate)ガントレットのみで別物。スキップ。"),
rec("306980246952-qty0-20260607","Game","PlayStation5 FINAL FANTASY XVI Edition DualSense Controller NEW Japan","306980246952","メルカリ",None,None,"skipped","Qty0版。eBay New。メルカリにFF16 DualSenseの新品(item_condition_id=1)在庫なし。最安¥6,900は中古(目立った傷/着払い)、他も美品中古・ジャンクのみ。New一致せずスキップ。試行KW:FF16 DualSense コントローラー/ファイナルファンタジー16 コントローラー。"),
rec("306979329264-qty0-20260607","Plush","SUPERJUNIOR YESUNG LIVE TOUR JAPAN MD Plush Keychain Set of 4 New","306979329264","メルカリ",None,None,"skipped","Qty0版。eBay New。メルカリにイェソンLIVE TOUR MDぬいぐるみキーホルダー4個セットの在庫なし(トレカ/マスコット/他メンバーのランダムトイ等)。セット4種一致せずスキップ。試行KW:SUPER JUNIOR イェソン ぬいぐるみ キーホルダー。"),
rec("306979299608-qty0-20260607","Apparel","BTS Jungkook Arirang Official T-Shirt M Size Kpop Merch From Japan","306979299608","メルカリ",None,None,"skipped","Qty0版。eBay New。メルカリにジョングク ARIRANG 公式TシャツMの一致なし(ぬい服/クッションカバー/トレカ/全員フォトT等)。近辺¥10,555は全員(member不一致)。スキップ。試行KW:BTS ジョングク アリラン Tシャツ。"),
rec("306970492101-qty0-20260607","Accessory","Gucci x Oura Smart Ring US 11 Black Luxury Health Tracker Gen 3 New Bluetooth","306970492101","メルカリ",None,None,"skipped","Qty0版。eBay New。Gucci/Oura出品OKだがメルカリにGucci x Oura スマートリング(US11/Gen3)の在庫なし。新しい高級スマートリングで出品ほぼ無し。スキップ。試行KW:Gucci Oura リング。"),
rec("306970491838-qty0-20260607","フィギュア","Emby Burning Godzilla Clear Yellow Sofubi Kit WF2026W Japan New Limited","306970491838","メルカリ",None,None,"skipped","Qty0版。eBay New。WF2026冬 EmbyバーニングゴジラクリアイエローソフビKitの在庫なし(極ニッチなガレキ)。試行KW:バーニングゴジラ ソフビ クリアイエロー/Emby ゴジラ ソフビ。スキップ。"),
]
block=",\n".join(json.dumps(it,ensure_ascii=False) for it in items)
marker="\n];"
idx=s.find(marker, s.find("var items = ["))
assert idx!=-1
new=s[:idx]+",\n"+block+s[idx:]
open(F,"w",encoding="utf-8").write(new)
import collections
c=collections.Counter()
for line in new.splitlines():
    m=line.find('"status"')
    if m!=-1:
        import re
        mm=re.search(r'"status":\s*"([^"]+)"',line)
        if mm: c[mm.group(1)]+=1
print("inserted",len(items),"-> total status:",sum(c.values()),dict(c))
