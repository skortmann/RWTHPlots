#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Definition of RWTH standard theme for plotting.

# Installation via
pip install -e .

# to check succesful installation
import matplotlib.pyplot as plt
plt.style.available

# for simple usage
import matplotlib.pyplot as plt
plt.style.use('rwth-latex')

# release note: certain charcters need special escaping such as
$ % & ~ ^ \ { } \( \) \[ \]

#Temporary styling
with plt.style.context('dark_background'):
    plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
plt.show()

all credits go out to John D. Garret https://github.com/garrettj403/SciencePlots

Institut für Elektrische Anlagen und Netze, Digitalisierung und Energiewirtschaft (IAEW)
(c) 2022, Steffen Kortmann
"""

import atexit
import glob
import os
import shutil

import matplotlib
from setuptools import setup
from setuptools.command.install import install


def install_styles():
    # Find all style files
    stylefiles = glob.glob('styles/**/*.mplstyle', recursive=True)
    # Find stylelib directory (where the *.mplstyle files go)
    print("Your style sheets are located at: {}".format(os.path.join(matplotlib.__path__[0], 'mpl-data', 'stylelib')))
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)
    # Copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in stylefiles:
        print(os.path.basename(stylefile))
        shutil.copy(
            stylefile,
            os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))


class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)


# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='RWTHPlots',
    version='1.0.0',
    author="Steffen Kortmann",
    author_email="steffen.kortmann@rwth-aachen.de",
    description="Adding standard themes with RWTH Aachen University colous to matplotlib",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    keywords=[
        "matplotlib-style-sheets",
        "matplotlib-figures",
        "scientific-papers",
        "thesis-template",
        "matplotlib-styles",
        "python"
    ],
    url="https://github.com/skortmann/cmap_rwth_colours",
    install_requires=['matplotlib', ],
    cmdclass={'install': PostInstallMoveFile, },
)