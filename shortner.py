import requests
import json
url = "https://rel.ink/api/links/"
short ="https://rel.ink/"
data ={
  "url": "https://lkyoubuzz.tk"
}
o = requests.post(url=url,data=data)
res = json.loads(o.text)
link=res["hashid"]
short = short+link
print(short)



