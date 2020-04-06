"""
PyCLES
Desc: This is an implementation of the Common Language Effect Size (CLES) in Python
Author: Matthew Kovacs
Date: 04/05/20
"""

import numpy as np

from scipy.stats import norm


def nonparametric_cles(a, b, half_credit=True) -> float:
    """Nonparametric solver for the common language effect size.  This solves 
    for the probability that a random draw from `a` will be greater than a random 
    draw from `b` using a brute force approach.
    
    If half_credit=True then equal values between vectors will be granted half points.
    
    e.g.
        nonparametric_cles([0, 1], [0, 0], True) >> 0.75
        nonparametric_cles([0, 1], [0, 0], False) >> 0.5
        nonparametric_cles([1, 1], [0, 0]) >> 1.0
        nonparametric_cles([0, 0], [1, 1]) >> 0.0
    """
    
    m = np.subtract.outer(a, b)
    m = np.sign(m)
    
    if half_credit:
        m = np.where(m == 0, 0.5, m)
    m = np.where(m == -1, 0, m)
    
    return np.mean(m)


def parametric_cles(a, b):
    """Parametric solver for the common language effect size. This function
    assumes that your data is normally distributed.  It returns the probability
    that a random draw from `a` will be greater than a random draw from `b` using
    the normal cumulative distribution function."""

    ma, mb = np.mean(a), np.mean(b)
    sd = np.sqrt(ma**2 + mb**2)

    return norm.cdf(x=0, loc=mb-ma, scale=sd)

