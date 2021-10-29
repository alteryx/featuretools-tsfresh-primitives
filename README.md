# TSFresh Primitives

<p align="center">
    <a href="https://github.com/alteryx/featuretools-tsfresh-primitives/actions?query=branch%3Amain+workflow%3ATests" target="_blank">
        <img src="https://github.com/alteryx/featuretools-tsfresh-primitives/workflows/Tests/badge.svg?branch=main" alt="Tests" />
    </a>
    <a href="https://codecov.io/gh/alteryx/featuretools-tsfresh-primitives">
        <img src="https://codecov.io/gh/alteryx/featuretools-tsfresh-primitives/branch/main/graph/badge.svg?token=FtcPOJLpjj"/>
    </a>
    <a href="https://badge.fury.io/py/featuretools-tsfresh-primitives" target="_blank">
        <img src="https://badge.fury.io/py/featuretools-tsfresh-primitives.svg?maxAge=2592000" alt="PyPI Version" />
    </a>
    <a href="https://pepy.tech/project/featuretools-tsfresh-primitives" target="_blank">
        <img src="https://pepy.tech/badge/featuretools-tsfresh-primitives/month" alt="PyPI Downloads" />
    </a>
</p>
<hr>

### Installation

Install with pip:

```python
python -m pip install "featuretools[tsfresh]"
```

## Calculating Features

In `tsfresh`, this is how you can calculate a feature.

```python
from tsfresh.feature_extraction.feature_calculators import agg_autocorrelation

data = list(range(10))
param = [{'f_agg': 'mean', 'maxlag': 5}]
agg_autocorrelation(data, param=param)
```

```bash
[('f_agg_"mean"__maxlag_5', 0.1717171717171717)]
```

With tsfresh primtives in `featuretools`, this is how you can calculate the same feature.
```python
from featuretools.tsfresh import AggAutocorrelation

data = list(range(10))
AggAutocorrelation(f_agg='mean', maxlag=5)(data)
```

```bash
0.1717171717171717
```

## Combining Primitives

In `featuretools`, this is how to combine tsfresh primitives with built-in or other installed primitives.
```python
import featuretools as ft
from featuretools.tsfresh import AggAutocorrelation, Mean

entityset = ft.demo.load_mock_customer(return_entityset=True)
agg_primitives = [Mean, AggAutocorrelation(f_agg='mean', maxlag=5)]
feature_matrix, features = ft.dfs(entityset=entityset, target_dataframe_name='sessions', agg_primitives=agg_primitives)

feature_matrix[[
    'MEAN(transactions.amount)',
    'AGG_AUTOCORRELATION(transactions.amount, f_agg=mean, maxlag=5)',
]].head()
```
```
            MEAN(transactions.amount)  AGG_AUTOCORRELATION(transactions.amount, f_agg=mean, maxlag=5)
session_id
1                           76.813125                                           0.044268
2                           74.696000                                          -0.053110
3                           88.600000                                           0.007520
4                           64.557200                                          -0.034542
5                           70.638182                                          -0.100571
```
Notice that tsfresh primtives are applied across relationships in an entityset generating many features that are otherwise not possible.

```python
feature_matrix[['customers.AGG_AUTOCORRELATION(transactions.amount, f_agg=mean, maxlag=5)']].head()
```
```
            customers.AGG_AUTOCORRELATION(transactions.amount, f_agg=mean, maxlag=5)
session_id
1                                                    0.011102
2                                                   -0.001686
3                                                   -0.010679
4                                                    0.011204
5                                                   -0.010679
```

## Built at Alteryx Innovation Labs

<a href="https://www.alteryx.com/innovation-labs">
    <img src="https://evalml-web-images.s3.amazonaws.com/alteryx_innovation_labs.png" alt="Alteryx Innovation Labs" />
</a>
