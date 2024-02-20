from setuptools import setup, find_packages

setup(
    name='runes',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'langchain',
    ],
    entry_points={
        'console_scripts': [
            'runes=runes.example_usage:main',
        ],
    },
)
