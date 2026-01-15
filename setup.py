"""
This file helps in setting up the application as a package and deploy into pypi for example. Contributes to open-source. Anybody can 
use this package. 
"""

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of all requirements
    """
    requirements=[]
    with open('/Users/saivenkatasravangudepu/Desktop/ML_Project/requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


# Consider this as the metadata about your package
setup(
    name="ml_project" ,
    version="0.0.1",
    author="Sravan Gudepu" ,
    author_email="gsvsra1@gmail.com" ,
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)