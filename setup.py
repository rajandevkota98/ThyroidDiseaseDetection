from setuptools import find_packages, setup
from typing import List

REQUIRED_FILE_NAME = 'requirements.txt'
def get_requirements()->List[str]:
    with open(REQUIRED_FILE_NAME) as file:
        required_list = file.readlines()
    required_list = [requirement_name.replace('\n', '') for requirement_name in required_list]

    if '-e .' in required_list:
        required_list.remove('-e .')
    return required_list

setup(
    name = 'Thyroid',
    version = '0.0.1',
    author = 'Rajan',
    author_email = 'r.devkota.98@gmail.com',
    package = find_packages(),
    install_requires = get_requirements(),
)


