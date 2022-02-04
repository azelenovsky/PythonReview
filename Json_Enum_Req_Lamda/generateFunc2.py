def GenFunc():
    with open('text.txt', encoding='utf-8') as r:
        for x in r:
            yield x
            
p = GenFunc()

print(next(p))
print(next(p))

for i in p:
    print(i)