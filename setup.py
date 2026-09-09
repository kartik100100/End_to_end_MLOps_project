from setuptools import setup,find_packages
from typing import List
HYPHON_E_DOT = "-e ."

def get_requires(file_path:str)->List[str]:
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("/n"," ") for req in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
    return requirements


setup(
    name = "MLproject",
    version="0.1",
    author="Kartik",
    author_email="kartikshivnani01@gmail.com",
    packages=find_packages(),
    install_requires=get_requires("requirements.txt")
)