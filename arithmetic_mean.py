try:
    x = list(map(int, input('Input some integer numbers: ').split()))
    f = lambda x: sum(x) / len(x)
    print("Arithmetic mean is:", f(x))
except ValueError as v:
    print(v)
