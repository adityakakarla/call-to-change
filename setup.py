from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='call_to_change',
    version='0.8.6',
    packages=find_packages(),
    install_requires=[
        'openai',
        'requests'
    ],
    long_description=description,
    long_description_content_type="text/markdown",

)