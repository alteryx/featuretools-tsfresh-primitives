from setuptools import find_packages, setup

setup(
    name='featuretools_tsfresh_primitives',
    version='0.1.0',
    author='Feature Labs, Inc.',
    author_email='support@featurelabs.com',
    description='TSFresh primitives for featuretools',
    license='MIT',
    install_requires=['tsfresh>=0.11.2', 'featuretools>=0.7.0'],
    tests_require=open('test-requirements.txt').readlines(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'featuretools_plugin': [
            'tsfresh = featuretools_tsfresh_primitives.__init__',
        ],
    },
)
