from setuptools import setup

setup(name='VaspGibbs',
      version='0.2.3',
      description='A simplified way to get Gibbs free energy from Vasp calculations',
      url='https://github.com/ftherrien/VaspGibbs',
      author='Felix Therrien',
      author_email='felix.therrien@gmail.com',
      license='MIT',
      packages=['vaspgibbs'],
      python_requires='>=3',
      install_requires=[
          'numpy',
      ],
      scripts=['vasp_gibbs'],)
