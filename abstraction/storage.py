def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

storage = {}
init(storage)
print(storage)

def lookup(data, label, name):
    return data[label].get(name)

print(lookup(storage, 'middle', 'Lie'))
