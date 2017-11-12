# Part One: `intro_to_tangent.py`

This routine is just me playing around with just the gut-simplest functionality
of Tangent: defining functions, and asking Tangent to automatically
differentiate them for me.

Right now it produces:

```
$ python intro_to_tangent.py
Hi, everybody!!
def dcube_x_plus_xdx(x, bb_plus_x=1.0):
    # Beginning of forward pass
    """f(x) = x^3 + x"""
    a = x * x
    b = a * x

    # Grad of: b = a * x
    _bb = tangent.unbroadcast(bb_plus_x, b)
    _bx4 = tangent.unbroadcast(bb_plus_x, x)
    bb = _bb
    bx = _bx4
    _ba = tangent.unbroadcast(bb * x, a)
    _bx3 = tangent.unbroadcast(bb * a, x)
    ba = _ba
    bx = tangent.add_grad(bx, _bx3)

    # Grad of: a = x * x
    _bx = tangent.unbroadcast(ba * x, x)
    _bx2 = tangent.unbroadcast(ba * x, x)
    bx = tangent.add_grad(bx, _bx)
    bx = tangent.add_grad(bx, _bx2)
    return bx

1 2 4.0 4
2 10 13.0 13
3 30 28.0 28
4 68 49.0 49
5 130 76.0 76
6 222 109.0 109
7 350 148.0 148
8 520 193.0 193
9 738 244.0 244
```

That first block is a verbose print-out of the automatically generated
derivative of a function that computes `x^3 + x` for a scalar `x`.

The second block iterates through several scalars, `x = 1, 2, ..., 9`, and
displays:
* The value `x`,
* The value of the function at `x`, `f(x) = x^3 + x`
* Tangent's version of the value of the derivative of `f` at `x`
* My own manual implementation of the derivative of `f` at `x`

It's great that Tangent's version agrees with mine!  Predictable, but great.
