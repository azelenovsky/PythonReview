

j = [1,2,3,4,5]

# Basic, inefficient
newj = []
for x in j:
    if x % 2 == 0:
        newj.append(x*2)

newj2 = [x*2 for x in j]
z = {x*2 for x in j}
f = {x:x*2 for x in j}

print(f)

g = [x for x in j if x % 2 == 0]

print(g)
print(type(g))