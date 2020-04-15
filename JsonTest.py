import json

f = open('.\\config\\Recon1.json', encoding='UTF-8')
fdata = f.read()

conf = json.loads(fdata)
# conf = json.load(f)

print(conf)
print(conf['ReconciliationName'])

