import json
file=open("swathi.json","w")
a="{1:2,3:4,5:6}"
json.dump(a,file)