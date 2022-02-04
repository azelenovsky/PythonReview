def NonGenFunc():
    list_text = []
    with open('text.txt', encoding='utf-8') as r:
        for x in r:
            list_text.append(x)
    return list_text

def GenFunc():
    with open('text.txt', encoding='utf-8') as r:
        for x in r:
            yield x

for i in NonGenFunc():
    print(i.split())
    
for i in GenFunc():
    print(i.split())