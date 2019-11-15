import requests
import json
from blog.models import Cafe

# APIキーの指定
apikey = "720080a2660c9bab99f283596cb1d67f"

# APIのひな型
api = "https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid={key}&latitude=35.689738&longitude=139.700391&range=4&freeword=カフェ&hit_per_page=100"


    # APIのURLを得る
url = api.format(key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
r = requests.get(url)
# 結果はJSON形式なのでデコードする
data = json.loads(r.text)

#for jsn_key in data:
 #print(jsn_key)
hit = data["hit_per_page"]

for i in range(0,hit):
 Cafe.objects.create(name=data["rest"][i]["name"], latitude=data["rest"][i]["latitude"], longitude=data["rest"][i]["longitude"])
 
#print(data["rest"][0]["latitude"])
#print(data["rest"][0]["longitude"])
#print(data["rest"][i]["name"]+" "+data["rest"][i]["latitude"]+" "+data["rest"][i]["longitude"])
