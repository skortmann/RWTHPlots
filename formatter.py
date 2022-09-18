#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition of figure size for using Matplotlib with LaTeX.

example of usage:
x = np.linspace(0, 2 * np.pi, 100)
# Initialise figure instance
fig, ax = plt.subplots(1, 1, figsize=set_size(width))

or for multiple figures: fig, ax = plt.subplots(5, 2, figsize=set_size(width, subplots=(5, 2)))

# Plot
ax.plot(x, np.sin(x))
ax.set_xlim(0, 2 * np.pi)
ax.set_xlabel(r'$\theta$')
ax.set_ylabel(r'$\sin (\theta)$')

# Save and remove excess whitespace
fig.savefig('example_1.pdf', format='pdf', bbox_inches='tight')

all credits go out to Jack Walton https://jwalton.info/Embed-Publication-Matplotlib-Latex/

Institut für Elektrische Anlagen und Netze, Digitalisierung und Energiewirtschaft (IAEW)
(c) 2022, Steffen Kortmann
"""

def set_size(width, fraction=1, subplots=(1, 1)):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float or string
            Document width in points, or string of predined document type
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    if width == 'thesis':
        width_pt = 426.79135
    elif width == 'beamer':
        width_pt = 307.28987
    else:
        width_pt = width

    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)