from setuptools import setup, find_packages

setup(
    name='BDF2CSV',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[  
        'click',
        'dbfread',
        'chardet'
    ],
    include_package_data=True,
    description='DBF to CSV file convert',
    author='SantosPereira',
    author_email='pedrohenriquelemam@gmail.com',
    url='https://github.com/SantosPereira/BDF2CSV',
)
