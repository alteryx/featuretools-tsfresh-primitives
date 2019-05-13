#!/bin/bash

# Clone featuretools-tsfresh-primitives repo
git clone https://github.com/FeatureLabs/featuretools-tsfresh-primitives.git /home/circleci/featuretools-tsfresh-primitives
# Checkout specified commit
cd /home/circleci/featuretools-tsfresh-primitives
git checkout "${1}"
# Remove build artifacts
rm -rf .eggs/ rm -rf dist/ rm -rf build/
# Create distributions
python setup.py sdist bdist_wheel
# Install twine, module used to upload to pypi
pip install --user twine
# Upload to pypi or testpypi
echo "Upoading to ${2:-pypi} . . ."
python -m twine upload dist/* -r "${2:-pypi}"
