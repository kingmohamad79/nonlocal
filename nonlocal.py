x = 15
def outer():
    x = 10
    print(x)
    def inner():
        x = 5
        print(x)
    inner()
    print(x)

outer()
print(x)