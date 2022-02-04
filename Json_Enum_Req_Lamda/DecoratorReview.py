#decorator practice

def decor(f):
    def wrapper():
        print("Decorator Code")
        f()
        print("Decorator Code 2")
    return wrapper

@decor # make = decor(make)
def make():
    enter = input("Enter something...")
    print(enter)
    

    
make()