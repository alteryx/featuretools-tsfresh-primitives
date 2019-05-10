from setuptools import find_packages, setup

setup(
    name='featuretools_tsfresh_primitives',
    version='0.1.0',
    author='Feature Labs, Inc.',
    author_email='support@featurelabs.com',
    license='MIT',
    install_requires=['tsfresh>=0.11.2', 'featuretools>=0.7.0'],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'featuretools_plugin': [
            'tsfresh = featuretools_tsfresh_primitives',
        ],
    },
)
