from setuptools import find_packages, setup
from typing import List


def get_requirements(filePath:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(filePath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
    

setup(
    name="mlProject",
    version='0.0.1',
    author='Ahmed Gamal',
      author_email='ahmedgamal52001@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
)


