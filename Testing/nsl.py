ames = json.loads(r.content)
print(names)

newJson = []
for name in names:
    if name['status']['status'] == 'ERROR':
        newJson.append(name)
print(newJson)
tweet = []

df02 = df.DataFrame(newJson)