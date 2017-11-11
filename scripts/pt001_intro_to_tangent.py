import tangent


def cube_x_plus_x(x):
    """f(x) = x^3 + x"""
    a = x * x
    b = a * x
    return b + x


def expected_deriv(x):
    """f'(x) = 3*x^2 + 1"""
    return 3*x*x + 1


def main():
    print "Hi, everybody!!"
    df = tangent.grad(cube_x_plus_x, verbose=1)
    for i in range(1, 10):
        print i, cube_x_plus_x(i), df(i), expected_deriv(i)


if __name__ == "__main__":
    main()
