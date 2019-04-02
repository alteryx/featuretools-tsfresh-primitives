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
from featuretools.primitives import AggAutocorrelation

data = list(range(10))
AggAutocorrelation(f_agg='mean', maxlag=5)(data)
```
```
0.1717171717171717
```
## Combining Primitives
In featuretools, this is how to combine tsfresh primitives with built-in or other installed primitives.
```python
import featuretools as ft
from featuretools.primitives import AggAutocorrelation, AvgTimeBetween

entityset = ft.demo.load_mock_customer(return_entityset=True)
agg_primitives = [AvgTimeBetween, AggAutocorrelation(f_agg='mean', maxlag=5)]
feature_matrix, features = ft.dfs(entityset=entityset, target_entity='sessions', agg_primitives=agg_primitives)
feature_matrix[['AVG_TIME_BETWEEN(transactions.transaction_time)', 'AGG_AUTOCORRELATION(transactions.amount, f_agg=mean, maxlag=5)']].head()
```
```
            AVG_TIME_BETWEEN(transactions.transaction_time)  AGG_AUTOCORRELATION(transactions.amount, f_agg=mean, maxlag=5)
session_id
1                                                      65.0                                           0.044268
2                                                      65.0                                          -0.053110
3                                                      65.0                                           0.007520
4                                                      65.0                                          -0.034542
5                                                      65.0                                          -0.100571
```
Notice that tsfresh primtives are applied across relationships in an entityset generating features that would otherwise not be possible.

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