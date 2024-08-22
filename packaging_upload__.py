''' Upload package to PIP'''
# pip install setuptools wheel
#python setup.py sdist bdist_wheel
import twine
!twine upload dist/*