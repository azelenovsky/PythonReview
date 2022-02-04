import requests

response = requests.get('https://randomuser.me/api/?results=10')

data = response.json()

for user in data['results']:
    print(user['name']['first'])

def greet(greeting, name):
    """Returns a greeting  

    Args:
        greeting ([type]): [description]
        name ([type]): [description]

    Returns:
        [type]: [description]
    """
    return f'{greeting} {name}'

print(greet("Hello", "World"))