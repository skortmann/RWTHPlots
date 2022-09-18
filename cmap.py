#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition of RWTH colour schemes for lines and maps.

# Change default colorset (for lines) and colormap (for maps).
plt.rc('axes', prop_cycle=plt.cycler('color', list(rwth_cset('rwth_100'))))
plt.cm.register_cmap('standard_RWTH_discrete', rwth_cmap('standard_RWTH_discrete'))
plt.rc('image', cmap='standard_RWTH_discrete')

all credits go out to Paul Tol //personal.sron.nl/~pault/

Institut für Elektrische Anlagen und Netze, Digitalisierung und Energiewirtschaft (IAEW)
(c) 2022, Steffen Kortmann
"""

import copy
from operator import index
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, to_rgba_array

def discretemap(colormap, hexclrs):
    """
    Produce a colormap from a list of discrete colors without interpolation.
    """
    clrs = to_rgba_array(hexclrs)
    clrs = np.vstack([clrs[0], clrs, clrs[-1]])
    cdict = {}
    for ki, key in enumerate(('red','green','blue')):
        cdict[key] = [ (i/(len(clrs)-2.), clrs[i, ki], clrs[i+1, ki]) for i in range(len(clrs)-1) ]
    return LinearSegmentedColormap(colormap, cdict)


class RWTHcmaps(object):
    """
    Class RWTHcmaps definition.
    """
    def __init__(self):
        """
        """
        self.cmap = None
        self.cname = None
        self.namelist = (
            'standard_RWTH_discrete', 'standard_RWTH', 
            'blue_RWTH_discrete', 'blue_RWTH',
            'black_RWTH_discrete', 'black_RWTH',
            'magenta_RWTH_discrete', 'magenta_RWTH',
            'yellow_RWTH_discrete', 'yellow_RWTH',
            'petrol_RWTH_discrete', 'petrol_RWTH',
            'turquoise_RWTH_discrete', 'turqoise_RWTH',
            'green_RWTH_discrete', 'green_RWTH',
            'maygreen_RWTH_discrete', 'maygreen_RWTH',
            'orange_RWTH_discrete', 'orange_RWTH',
            'red_RWTH_discrete', 'red_RWTH',
            'bordeaux_RWTH_discrete', 'bordeaux_RWTH',
            'violet_RWTH_discrete', 'violet_RWTH',
            'purple_RWTH_discrete', 'purple_RWTH',
            'continuous_RWTH_discrete',
            'rolling_RWTH_discrete',
            'extended_RWTH_discrete')

        self.funcdict = dict(
            zip(self.namelist,
                (self.standard_RWTH_discrete, self.standard_RWTH,
                self.blue_RWTH_discrete, self.blue_RWTH,
                self.black_RWTH_discrete, self.black_RWTH,
                self.magenta_RWTH_discrete, self.magenta_RWTH,
                self.yellow_RWTH_discrete, self.yellow_RWTH,
                self.petrol_RWTH_discrete, self.petrol_RWTH,
                self.turquoise_RWTH_discrete, self.turquoise_RWTH,
                self.green_RWTH_discrete, self.green_RWTH,
                self.maygreen_RWTH_discrete, self.maygreen_RWTH,
                self.orange_RWTH_discrete, self.orange_RWTH,
                self.red_RWTH_discrete, self.red_RWTH,
                self.bordeaux_RWTH_discrete, self.bordeaux_RWTH,
                self.violet_RWTH_discrete, self.violet_RWTH,
                self.purple_RWTH_discrete, self.purple_RWTH,
                self.continuous_RWTH_discrete, self.rolling_RWTH_discrete,
                self.extended_RWTH_discrete)))

    def standard_RWTH_discrete(self):
        """
        Define colormap 'RWTH_discrete'.
        """
        clrs = ['#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                '#A11035', '#612158', '#7A6FAC']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def standard_RWTH(self):
        """
        Define colormap 'RWTH'.
        """
        clrs = ['#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                '#A11035', '#612158', '#7A6FAC']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def blue_RWTH_discrete(self):
        """
        Define colormap 'blue_RWTH_discrete'.
        """
        clrs = ['#00549F', '#407FB7', '#8EBAE5', '#C7DDF2', '#E8F1FA']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def blue_RWTH(self):
        """
        Define colormap 'blue_RWTH'.
        """
        clrs = ['#00549F', '#407FB7', '#8EBAE5', '#C7DDF2', '#E8F1FA']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def black_RWTH_discrete(self):
        """
        Define colormap 'black_RWTH_discrete'.
        """
        clrs = ['#000000', '#646567', '#9C9E9F', '#CFD1D2', '#ECEDED']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def black_RWTH(self):
        """
        Define colormap 'black_RWTH'.
        """
        clrs = ['#000000', '#646567', '#9C9E9F', '#CFD1D2', '#ECEDED']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def magenta_RWTH_discrete(self):
        """
        Define colormap 'magenta_RWTH_discrete'.
        """
        clrs = ['#E30066', '#E96088', '#F19EB1', '#F9D2DA', '#FDEEF0']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def magenta_RWTH(self):
        """
        Define colormap 'magenta_RWTH'.
        """
        clrs = ['#E30066', '#E96088', '#F19EB1', '#F9D2DA', '#FDEEF0']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def yellow_RWTH_discrete(self):
        """
        Define colormap 'yellow_RWTH_discrete'.
        """
        clrs = ['#FFED00', '#FFF055', '#FFF59B', '#FFFAD1', '#FFFDEE']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def yellow_RWTH(self):
        """
        Define colormap 'yellow_RWTH'.
        """
        clrs = ['#FFED00', '#FFF055', '#FFF59B', '#FFFAD1', '#FFFDEE']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def petrol_RWTH_discrete(self):
        """
        Define colormap 'petrol_RWTH_discrete'.
        """
        clrs = ['#006165', '#2D7F83', '#7DA4A7', '#BFD0D1', '#E6ECEC']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def petrol_RWTH(self):
        """
        Define colormap 'petrol_RWTH'.
        """
        clrs = ['#006165', '#2D7F83', '#7DA4A7', '#BFD0D1', '#E6ECEC']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def turquoise_RWTH_discrete(self):
        """
        Define colormap 'turquoise_RWTH_discrete'.
        """
        clrs = ['#0098A1', '#00B1B7', '#89CCCF', '#CAE7E7', '#EBF6F6']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def turquoise_RWTH(self):
        """
        Define colormap 'turquoise_RWTH'.
        """
        clrs = ['#0098A1', '#00B1B7', '#89CCCF', '#CAE7E7', '#EBF6F6']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def green_RWTH_discrete(self):
        """
        Define colormap 'green_RWTH_discrete'.
        """
        clrs = ['#57AB27', '#8DC060', '#B8D698', '#DDEBCE', '#F2F7EC']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def green_RWTH(self):
        """
        Define colormap 'green_RWTH'.
        """
        clrs = ['#57AB27', '#8DC060', '#B8D698', '#DDEBCE', '#F2F7EC']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def maygreen_RWTH_discrete(self):
        """
        Define colormap 'maygreen_RWTH_discrete'.
        """
        clrs = ['#BDCD00', '#D0D95C', '#E0E69A', '#F0F3D0', '#F9FAED']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def maygreen_RWTH(self):
        """
        Define colormap 'maygreen_RWTH'.
        """
        clrs = ['#BDCD00', '#D0D95C', '#E0E69A', '#F0F3D0', '#F9FAED']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def orange_RWTH_discrete(self):
        """
        Define colormap 'orange_RWTH_discrete'.
        """
        clrs = ['#F6A800', '#FABE50', '#FDD48F', '#FEEAC9', '#FFF7EA']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def orange_RWTH(self):
        """
        Define colormap 'orange_RWTH'.
        """
        clrs = ['#F6A800', '#FABE50', '#FDD48F', '#FEEAC9', '#FFF7EA']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def red_RWTH_discrete(self):
        """
        Define colormap 'orange_RWTH_discrete'.
        """
        clrs = ['#CC071E', '#D85C41', '#E69679', '#F3CDBB', '#FAEBE3']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def red_RWTH(self):
        """
        Define colormap 'orange_RWTH'.
        """
        clrs = ['#CC071E', '#D85C41', '#E69679', '#F3CDBB', '#FAEBE3']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def bordeaux_RWTH_discrete(self):
        """
        Define colormap 'bordeaux_RWTH_discrete'.
        """
        clrs = ['#A11035', '#B65256', '#CD8B87', '#E5C5C0', '#F5E8E5']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def bordeaux_RWTH(self):
        """
        Define colormap 'bordeaux_RWTH'.
        """
        clrs = ['#A11035', '#B65256', '#CD8B87', '#E5C5C0', '#F5E8E5']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def violet_RWTH_discrete(self):
        """
        Define colormap 'violet_RWTH_discrete'.
        """
        clrs = ['#612158', '#834E75', '#A8859E', '#D2C0CD', '#EDE5EA']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def violet_RWTH(self):
        """
        Define colormap 'violet_RWTH'.
        """
        clrs = ['#612158', '#834E75', '#A8859E', '#D2C0CD', '#EDE5EA']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def purple_RWTH_discrete(self):
        """
        Define colormap 'purple_RWTH_discrete'.
        """
        clrs = ['#7A6FAC', '#9B91C1', '#BCB5D7', '#DEDAEB', '#F2F0F7']
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def purple_RWTH(self):
        """
        Define colormap 'purple_RWTH'.
        """
        clrs = ['#7A6FAC', '#9B91C1', '#BCB5D7', '#DEDAEB', '#F2F0F7']
        self.cmap = LinearSegmentedColormap.from_list(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def continuous_RWTH_discrete(self, lut=None):
        """
        Define colormap 'continuous_RWTH_discrete'.
        """
        clrs = ['#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                '#A11035', '#612158', '#7A6FAC',
                '#407FB7', '#646567', '#E96088', '#FFF055', '#2D7F83',
                '#00B1B7', '#8DC060', '#D0D95C', '#FABE50', '#D85C41',
                '#B65256', '#834E75', '#9B91C1',
                '#8EBAE5', '#9C9E9F', '#F19EB1', '#FFF59B', '#7DA4A7',
                '#89CCCF', '#B8D698', '#E0E69A', '#FDD48F', '#E69679',
                '#CD8B87', '#A8859E', '#BCB5D7',
                '#C7DDF2', '#CFD1D2', '#F9D2DA', '#FFFAD1', '#BFD0D1',
                '#CAE7E7', '#DDEBCE', '#F0F3D0', '#FEEAC9', '#F3CDBB',
                '#E5C5C0', '#D2C0CD', '#DEDAEB',
                '#E8F1FA', '#ECEDED', '#FDEEF0', '#FFFDEE', '#E6ECEC',
                '#EBF6F6', '#F2F7EC', '#F9FAED', '#FFF7EA', '#FAEBE3',
                '#F5E8E5', '#EDE5EA', '#F2F0F7'
                ]
        indexes = []
        for i in range(5):
            indexes.append([i*13 for i in range(i+1)])
        for j in range(12):
            for i in range(5):
                indexes.append(copy.deepcopy(indexes[-1]))
                indexes[-1].append(i*13+(j+1))
        if lut == None or lut < 1 or lut > (13*5):
            lut = 23
        self.cmap = discretemap(self.cname, [ clrs[i] for i in indexes[lut-1] ])
        if lut == 23:
            self.cmap.set_bad('#777777')
        else:
            self.cmap.set_bad('#FFFFFF')

    def rolling_RWTH_discrete(self, lut=None):
        """
        Define colormap 'rolling_RWTH_discrete'.
        """
        clrs = ['#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                '#A11035', '#612158', '#7A6FAC',
                '#407FB7', '#646567', '#E96088', '#FFF055', '#2D7F83',
                '#00B1B7', '#8DC060', '#D0D95C', '#FABE50', '#D85C41',
                '#B65256', '#834E75', '#9B91C1',
                '#8EBAE5', '#9C9E9F', '#F19EB1', '#FFF59B', '#7DA4A7',
                '#89CCCF', '#B8D698', '#E0E69A', '#FDD48F', '#E69679',
                '#CD8B87', '#A8859E', '#BCB5D7',
                '#C7DDF2', '#CFD1D2', '#F9D2DA', '#FFFAD1', '#BFD0D1',
                '#CAE7E7', '#DDEBCE', '#F0F3D0', '#FEEAC9', '#F3CDBB',
                '#E5C5C0', '#D2C0CD', '#DEDAEB',
                '#E8F1FA', '#ECEDED', '#FDEEF0', '#FFFDEE', '#E6ECEC',
                '#EBF6F6', '#F2F7EC', '#F9FAED', '#FFF7EA', '#FAEBE3',
                '#F5E8E5', '#EDE5EA', '#F2F0F7'
                ]
        self.cmap = discretemap(self.cname, clrs)
        self.cmap.set_bad('#FFFFFF')

    def extended_RWTH_discrete(self, lut=None):
        """
        Define colormap 'extended_RWTH_discrete'.
        """
        clrs = ['#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                '#A11035', '#612158', '#7A6FAC',
                '#407FB7', '#646567', '#E96088', '#FFF055', '#2D7F83',
                '#00B1B7', '#8DC060', '#D0D95C', '#FABE50', '#D85C41',
                '#B65256', '#834E75', '#9B91C1',
                '#8EBAE5', '#9C9E9F', '#F19EB1', '#FFF59B', '#7DA4A7',
                '#89CCCF', '#B8D698', '#E0E69A', '#FDD48F', '#E69679',
                '#CD8B87', '#A8859E', '#BCB5D7',
                '#C7DDF2', '#CFD1D2', '#F9D2DA', '#FFFAD1', '#BFD0D1',
                '#CAE7E7', '#DDEBCE', '#F0F3D0', '#FEEAC9', '#F3CDBB',
                '#E5C5C0', '#D2C0CD', '#DEDAEB',
                '#E8F1FA', '#ECEDED', '#FDEEF0', '#FFFDEE', '#E6ECEC',
                '#EBF6F6', '#F2F7EC', '#F9FAED', '#FFF7EA', '#FAEBE3',
                '#F5E8E5', '#EDE5EA', '#F2F0F7'
                ]
        indexes = []
        for i in range(13):
            indexes.append([i for i in range(i+1)])
        for j in range(4):
            for i in range(13):
                indexes.append(copy.deepcopy(indexes[-1]))
                indexes[-1].insert((i*2+1+j),(j*13+i+13))
        if lut == None or lut < 1 or lut > (13*5):
            lut = 23
        self.cmap = discretemap(self.cname, [ clrs[i] for i in indexes[lut-1] ])
        if lut == 23:
            self.cmap.set_bad('#777777')
        else:
            self.cmap.set_bad('#FFFFFF')

    def show(self):
        """
        List names of defined colormaps.
        """
        print(' '.join(repr(n) for n in self.namelist))

    def get(self, cname='extended_RWTH_discrete', lut=None):
        """
        Return requested colormap, default is 'extended_RWTH_discrete'.
        """
        self.cname = cname
        if cname == 'extended_RWTH_discrete':
            self.extended_RWTH_discrete(lut)
        else:
            self.funcdict[cname]()
        return self.cmap


def rwth_cmap(colormap=None, lut=None):
    """
    Continuous and discrete color sets for ordered data.
    
    Return a matplotlib colormap.
    Parameter lut is ignored for all colormaps except 'standard_RWTH_discrete'.
    """
    obj = RWTHcmaps()
    if colormap == None:
        return obj.namelist
    if colormap not in obj.namelist:
        colormap = 'standard_RWTH_discrete'
        print('*** Warning: requested colormap not defined,',
              'known colormaps are {}.'.format(obj.namelist),
              'Using {}.'.format(colormap))
    return obj.get(colormap, lut)


def rwth_cset(colorset=None):
    """
    Discrete color sets for qualitative data.

    Define a namedtuple instance with the colors.
    Examples for: cset = rwth_cset(<scheme>)
      - cset.red and cset[1] give the same color (in default 'bright' colorset)
      - cset._fields gives a tuple with all color names
      - list(cset) gives a list with all colors
    """
    from collections import namedtuple
    
    namelist = ('rwth_100', 'rwth_75', 'rwth_50', 'rwth_25', 'rwth_10')
    if colorset == None:
        return namelist
    if colorset not in namelist:
        colorset = 'rwth_100'
        print('*** Warning: requested colorset not defined,',
              'known colorsets are {}.'.format(namelist),
              'Using {}.'.format(colorset)) 

    if colorset == 'rwth_100':
        cset = namedtuple('Bcset',
                    'blue black magenta yellow petrol turquoise green maygreen orange red bordeaux violet purple')
        return cset('#00549F', '#000000', '#E30066', '#FFED00', '#006165',
                    '#0098A1', '#57AB27', '#BDCD00', '#F6A800', '#CC071E',
                    '#A11035', '#612158', '#7A6FAC')

    if colorset == 'rwth_75':
        cset = namedtuple('Hcset',
                    'blue black magenta yellow petrol turquoise green maygreen orange red bordeaux violet purple')
        return cset('#407FB7', '#646567', '#E96088', '#FFF055', '#2D7F83',
                    '#00B1B7', '#8DC060', '#D0D95C', '#FABE50', '#D85C41',
                    '#B65256', '#834E75', '#9B91C1')

    if colorset == 'rwth_50':
        cset = namedtuple('Vcset',
                    'blue black magenta yellow petrol turquoise green maygreen orange red bordeaux violet purple')
        return cset('#8EBAE5', '#9C9E9F', '#F19EB1', '#FFF59B', '#7DA4A7',
                    '#89CCCF', '#B8D698', '#E0E69A', '#FDD48F', '#E69679',
                    '#CD8B87', '#A8859E', '#BCB5D7')

    if colorset == 'rwth_25':
        cset = namedtuple('Mcset',
                    'blue black magenta yellow petrol turquoise green maygreen orange red bordeaux violet purple')
        return cset('#C7DDF2', '#CFD1D2', '#F9D2DA', '#FFFAD1', '#BFD0D1',
                    '#CAE7E7', '#DDEBCE', '#F0F3D0', '#FEEAC9', '#F3CDBB',
                    '#E5C5C0', '#D2C0CD', '#DEDAEB')

    if colorset == 'rwth_10':
        cset = namedtuple('Mcset',
                    'blue black magenta yellow petrol turquoise green maygreen orange red bordeaux violet purple')
        return cset('#E8F1FA', '#ECEDED', '#FDEEF0', '#FFFDEE', '#E6ECEC',
                    '#EBF6F6', '#F2F7EC', '#F9FAED', '#FFF7EA', '#FAEBE3',
                    '#F5E8E5', '#EDE5EA', '#F2F0F7')


def main():

    from matplotlib import pyplot as plt

    # Show colorsets rwth_cset(<scheme>).
    schemes = rwth_cset()
    fig, axes = plt.subplots(ncols=len(schemes), figsize=(9, 3.5))
    fig.subplots_adjust(top=0.9, bottom=0.02, left=0.02, right=0.92)
    for ax, scheme in zip(axes, schemes):
        cset = rwth_cset(scheme)
        names = cset._fields
        colors = list(cset)
        for name, color in zip(names, colors):
            ax.scatter([], [], c=color, s=80, label=name)
        ax.set_axis_off()
        ax.legend(loc=2)
        ax.set_title(scheme)
    plt.show()

    # Show colormaps rwth_cmap(<scheme>). 
    schemes = rwth_cmap()
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, axes = plt.subplots(nrows=len(schemes))
    fig.subplots_adjust(top=0.98, bottom=0.02, left=0.2, right=0.99)
    for ax, scheme in zip(axes, schemes):
        pos = list(ax.get_position().bounds)
        ax.set_axis_off()
        ax.imshow(gradient, aspect=4, cmap=rwth_cmap(scheme))
        fig.text(pos[0] - 0.01, pos[1] + pos[3]/2., scheme, va='center', ha='right', fontsize=10)
    plt.show()

    # Show colormaps rwth_cmap('continous_RWTH_discrete', <lut>). 
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, axes = plt.subplots(nrows=13*5)
    fig.subplots_adjust(top=0.98, bottom=0.02, left=0.25, right=0.99)
    for lut, ax in enumerate(axes, start=1):
        pos = list(ax.get_position().bounds)
        ax.set_axis_off()
        ax.imshow(gradient, aspect=4, cmap=rwth_cmap('continuous_RWTH_discrete', lut))
        fig.text(pos[0] - 0.01, pos[1] + pos[3]/2., 'continuous_RWTH_discrete, ' + str(lut), va='center', ha='right', fontsize=8)
    plt.show()

    # Show colormaps rwth_cmap('extended_RWTH_discrete', <lut>). 
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, axes = plt.subplots(nrows=13*5)
    fig.subplots_adjust(top=0.98, bottom=0.02, left=0.25, right=0.99)
    for lut, ax in enumerate(axes, start=1):
        pos = list(ax.get_position().bounds)
        ax.set_axis_off()
        ax.imshow(gradient, aspect=4, cmap=rwth_cmap('extended_RWTH_discrete', lut))
        fig.text(pos[0] - 0.01, pos[1] + pos[3]/2., 'extended_RWTH_discrete, ' + str(lut), va='center', ha='right', fontsize=8)
    plt.show()


if __name__ == '__main__':
    main()