from setuptools import setup
from typing import List

HYPEN_E = '-e .'
def get_requirements(file_name) -> List[str]:
    try:
        with open(file_name, 'r') as files:
            req = [file.replace("\n", "") for file in files.readlines() if file != HYPEN_E]
            return req
    except Exception as e:
        return str(e)
    

    setup(
        name = 'DATA_FUSION',
        version = '1.0.0.3',
        description = 'Data_fusion with automatation',
        author = 'Victor Oshionwu',
        author_email= 'victoropeyemi97@outlookcom',
        packages = find_packages(),
        license = "MIT License",
        install_requires = get_requirements()
    )
