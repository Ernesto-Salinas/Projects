def print_arguments(*args):
    for x in args:
        if not isinstance(x, int):
            print(x)

print_arguments(2,7.8, "a", 10.0)