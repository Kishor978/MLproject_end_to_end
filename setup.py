from setuptools import find_packages,setup
from typing import List

HYPEN_E_dot='-e .'    
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()         #read every line
        requirements=[req.replace ("\n","")for req in requirements]   #replace \n as it is present in every line
        if HYPEN_E_dot in requirements:         # to remove -e from the requirement.txt
            requirements.remove(HYPEN_E_dot)



setup(
    name='mlproject',
    version='0.0.1',
    author='kishor',
    author_email='thaunnakishor@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)

