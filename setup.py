from setuptools import setup

requirements = list()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = str()
with open('README.md') as f:
    readme = f.read()

setup(name='Bookkeeper',

      # PEP 440 -- Version Identification and Dependency Specification
      version='0.0.1',

      # Project description
      description='Learnig app',
      long_description=readme,

      # Author details
      author='Joshua Ugba',
      author_email='justjosh001@gmail.com',

      # Project details
      url='https://github.com/andela-jugba/Bookkeeper',
      license="GNU v3",

      # Project dependencies
      install_requires=requirements,
      )
