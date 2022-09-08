from setuptools import setup, find_packages 

setup(
    name='cleanh1b',  # Update this to a unique name
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    author='Aravind Satyanarayanan', 
    author_email='aravind.bedean@gmail.com',
    description='A package for cleaning data frames.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AravindSatyan/h1b-data-cleaner',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
