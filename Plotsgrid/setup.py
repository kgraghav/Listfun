from setuptools import setup, find_packages

setup(
    name='plotsgrid',
    version='0.1.0',
    author='kgraghav',
    description='A package for creating grid plots',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kgraghav/plotsgrid',
    packages=find_packages(),
    install_requires=[
        'seaborn','matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
