from setuptools import find_packages, setup


setup(
    name="mlProject",
    version='0.0.1',
    author='Ahmed Gamal',
      author_email='ahmedgamal52001@gmail.com',
      packages=find_packages(),
      install_requires=['pandas','numpy', 'matplotlib', 'seaborn', 'sklearn']
)


