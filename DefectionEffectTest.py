import os
import pandas as pd
from FactorSynthesis import raw_data_dict
from YearDate import *
import numpy as np
import statsmodels.api as sm
from DataVisualizing import *
from ShareListDelistSelection import get_annual_on_df
from TimeSeries import *
from VisualizationTools import plot_bar
from ICTest import get_return_anl

"""
The code is to test the effect that the financial defections bring about
"""

raw_data_list = \
    ['rcv', 'oth_rcv', 'notes_rcv', 'inventories', 'goodwill', 'depr_fa_coga_dpba', 'roe', 'equity', 'waa', 'assets']

# raw_data_list = raw_data_dict.keys()


def retrieve_raw_data(rw_data_list):

    """
    :param rw_data_list: the raw data id list
    :return: df_raw_data_dict: the dict whose keys are the  raw data id and
    whose values are the dataframes for raw data
    """

    df_raw_data_dict = dict()

    """
    The path of the raw data files
    """
    path_source = "/home/aeront/PycharmProjects/TXLCScreen/FactorReservoir/"

    for raw_data_id in rw_data_list:
        filename = raw_data_dict[raw_data_id][2]
        path_filename_source = "".join([path_source, filename])
        df_raw_data = pd.read_pickle(path_filename_source, compression='bz2')

        df_raw_data_dict[raw_data_id] = df_raw_data

    return df_raw_data_dict


def factor_create(df_raw_dict):
    """
    :param df_raw_dict:  the raw data dict whose keys are the raw data id and whose
    values are the dataframes for the raw data
    :return: df_factor: the dataframe for the factor
    """

    df_dlt = df_raw_dict['rcv'] + df_raw_dict['oth_rcv'] + df_raw_dict['notes_rcv']

    df_asset = df_data_dict['asset']
    df_factor = df_dlt / df_asset
    df_factor.replace(to_replace=[-np.inf, np.inf], value=np.nan, inplace=True)

    return df_factor


def delta_value(df_raw_dict):
    """
    :param df_raw_dict:  the raw data dict whose keys are the raw data id and whose
    values are the dataframes for the raw data
    :return: df_delta: the dataframe for the delta
    """
    df_dlt = - df_raw_dict['rcv'] - df_raw_dict['oth_rcv'] - df_raw_dict['notes_rcv'] \
             - df_raw_dict['inventories'] - df_raw_dict['goodwill'] + df_raw_dict['depr_fa_coga_dpba']

    # df_dlt = df_raw_dict['rcv'] + df_raw_dict['oth_rcv'] + df_raw_dict['notes_rcv']

    df_equity = df_data_dict['equity']
    df_delta = df_dlt / df_equity
    df_delta.replace(to_replace=[-np.inf, np.inf], value=np.nan, inplace=True)
    df_roe = df_raw_dict['roe'] / 100
    df_delta = (1 - df_roe) * df_delta

    df_delta = df_delta.rolling(1).mean()

    return df_delta


def regression_test(fac_id, df_fac_slice, df_roe_slice):

    path_factor = "".join(["./FactorTest", "/", fac_id])
    path_factor_pic = "".join([path_factor, '/', 'Pic'])

    if not os.path.exists(path_factor_pic):
        os.makedirs(path_factor_pic)
    else:
        pass

    # excl_anl_dict = get_excl_dict(src='local')
    stats_test_dict = dict()
    for ii_fy in fy_list:

        ii_py = fy_py_mapper[ii_fy]
        if ii_py is None:
            continue
        srs_factor = df_fac_slice.loc[ii_fy, :]
        srs_valid_factor = srs_factor.notna()

        srs_ret = df_roe_slice.loc[ii_py, :]
        srs_valid_ret = srs_ret.notna()

        sec_mean = srs_factor.mean()
        sec_std_dev = srs_factor.std()
        down_bound = sec_mean - 1 * sec_std_dev
        up_bound = sec_mean + 3 * sec_std_dev
        down_bound = 0
        up_bound = 30

        print("The mean of the factor is: {0}\n".format(sec_mean))
        print("The standard deviation of the factor is: {0}\n".format(sec_std_dev))
        print("The range in consideration of the factor is {0}: {1} \n".format(down_bound, up_bound))

        srs_range_valid = \
            srs_ret.apply(lambda factor_value: True if down_bound <= factor_value <= up_bound else False) \
            & srs_factor.apply(lambda factor_value: True if -2.0 <= factor_value <= 1.0 else False)

        srs_valid_all = srs_valid_factor & srs_valid_ret & srs_range_valid

        srs_exog = srs_factor.loc[srs_valid_all]
        srs_endog = srs_ret.loc[srs_valid_all]

        if srs_endog.size == 0:
            continue
        else:
            np_exog = np.array(srs_exog).transpose()
            np_endog = np.array(srs_endog).transpose()
            np_exog = sm.add_constant(np_exog)

            model = sm.OLS(np_endog, np_exog)
            result = model.fit()
            print(result.summary())

            y_fitted = result.fittedvalues
            plt_reg = plot_regression(srs_exog, srs_endog, y_fitted, fac_id)
            pic_filename = "".join([path_factor_pic, "/", fac_id, "_", "regression", "_", ii_py, ".png"])
            plt_reg.savefig(pic_filename, format="png")
            plt_reg.close()

            stats_section_test_list = list()

            stats_section_test_list.append(result.fvalue)
            stats_section_test_list.append(result.f_pvalue)
            stats_section_test_list.append(result.tvalues[0])
            stats_section_test_list.append(result.pvalues[0])
            stats_section_test_list.append(result.tvalues[1])
            stats_section_test_list.append(result.pvalues[1])

            stats_test_dict[ii_py] = stats_section_test_list

    index = ['f value', 'f_pvalue', 'intcpt t value', 'intcpt t test p value', 'linear t values', 'linear t test p values']
    df_reg_test = pd.DataFrame(data=stats_test_dict, index=index)
    df_reg_test = df_reg_test.T

    return df_reg_test


