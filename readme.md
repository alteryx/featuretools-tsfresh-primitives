# Featuretools TSFresh Primitives
### Installation
```python
pip install 'featuretools[tsfresh]'
```
## Calculating Features
In `tsfresh`, this is how to calculate a feature.
```python
from tsfresh.feature_extraction.feature_calculators import agg_autocorrelation

data = list(range(10))
param = [{'f_agg': 'mean', 'maxlag': 5}]
agg_autocorrelation(data, param=param)
```
```
[('f_agg_"mean"__maxlag_5', 0.1717171717171717)]
```
With tsfresh primtives in `featuretools`, this is how to calculate the same feature.
```python
from featuretools.tsfresh import AggAutocorrelation

data = list(range(10))
AggAutocorrelation(f_agg='mean', maxlag=5)(data)
```
```
0.1717171717171717
```
## Combining Primitives
In `featuretools`, this is how to combine tsfresh primitives with built-in or other installed primitives.
```python
import featuretools as ft
from featuretools.tsfresh import AggAutocorrelation, Mean

entityset = ft.demo.load_mock_customer(return_entityset=True)
agg_primitives = [Mean, AggAutocorrelation(f_agg='mean', maxlag=5)]
feature_matrix, features = ft.dfs(entityset=entityset, target_entity='sessions', agg_primitives=agg_primitives)

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
