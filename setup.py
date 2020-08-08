from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='craps-pkg-sharnajh',
    version='0.1.12',
    description='Returns 2 dice rolls with associated craps nickname',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sharnajh/craps_pkg.git',
    author='Sharna Hossain',
    author_email='sharnajh@gmail.com',
    license='BSD 2-clause',
    packages=['craps_pkg'],

    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
