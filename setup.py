from setuptools import find_packages, setup

setup(name='rivernet',
      version='0.1',
      description='Exploration of neural ODE processes and Fourier layers.',
      url='https://github.com/alasdairtran/rivernet',
      author='Alasdair Tran',
      author_email='alasdair.tran@anu.edu.au',
      license='MIT',
      packages=find_packages(),
      install_requires=[],
      entry_points='''
            [console_scripts]
            rivernet=rivernet.commands.__main__:app
      ''',
      zip_safe=False)