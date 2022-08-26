from setuptools import setup, find_packages

with open("./requirements.txt") as requirement_file:
    requirements = requirement_file.read().split()

setup(
    name='cmap_rwth_colours',
    version='0.0.3',
    packages=find_packages(),
    url='',
    license='MIT License',
    author='Steffen Kortmann',
    author_email='',
    description='',
    long_description=open('README.md').read(),
    install_requires=requirements
)

