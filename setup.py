from setuptools import find_packages,setup
#this finds all the packages required for ML based projects 
from typing import List 
#A function returns a list

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:  #this will return a list of requirements from requirements.txt
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        #when readlines goes through all the requirements it also adds up "\n" to replace that with blank:
        requirements=[req.replace("\n","") for req in requirements] 
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
        
setup(
 name ='mlproject',
 version ='0.0.1',
 author='piyush',
 author_email = 'piyushgopal172@gmail.com',
 packages=find_packages(),
 install_requires = get_requirements('requirements.txt'),
    
    
)