def print_params(*params):
    print(params)

print_params('Testing')
print_params(1,2,3)

def print_params_2(title, *params):
    print(title)
    print(params)

print_params_2('Params:', 1, 2, 3)

def print_params_3(**params):
    print(params)

print_params_3(x=1, y=2, z=3)

def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)

print_params_4(1,2,3, 5,6,7, foo=1,bar=2)
