from os import path

from setuptools import find_packages, setup

dirname = path.abspath(path.dirname(__file__))
with open(path.join(dirname, 'README.md')) as f:
    long_description = f.read()

setup(
    name='featuretools_tsfresh_primitives',
    version='1.0.2',
    author='Feature Labs, Inc.',
    author_email='support@featurelabs.com',
    license='MIT',
    description='TSFresh primitives for featuretools',
    url='https://github.com/alteryx/featuretools-tsfresh-primitives/',
    classifiers=[
         'Development Status :: 3 - Alpha',
         'Intended Audience :: Developers',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3.8',
         'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
    tests_require=open('test-requirements.txt').readlines(),
    python_requires='>=3.7, <4',
    include_package_data=True,
    entry_points={
        'featuretools_plugin': [
            'tsfresh = featuretools_tsfresh_primitives.__init__',
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
