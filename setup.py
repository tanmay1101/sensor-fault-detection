from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:
    
    
    """
    this Function will return list of requirements
    
    """
    
    requirement_list:List[str]=[]
    return requirement_list




setup (
    
    name= 'Sensor',
    version='0.0.1',
    author= 'Tanmay',
    author_email='dwiveditanmay102@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements()
)