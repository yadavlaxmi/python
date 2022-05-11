# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?

import json
a={"4": 5, "6": 7, "1": 3, "2": 4}
a=sorted(a.items())
b={}
for i in a:
    b.update(a)
print(type(b))
c=json.dumps(b)
print(c)
print(type(c))