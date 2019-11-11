from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='pdext',
      version='0.0.1',
      description='Pandas Extention python module',
      long_description=readme(),
      url='https://github.com/malneni/PdExt',
      author='Venkatesh Malneni',
      author_email='malneni258@gmail.com',
      license='MIT',
      install_requires=['pandas', 'docx', 'numpy'],
      py_modules = ['pdext'],
      classifiers=["Programming Language :: Python :: 3.7"],
      zip_safe=False,
      )
