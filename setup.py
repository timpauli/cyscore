from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    lic = f.read()

setup(
    name='cyscore',
    version='0.1.0',
    description='score abstraction for csound written in python',
    long_description=readme,
    author='Tim Pauli',
    author_email='tim.pauli@folkwang-uni.de',
    url='https://github.com/inkeye/cyscore',
    license=lic,
    packages=['cyscore']
)
