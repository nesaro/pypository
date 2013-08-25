from setuptools import setup, find_packages
setup(name='pypository',
      version='0.1.0',
      description='Repository library for python objects',
      author='Nestor Arocha',
      author_email='nesaro@gmail.com',
      url='https://github.com/nesaro/pypository',
      packages = find_packages(exclude=['tests.*']),
     )

