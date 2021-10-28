# Release Process

## 0. Pre-Release Checklist

Before starting the release process, verify the following:

* All work required for this release has been completed and the team is ready to release.
* [All Github Actions Tests are green on main](https://github.com/alteryx/featuretools-tsfresh-primitives/actions?query=branch%3Amain+workflow%3ATests).
* Get agreement on the version number to use for the release.

#### Version Numbering

TSFresh Primitives uses [semantic versioning](https://semver.org/). Every release has a major, minor and patch version number, and are displayed like so: `<majorVersion>.<minorVersion>.<patchVersion>`.

If you'd like to create a development release, which won't be deployed to pypi and conda and marked as a generally-available production release, please add a "dev" prefix to the patch version, i.e. `X.X.devX`. Note this claims the patch number--if the previous release was `0.12.0`, a subsequent dev release would be `0.12.dev1`, and the following release would be `0.12.2`, *not* `0.12.1`. Development releases deploy to [test.pypi.org](https://test.pypi.org/project/featuretools-tsfresh-primitives/) instead of to [pypi.org](https://pypi.org/project/featuretools-tsfresh-primitives).

## 1. Create TSFresh Primitives release on Github

#### Create release branch

1. Branch off of featuretools-tsfresh-primitives `main`. For the branch name, please use "release_vX.Y.Z" as the naming scheme (e.g. "release_v0.13.3"). Doing so will bypass our release notes checkin test which requires all other PRs to add a release note entry.

#### Bump version number

1. Bump `__version__` in `setup.py` and `featuretools-tsfresh-primitives/version.py`.

#### Checklist before merging:

* All tests are currently green on checkin and on `main`.
* PR has been reviewed and approved.
* Confirm with the team that `main` will be frozen until step 2 (Github Release) is complete.

## 2. Create Github Release

After the release pull request has been merged into the `main` branch, it is time draft the github release. [Example release](https://github.com/alteryx/featuretools-tsfresh-primitives/releases/tag/v0.0.2)

* The target should be the `main` branch
* The tag should be the version number with a v prefix (e.g. v0.13.3)
* Release title is the same as the tag
* Release description should be the full Release Notes updates for the release, including the line thanking contributors.  Contributors should also have their links changed from the docs syntax (:user:\`gsheni\`) to github syntax (@gsheni)
* This is not a pre-release
* Publishing the release will automatically upload the package to PyPI

## Release on conda-forge
1. A bot should automatically create a new PR in [conda-forge/featuretools-tsfresh-primitives-feedstock](https://github.com/conda-forge/featuretools-tsfresh-primitives-feedstock/pulls) - note, the PR may take up to a few hours to be created
2. Update requirements changes in `recipe/meta.yaml` (bot should have handled version and source links on its own)
3. After tests pass, a maintainer will merge the PR in
