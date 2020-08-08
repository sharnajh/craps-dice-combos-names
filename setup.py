from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='craps-dice-combos-names',
    version='0.1.127.1',
    description='A miniscule library for generating and identifying dice combos in craps',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sharnajh/craps_pkg.git',
    author='Sharna Hossain',
    author_email='sharnajh@gmail.com',
    license='BSD 2-clause',
    packages=['craps_pkg'],

    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Turn Based Strategy',
        'Topic :: Games/Entertainment :: Simulation',
        'Topic :: Games/Entertainment :: Arcade'
    ],
)
