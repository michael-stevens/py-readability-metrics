#!/user/bin/env python

from setuptools import setup

setup(
    name='py-readability',
    version='0.0.1',
    description='Calculate readability scores. e.g. Gunning Fog',
    author='Erin Hengel',
    url='https://github.com/cdimascio/py-readability',
    packages=['py-readabilitiy'],
    install_requires=['spacy>=2.0.16'],
    package_data={'readability': [], '': ['README.md', 'LICENSE']},
    package_dir={'readabiliity': 'readabiliity'},
    include_package_data=True,
    author_email='cdimascio@gmail.com',
    license='MIT',
    zip_safe=False,
)
