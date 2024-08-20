import os

# Define the desired folder structure
structure = {
    'Plotsgrid': {
        'plotsgrid': {
            '__init__.py': '',
            'plotsgrid.py': '# Your class code here'
        },
        'tests': {
            'test_plotsgrid.py': '# Your test cases'
        },
        'README.md': '# Plotsgrid Package\n\nDescription of the Plotsgrid package.',
        'setup.py': """from setuptools import setup, find_packages

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
""",
        'setup.cfg': """[metadata]
name = plotsgrid
version = 0.1.0
author = kgraghav
description = A package for creating grid plots
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/kgraghav/plotsgrid
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
packages = find:
install_requires =[
        'seaborn','matplotlib']
python_requires = >=3.6
"""
    }
}

# Function to create the folder structure
def create_structure(base, structure):
    for name, contents in structure.items():
        path = os.path.join(base, name)
        if isinstance(contents, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, contents)  # Recursive call for nested directories
        else:
            with open(path, 'w') as f:
                f.write(contents)

# Create the folder structure
create_structure('.', structure)  # Use current directory as base