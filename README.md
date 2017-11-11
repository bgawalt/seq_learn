# Sequence learning: Self study

Follow along as I try and teach myself recurrent neural nets by way of the
[Tangent](https://github.com/google/tangent) library.

I have a background in machine learning, and a solid grip on the fundamentals.
But neural net stuff, I've mostly just watched unfold.  I get the concepts
well enough, but there's now a whole language and system and culture and
curriculum that I've never fully participated in.

This repo is set up to slowly progress from those basic fundamentals --
auto-differentiation, gradient descent, feed-forward networks -- until we reach
the big-time: recurrent neural nets for learning over sequences.

You can find the scripts which implement each of these little incremental
chapters in the `scripts` directory, and corresponding "director's
commentary" in the `walkthrough` directory.  Each part is named `pt001_blahblah`
for part one, `pt002_yadayada` for part two, and so on.

My goal is to make this as broadly readable as possible.  I think anyone who's
taken some pre-calculus, with a sense of what it means to take a derivative of a
function, should be able to follow the progression.  By the end, you should be
able to build a (humble) recurrent neural net from scratch, no matter what you
knew at the outset -- that's the ideal.

The state of the art is complicated, but the simplest implementation of a
recurrent neural net doesn't have to be.  Or at least, we can build it up one
simple step at a time.

So if anything seems ambiguous, hand-wavy, or underspecified, treat that as a
bug.  Let me know where things got confusing, and I'll fix it.  I'm `bgawalt@`
on Twitter, and `bgawalt@gmail` on email.  There are plenty of quick-start
tutorials out there for deep learning.  I'd like this instead to take the scenic
route, and leave as few "exercises for the reader" as possible.

(This level of detail and from-scratch-ness is valuable to me just as a
self-study.  It should leave nothing for me to be confused about if I ever
refer back to any of this when I'm doing some new project four years from now.)

## Table of contents:

* `pt001_intro_to_tangent`: Defines a simple polynomial function of a scalar.
  Asks Tangent to build a new function which provides the gradient of that
  polynomial.  Checks the Tangent version of the gradient matches the same
  results we get from a manually-specified version of the gradient.

### Roadmap

Here's the basic trajectory I see this taking:

* ~~Auto-differentiate a scalar function.~~ (Done!)
* Auto-differentiate a function with multiple input variables.
* Use auto-differentiation to minimize a univariate function.
* Use auto-differentiation to minimize a multivariate function.
* Define and train a neural net classifier using auto-differentiation --
  probably using the MNIST digit set.
  * Simple logistic regression binary classifier (no hidden layer)
  * Add a hidden layer to the binary classifier
  * Upgrade the output layer to support multiple classes
* Define and build an autoencoder.  Use it to synthesize new data examples.
* Define a neural net with recurrent state -- probably a reimplementation of
  "CharRNN".  Use it to synthesize new strings.

## Set up

To get the code to run, I first ran these commands, after setting up a new
`virtualenv`:

```
pip install --upgrade pip
pip install tangent
```

(I should probably figure out why my `mkvirtualenv` was creating an environment
with such a stale version of `pip` that it couldn't find the `tf-nightly`
dependency that Tangent was looking for.)
