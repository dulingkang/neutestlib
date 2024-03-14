from setuptools import find_packages
from setuptools import setup
import os

cuda_version = os.environ.get('CUDA_VERSION')

version = '0.1.0'

using_cuda = True
if cuda_version == '11':
  version += '+cu11'
elif cuda_version == '12':
  version += '+cu12'
else:
  using_cuda = False

with open('README.md') as f:
  _long_description = f.read()

d = dict(
  name='neurailib',
  version=version,
  description='C++/CUDA Library for NeurAI',
  long_description=_long_description,
  long_description_content_type='text/markdown',
  author='CNAEIT',
  packages=find_packages(),
  include_package_data=True,
  install_requires=['numpy'],
  python_requires='>=3.8',
  license='GPL-3.0 License')

setup(**d)
