from setuptools import setup

version = '0.1'

description = "Downloads pixa images."

setup(
    name="inventory",
    version=version,
    url='http://github.com/travishathaway',
    license='BSD',
    description=description,
    author='Travis Hathaway',
    author_email='travis.j.hathaway@gmail.com',
    packages=['getpixa'],
    install_requires=[
        'requests'
    ],
    entry_points="""
        [console_scripts]
        getpixa = getpixa.cli:main
    """,
    classifiers=[
        'Environment :: Console',
    ],
)
