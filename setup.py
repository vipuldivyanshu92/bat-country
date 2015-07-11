from distutils.core import setup

setup(
    name='bat-country',
    packages=['batcountry'],
    version='0.2',
    description='A lightweight, extendible, easy to use Python package for deep dreaming and image generation with Caffe and CNNs',
    author='Adrian Rosebrock',
    author_email='adrian@pyimagesearch.com',
    url='https://github.com/jrosebr1/bat-country',
    download_url='https://github.com/jrosebr1/bat-country/tarball/0.1',
    license='MIT',
    install_requires=[
        'Pillow==2.9.0',
        'argparse==1.2.1',
        'decorator==3.4.2',
        'imutils==0.2.2',
        'matplotlib==1.4.3',
        'mock==1.0.1',
        'networkx==1.9.1',
        'nose==1.3.7',
        'numpy==1.9.2',
        'protobuf==2.6.1',
        'pyparsing==2.0.3',
        'python-dateutil==2.4.2',
        'pytz==2015.4',
        'scikit-image==0.11.3',
        'scipy==0.15.1',
        'six==1.9.0',
        'wsgiref==0.1.2',
    ],
    keywords=['computer vision', 'machine learning', 'deep learning',
        'convolutional neural network', 'deep dream', 'inceptionism'],
    classifiers=[],
)
