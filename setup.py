from setuptools import setup,find_packages
from typing import List

Hyphen_e_dot="-e ."

def get_requirement(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as f:
        requirement=f.readlines()
        requirement=[req.replace("\n","") for req in requirement]

        if Hyphen_e_dot in requirement:
            requirement.remove(Hyphen_e_dot)

        return requirement



setup(
    name="src",
    version="0.0.1",
    author="arshia",
    author_email="aishanaaza@gmail.com",
    install_requires=get_requirement("requirements.txt"),
    package=find_packages()


)
 