def roe_delta_compare(wind_code, df_on, df_roe, df_delta):

    srs_roe = df_roe.loc[:, wind_code]
    srs_roe = srs_roe.iloc[:-1]
    srs_delta = df_delta.loc[:, wind_code]
    srs_delta = srs_delta[:-1]
    srs_on = df_on.loc[:, wind_code]
    srs_on = srs_on[:-1]

    srs_roe_valid = srs_roe.notna()
    srs_delta_valid = srs_delta.notna()
    srs_valid = srs_roe_valid & srs_delta_valid & srs_on

    srs_roe = srs_roe[srs_valid]
    srs_delta = srs_delta[srs_valid]

    abscissa = srs_roe.index.tolist()
    ordinate_roe = srs_roe.values.tolist()
    ordinate_delta = srs_delta.values.tolist()

    import matplotlib
    matplotlib.rcParams['axes.unicode_minus'] = False
    fig = plt.figure()
    plt.ioff()

    ax1 = fig.add_subplot(111)
    # font = {'color': 'blue'}
    ax1.plot(abscissa, ordinate_roe, 'b', label='roe')
    ax1.set_ylabel('roe')
    ax1.set_ylim(-50, 50)
    # ax1.legend()

    ax2 = ax1.twinx()  # this is the important function
    # font = {'color': 'red'}
    ax2.plot(abscissa, ordinate_delta, 'r', label='delta')
    ax2.set_ylabel('delta')
    # ax2.legend()

    fig.legend()
    plt.show()


if __name__ == "__main__":

    df_return_slice = get_return_anl()
    srs_eqy = df_return_slice.prod(axis=0)

    df_data_dict = retrieve_raw_data(raw_data_list)
    df_delta_equity_ratio = delta_value(df_data_dict)
    df_waa = df_data_dict['waa']

    df_on_list = get_annual_on_df()
    df_on_total_list = df_on_list.apply(lambda x: False if False in x.values.tolist() else True, axis=0)

    def specific_range(srs_data):

        for ii_data in srs_data[0:-1].tolist():
            if -100 < ii_data < 100:
                pass
            else:
                return False

        return True

    df_specific_range_list = df_waa.apply(specific_range, axis=0)

    df_waa = df_waa.loc[:, df_on_total_list & df_specific_range_list]
    # stability_value = df_waa.apply(stability, axis=0)
    # stability_rank = stability_value.rank(method='first', pct=False)
    # stability_rank = stability_rank.astype('int')
    # wind_code_select = stability_rank[stability_rank < 30].index.tolist()
    growth_value = df_waa.apply(growth, axis=0, by="regression")
    # growth_rank = growth_value.rank(method='first', ascending=False, pct=False)
    growth_rank = growth_value.rank(method='first', ascending=True, pct=False)
    growth_rank = growth_rank.astype('int')
    # wind_code_select = growth_rank[growth_rank < 30].index.tolist()
    #
    # eqy_list = [srs_eqy.loc[ii_wind_code] for ii_wind_code in wind_code_select]
    wind_code_select = growth_rank.index.tolist()

    # eqy_list = [srs_eqy.loc[ii_wind_code] for ii_wind_code in wind_code_select]
    # plt.ioff()
    # plt.hist(eqy_list, bins=100)
    # plt.show()
    # title = u"growth_regression"
    # plot_bar(wind_code_select, eqy_list, title)


    # a = df_waa.mean(axis=1, skipna=True)
    # b = df_waa.loc['2018', :]
    factor_id = 'delta'
    wind_code_check = '002050.SZ'
    wind_code_list = df_waa.columns.tolist()
    # for ii_wind_code in wind_code_list:
    #     roe_delta_compare(ii_wind_code, df_on_list, df_waa, df_delta_equity_ratio)
    roe_delta_compare(wind_code_check, df_on_list, df_waa, df_delta_equity_ratio)
    # df_reg_delta = regression_test(factor_id, df_delta_equity_ratio, df_roe)
    a = 1

