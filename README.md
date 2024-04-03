# nonlocal

## python code 1
```python
x = 15
def outer():
    x = 10
    print(x)
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()
    print(x)

outer()
print(x)
```

## output

```cmd
10
11
11
15
```