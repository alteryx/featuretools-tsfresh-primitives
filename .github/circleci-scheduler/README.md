# CircleCI Scheduler

A GitHub Action for scheduling CircleCI dynamically.

## Install

In your repository, add the following lines to `.github/workflows/schedule.yml`:

```yaml
on:
  schedule:
    - cron:  '*/5 * * * *'

name: CircleCI Scheduler
jobs:
  Featuretools:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - uses: FeatureLabs/circleci-scheduler@master
      env:
        REPOSITORY: featurelabs/featuretools
        EVENT: Latest Commit to Master
        WITHIN: 'days=1'
        TOKEN : ${{ secrets.TOKEN }}
```

Then, add the following secrets to the repository settings:
  - `TOKEN`

## Usage