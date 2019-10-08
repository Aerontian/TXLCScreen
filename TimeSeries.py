# -*- coding: UTF-8 -*
import pandas as pd
import numpy as np
import statsmodels.api as sm


def stability(srs_data):

    std_dev = srs_data[:-1].std()

    return std_dev


def growth(srs_data, by='diff'):

    if by == 'diff':

        if srs_data[:-1].diff().std() == 0:
            return np.inf
        else:
            return srs_data[:-1].diff().mean() / srs_data[:-1].diff().std()

    elif by == 'regression':

        srs_exog = pd.Series(range(len(srs_data[:-1])))
        srs_endog = srs_data[:-1]

        np_exog = np.array(srs_exog).transpose()
        np_endog = np.array(srs_endog).transpose()
        np_exog = sm.add_constant(np_exog)

        model = sm.OLS(np_endog, np_exog)
        result = model.fit()

        k = result.params[1]
        p = result.pvalues[1]

        # if k > 0:
        #     return p / 2
        # else:
        #     return 1.0

        if p < 0.05 and k > 0:
            return -k
        elif p > 0.05 and k > 0:
            return -k / 2
        else:
            return 1.0


if __name__ == "__main__":

    srs_test = pd.Series([9.1, 8, 6.9, 5.9, 5.01, 4.1, 3, 2, 1.09])
    a = growth(srs_test, by="regression")
    a=1