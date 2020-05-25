from setuptools import setup

setup(name='Payne4GALAH',
      version='0.1',
      description='Tools for fitting GALAH spectra with The Payne.',
      author='Yuan-Sen Ting',
      author_email='ting@ias.edu',
      license='MIT',
      url='https://github.com/tingyuansen/Payne4GALAH',
      package_dir = {},
      packages=['Payne4GALAH'],
      package_data={'Payne4GALAH':['other_data/*.npz','other_data/*.fits']},
      dependency_links = [],
      install_requires=[])
