import pandas as pd


def catbind(a, b):
    # concatenate categorical series in pandas
    concatenated = pd.concat([pd.Series(a.astype("str")),
                              pd.Series(b.astype("str"))])
    return pd.Categorical(concatenated)
