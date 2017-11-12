"""This one taught me the gradient is taken with respect to the first parameter
of the function."""

import random
import tangent


def easy_quadratic(x, y):
    """f(x, y) = x^2 + y^2"""
    return (x * x) + (y * y)


def main():
    # By running this, I've "discovered" that the gradient is always calculated
    # with respect to the first argument of the function.
    df = tangent.grad(easy_quadratic, verbose=1)
    # I'd expect, then, that the gradient is always just d/dx{x^2} = 2x,
    # regardless of y's value.
    for xi in range(-1, 2):
        for yi in range(-1, 2):
            print xi, '\t', yi, '\t', easy_quadratic(xi, yi),
            print df(xi, yi), '\t', 2*xi
    # Let's try a collection of random values, too:
    print ''
    for _ in range(10):
        xi = 10*random.random() - 5
        yi = 10*random.random() - 5
        print xi, '\t', yi, ':',
        print df(xi, yi) ==  2*xi


if __name__ == "__main__":
    main()
