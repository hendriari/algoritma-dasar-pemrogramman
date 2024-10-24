import json

data = '{"nama": "Hendri", "npm" : 19670119}'

mySelf = json.loads(data)

print("Nama :",mySelf["nama"], type(mySelf["nama"]), "\nNPM :", mySelf["npm"], type(mySelf['npm']))