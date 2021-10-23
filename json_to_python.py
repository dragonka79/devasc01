import json
jsonstr = """{"people" : [{"firstName": "Joe","lastName": "Jackson","gender": "male","age": 28,"number": "7349282382","Active": true}]}"""

jsonobj = json.loads(jsonstr)

print(jsonobj)