from setuptools import setup, find_packages

setup(
    name="Ex_12",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    entry_points={
        'console_scripts': [
            'mycos=Ex_12.cli:main',
        ],
    },
)