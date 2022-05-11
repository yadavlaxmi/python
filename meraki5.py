# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?

import json
a='{ "name":2, "age":30, "city":4j}'
b=json.dumps(a)
print(a)
