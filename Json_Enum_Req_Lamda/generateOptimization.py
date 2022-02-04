urls = ['https:\\www.google.com', 'https:\\www.yahoo.com', 'https:\\www.amazon.com',
        'https:\\www.bungie.net', 'https:\\www.anekdotov.net']

n = [x.split('\\')[1] for x in urls if '.com' in x]

z = (x.split('\\')[1] for x in urls if '.com' in x)
print(type(z))

next(z)
next(z)