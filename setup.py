from setuptools import setup,find_packages
from typing import List

PROJECT_NAME="ML Project modular coding"
VERSION="0.0.1"
AUTHOR="Hrishikesh Bhagawati"
AUTHOR_EMAILID="hrishikeshbhagawati@gmail.com"
DESCRIPTION="End to End ML project with deployement"

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT="-e ."

def get_requirements_list():
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
        requirement_list=[req_name.replace("\n","") for req_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

    return requirement_list

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    author_email = AUTHOR_EMAILID,
    description = DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

