from setuptools import setup, find_packages

setup(
    name = "punits",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['punits_script'],
    install_requires = []
)