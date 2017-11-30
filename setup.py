from setuptools import setup

setup(
    name='cyscore',
    version='0.2.3',
    license='GPL',
    description='score abstraction for csound written in python',
    author='Tim Pauli',
    author_email='tim.pauli@folkwang-uni.de',
    url='https://github.com/inkeye/cyscore',
    packages=['cyscore'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires='>=3.5'
)
