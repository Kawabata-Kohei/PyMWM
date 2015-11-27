#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.constants import c
import pymwm
lmax = 1.2
lmin = 0.545
fmin = c * 1e-8 / lmax
fmax = c * 1e-8 / lmin
params = {'core': {'shape': 'cylinder', 'size': 0.2,
                   'fill': {'model': 'air'}},
          'clad': {'model': 'gold_dl'},
          'bounds': {'lmax': lmax, 'lmin': lmin, 'limag': 10.0},
          'modes': {'num_n': 6, 'num_m': 2}}
wg = pymwm.create(params)
w = 2 * np.pi
wg.plot_betas(fmin, fmax, comp='real')
wg.plot_betas(fmin, fmax, comp='imag')
