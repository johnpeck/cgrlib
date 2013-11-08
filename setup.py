from distutils.core import setup
setup(
    name = 'cgrlib',
    packages = ['cgrlib', 'cgrlib.test'], # this must be the same as the name above
    scripts=['bin/cgr-capture.py'],
    version = '0.1.0',
    license='LICENSE.txt',
    description = 'Capture waveforms with the CGR-101 USB oscilloscope',
    author = 'John Peck',
    author_email = 'john@johnpeck.info',
    url = 'https://github.com/johnpeck/cgr-capture',
    install_requires=[
        "numpy >= 1.7.1",
        "configobj >= 4.7.2",
        "gnuplot-py >= 1.8",
        "colorlog >= 2.0.0"
    ],
    keywords = ['testing', 'logging', 'example'] # arbitrary keywords
)