from setuptools import setup

setup(
    name='featuretools_tsfresh_primitives',
    version='0.0.0',
    author='Feature Labs, Inc.',
    author_email='support@featurelabs.com',
    install_requires=['tsfresh>=0.11.2', 'featuretools>=0.7.0'],
    packages=['featuretools_tsfresh_primitives'],
    entry_points={
        'featuretools_plugin': [
            'tsfresh = featuretools_tsfresh_primitives',
        ],
    },
)
