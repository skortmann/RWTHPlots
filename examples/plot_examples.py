#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Plot examples of RWTHPlots styles.

all credits go out to John D. Garret https://github.com/garrettj403/SciencePlots

Institut für Elektrische Anlagen und Netze, Digitalisierung und Energiewirtschaft (IAEW)
(c) 2022, Steffen Kortmann
"""

import os
import numpy as np
import matplotlib.pyplot as plt

import os
if not os.path.exists("examples/figures"):
    os.makedirs("examples/figures")

def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


pparam = dict(xlabel='Voltage (mV)', ylabel='Current ($\mu$A)')

x = np.linspace(0.75, 1.25, 201)

with plt.style.context(['rwth-custom']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100, 200, 300, 500]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(**pparam)
    fig.savefig('examples/figures/fig1.pdf')
    fig.savefig('examples/figures/fig1.jpg', dpi=300)

with plt.style.context(['rwth-latex']):
    fig, ax = plt.subplots()
    for p in [10, 20, 40, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    # Note: $\mu$ doesn't work with Times font (used by ieee style)
    ax.set_ylabel(r'Current (A)')  
    fig.savefig('examples/figures/fig2a.pdf')
    fig.savefig('examples/figures/fig2a.jpg', dpi=300)

with plt.style.context(['rwth-latex', 'grid']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    # Note: $\mu$ doesn't work with Times font (used by ieee style)
    ax.set_ylabel(r'Current (\textmu A)')  
    fig.savefig('examples/figures/fig2b.pdf')
    fig.savefig('examples/figures/fig2b.jpg', dpi=300)

with plt.style.context(['rwth-latex', 'blue']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    # Note: $\mu$ doesn't work with Times font (used by ieee style)
    ax.set_ylabel(r'Current (\textmu A)')  
    fig.savefig('examples/figures/fig2c.pdf')
    fig.savefig('examples/figures/fig2c.jpg', dpi=300)

with plt.style.context(['rwth-latex', 'red']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    # Note: $\mu$ doesn't work with Times font (used by ieee style)
    ax.set_ylabel(r'Current (\textmu A)')  
    fig.savefig('examples/figures/fig2d.pdf')
    fig.savefig('examples/figures/fig2d.jpg', dpi=300)

with plt.style.context(['rwth-latex', 'extended']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    # Note: $\mu$ doesn't work with Times font (used by ieee style)
    ax.set_ylabel(r'Current (\textmu A)')  
    fig.savefig('examples/figures/fig2e.pdf')
    fig.savefig('examples/figures/fig2e.jpg', dpi=300)


with plt.style.context(['rwth-word', 'extended']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    # Note: $\mu$ doesn't work with Times font (used by ieee style)
    ax.set_ylabel(r'Current (A)')  
    fig.savefig('examples/figures/fig3.pdf')
    fig.savefig('examples/figures/fig3.jpg', dpi=300)