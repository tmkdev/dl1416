from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='dl1416',
      version='0.21dev',
      description='DL1416 RPI.GPIO Based Driver',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Hardware :: Hardware Drivers',
      ],
      url='https://github.com/tmkdev/dl1416.git',
      author='T KOLODY - TMKDEV',
      author_email='tekolody@gmail.com',
      license='MIT',
      packages=['dl1416'],
      install_requires=['RPi.GPIO'],
      zip_safe=False)
