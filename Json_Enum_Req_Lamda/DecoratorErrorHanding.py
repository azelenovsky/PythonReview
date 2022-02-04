def decor(f):
    def wrapper():
        try:
            h = f()
        except Exception:
            print("Repeat Input ...")
            h = f()
        return h
    return wrapper 

@decor #Illustration make = decor(make)
def make():
    enter = float(input("Enter a number..."))
    return enter

@decor
def make2():
    enter = float(input('Enter a number again'))
    return enter

    
make2()
make