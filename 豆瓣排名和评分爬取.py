import requests
import json
import jsonpath
url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?items_only=1&start=0&count=20&for_mobile=1"
headers = {
    "referer" : "https://m.douban.com/subject_collection/tv_american",
    "user-agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
}
response = requests.get(url,headers= headers).text
dict_response = json.loads(response)
name = jsonpath.jsonpath(dict_response,"$..title")
value = jsonpath.jsonpath(dict_response,"$..value")
#第二种取值，字典取值，列表取值和字典便利
#name = dict_response['subject_collection_items']
#for item in name:
   # name =item['title']
   # value = item['rating']['value']
   # print((name:value))



with open("item.json","w",encoding="utf-8") as f:
    for item in zip(name, value):
        dict_item = {}
        dict_item["电影名称"] = item[0]
        dict_item["电影评分"] = item[1]
        print(dict_item)
        f.write(json.dumps(dict_item,ensure_ascii=False,indent=2)+';\n')

