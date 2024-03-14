from setuptools import find_packages
from setuptools import setup
import os

cuda_version = os.environ.get('CUDA_VERSION')

version = '0.1.1'
name = 'neutestlib'

using_cuda = True
if cuda_version == '11':
  name += '_cu11'
elif cuda_version == '12':
  name += '_cu12'
else:
  using_cuda = False

with open('README.md') as f:
  _long_description = f.read()

d = dict(
  name=name,
  packages=['neutestlib'],
  version=version,
  description='C++/CUDA Library for NeurAI',
  long_description=_long_description,
  long_description_content_type='text/markdown',
  author='CNAEIT',
  include_package_data=True,
  install_requires=['numpy'],
  python_requires='>=3.8',
  license='GPL-3.0 License')

setup(**d)
