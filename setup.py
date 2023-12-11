"""
Configuração do pacote image_processing 
para processamento de imagens.
"""
from setuptools import setup
from setuptools import find_packages


with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="rcvdigo",
    author_email="rcvdigo@gmail.com",
    description="My first package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)